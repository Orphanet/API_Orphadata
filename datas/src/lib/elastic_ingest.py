from typing import Dict, Generator, List, Union
from elasticsearch import helpers
from elasticsearch.client import Elasticsearch
import logging

logger = logging.getLogger(__name__)


class EsBulkInjector:
    """ Wrapper class to bulk inject documents to elasticsearch

        Parameters
        ----------        
        - es_client : Elasticsearch
            - Elasticsearch low-level client instance
        - index : str
            - Name of the index
        - mappings : Dict or None
            - Configuration for the index ({'mappings': {...}, 'settings': {...})
        - aliases : List[str]
            - List of aliases for the index
    """
    def __init__(self, es_client: Elasticsearch, index: str, doc_generator: Generator, max_chunk_bytes: float=100, **kwargs):
        self.es_client = es_client
        self.index = index
        self.doc_generator = doc_generator
        self.max_chunk_bytes = max_chunk_bytes

        self.mappings = kwargs['mappings'] if 'mappings' in kwargs else None
        self.aliases = kwargs['aliases'] if 'aliases' in kwargs else None

    def _check_index_exist(self) -> None:
        if self.es_client.indices.exists(index=self.index):
            logger.info("index {} exists. It will be removed and created again.".format(self.index))
            self.es_client.indices.delete(index=self.index, ignore=[400, 404])

    def _create_index(self) -> None:
        """Creates an index in Elasticsearch. If index exists, it is removed before before being created again."""
        self._check_index_exist()  
        self.es_client.indices.create(
            index=self.index,
            mappings=self.mappings,
            ignore=400,
        )
        if self.aliases:
            self._put_alias()
        self.es_client.indices.refresh(index=self.index)

    def _put_alias(self) -> None:
        for alias in self.aliases:
            self.es_client.indices.put_alias(index=self.index, name=alias)

    def _bulk(self) -> None:
        self._create_index()
        _success, _errors = helpers.bulk(
            client=self.es_client,
            index=self.index,
            actions=self.doc_generator,
            max_chunk_bytes=self.max_chunk_bytes,
            max_retries=3,
        )


        logger.info("- Number of success in document injection: {}".format(_success))
        logger.info("- Number of errors in document injection: {}".format(_errors))


    def run(self):
        self._bulk()

