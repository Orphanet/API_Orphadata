import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List, Union
import os

from dotenv import load_dotenv
from elasticsearch import Elasticsearch

from lib.config import ROOT_DIR
from lib.elastic_ingest import EsBulkInjector
from lib.es_mappings import MAPPING_BY_PRODUCTS


load_dotenv(ROOT_DIR / '.varenv')

FORMAT = '%(asctime)-26s %(name)-16s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger('orphadata_injection')
logging.getLogger("elasticsearch").setLevel(logging.WARNING)


def esConnector(url: str):
    """
    Parameters
    ----------
    url : str
        Keyword to indicate which ES instance to connect to.

        Value can be:

         - 'local': the url will be http://127.0.0.1:9200
         - 'remote' the connection parameters will taken from environment variables (port: 9243 by default)

    Returns
    -------
    Elasticsearch client instance
    """
    if url == 'local':
        es_client =  Elasticsearch(
            'http://127.0.0.1:9200',
            timeout=180,
            max_retries=3,
            retry_on_timeout=True
        )
    else:
        url = os.getenv('ELASTIC_URL', None)
        user = os.getenv('ELASTIC_USER', None)
        password = os.getenv('ELASTIC_PASS', None)

        if url and user and password:
            es_client = Elasticsearch(
                [url],
                port=9243,
                http_auth=(user, password),
                timeout=180, max_retries=3, retry_on_timeout=True
            )
        else:
            logger.error('Error: no profile configurations have been found to connect to the remote elasticsearch instance.')
            logger.error('Please ensure that the profile configurations are defined in environment variables.')
            exit()

    if es_client:
        logger.info('Successfully connected to ES instance: {}'.format(es_client))
        return es_client

def get_jsons(path: Union[str, Path], pattern: str=None) -> Union[Path, List]:
    """[summary]

    Parameters
    ----------
    path : Union[str, Path]
        Path to directory containing ES ready-to-inject JSON files

    Returns
    -------
    List
        List of Path instances of ES ready-to-inject JSON files 
    """
    match = '*{}*.json'.format(pattern) if pattern else '*.json'

    if isinstance(path, str):
        path = Path(path)

    if path.is_dir():
        return [x for x in path.glob(match)]
    
    if path.is_file() and path.exists():
        return path


def generate_actions(filename: str):
    with open(filename, 'r') as _file:
        for line in _file:
            if '{"index":' not in line:
                _line = json.loads(line)
                yield _line


def get_mappings(product: str) -> Dict:
    if product in MAPPING_BY_PRODUCTS:
        logger.info('A mapping settings have been found for {}'.format(product))
        return MAPPING_BY_PRODUCTS[product]
    else:
        logger.debug('No mapping settings have been found for {}'.format(product))
        return None


def bulk_inject(es_client: Elasticsearch, json_path: Union[str, Path, List], index: str=None):
    if not isinstance(json_path, List):
        json_path = [json_path]

    for json_filename in json_path:
        if not isinstance(json_filename, Path):
            json_filename = Path(json_filename)

        product = '_'.join(json_filename.stem.split('_')[1:]) if 'product3' not in json_filename.stem else 'product3'
        mappings = get_mappings(product=product)

        if not index:             
            _index = 'orphadata_{}'.format(json_filename.stem) if 'orphadata' not in json_filename.stem else json_filename.stem
        else:
            _index = index


        logger.info('Creating index {} and injecting documents from {}'.format(_index, json_filename))
        bulk_injector = EsBulkInjector(
            es_client=es_client,
            index=_index,
            doc_generator=generate_actions(filename=json_filename),
            mappings=mappings['mappings'],
            max_chunk_bytes=100
        )
        bulk_injector.run()


def parse_args():
    parser = argparse.ArgumentParser(description='Bulk inject ORPHADATA products in ES')
    parser.add_argument(
        "-path",
        required=False,
        nargs="?",
        type=str,
        help="Path or filename of JSON file(s)"
    )
    parser.add_argument(
        "-match",
        required=False,
        nargs="?",
        type=str,
        default="",
        help="String used to filter JSON filenames matching it (only if -path is a directory)"
    )
    parser.add_argument(
        "-index",
        required=False,
        nargs="?",
        type=str,
        default=None,
        help="Name of the index to create"
    )
    parser.add_argument(
        "-url",
        required=False,
        nargs="?",
        choices=("local", 'remote'),
        type=str,
        default="local",
        help="ES URL type: either 'local' or 'remote'"
    )
    parser.add_argument('--print', action='store_true')
    
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    path = args.path if args.path else ROOT_DIR / 'datas' / 'json_data'
    pattern = args.match
    url_type = args.url
    index = args.index


    json_filenames = get_jsons(path=path, pattern=pattern)
    if args.print:
        for _file in json_filenames:
            logger.info(' - ' + str(_file))
    else:
        es_client = esConnector(url=url_type)
        bulk_inject(es_client=es_client, json_path=json_filenames, index=index)


