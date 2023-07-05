from elasticsearch.client import Elasticsearch
import elasticsearch.exceptions as es_exceptions
from elasticsearch.helpers import scan as es_helpers_scan
from flask import make_response, current_app
import yaml

from api.config import Config
scroll_size = Config.ES_SIZE
scroll_timeout = Config.ES_SCROLL_TIMEOUT

# from api.config import scroll_size, scroll_timeout
# scroll_size = current_app.config.get('ES_SIZE')
# scroll_timeout = current_app.config.get('ES_SCROLL_TIMEOUT')


def handle_query(es, index, query, size=1):
    """
    Fetch the ES query and handle a first layer of error

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: optional number of responses to return
    :return: elasticsearch response object on success or error string
    """
    try:
        response = es.search(index=index, body=query, size=size)
        # print(response)
    except es_exceptions.NotFoundError:
        response = ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        response = ("ConnectionError type, Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        response = ("TransportError type, Elasticsearch node unavailable", 503)
    return response


def init_scroll_query(es, index, query, size, scroll_timeout):
    """
    Init a scrollable ES query and handle a first layer of error

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: optional number of responses to return PER SCROLL
    :param scroll_timeout: duration of scroll instance between calls
    :return: elasticsearch response object on success or error string
    """
    try:
        response = es.search(index=index, body=query, size=size, scroll=scroll_timeout)
        # print(response)
    except es_exceptions.NotFoundError:
        response = ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        response = ("Elasticsearch node unavailable", 503)
    return response


def next_scroll_query(es, sid, scroll_timeout=scroll_timeout):
    """
    Fetch a scrollable ES query and handle a first layer of error

    :param es: elasticsearch instance see elasticsearch module
    :param sid: scroll index return by previous call
    :param scroll_timeout: duration of scroll instance between calls
    :return: elasticsearch response object on success or error string
    """
    try:
        response = es.scroll(scroll_id=sid, scroll=scroll_timeout)
        # print(response)
    except es_exceptions.NotFoundError:
        response = ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        response = ("Elasticsearch node unavailable", 503)
    return response


def single_res(es, index, query):
    """
    When the query return a single object
    Handle the query with ES then perform error verification related to the response

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :return: single dictionary on success or string error code
    """
    response = handle_query(es, index, query)
    if isinstance(response, str) or isinstance(response, tuple):
        # ES node related error comes out as tuple or string
        pass
    else:
        try:
            response = response["hits"]["hits"][0]["_source"]
        except KeyError:
            response = ("Query not found", 404)
            # print(response)
        except IndexError:
            response = ("Query not found", 404)
            # print(response)
    return response


def multiple_res(es, index, query, size=scroll_size):
    """
    When the query can return a reasonable (N << 10000) number of object (ES limit = 10000)
    Handle the query with ES then perform error verification related to the response

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: number of responses to return
    :return: list of dictionary on success or string error code
    """
    response = handle_query(es, index, query, size)
    if isinstance(response, str) or isinstance(response, tuple):
        # ES node related error comes out as tuple or string
        pass
    else:
        try:
            response = [elem["_source"] for elem in response["hits"]["hits"]]
        except KeyError:
            response = ("Query not found", 404)
            # print(response)
        except IndexError:
            response = ("Query not found", 404)
            # print(response)
        if isinstance(response, list) and not response:
            response = ("Query not found", 404)
    return response


def uncapped_res(es, index, query, size=scroll_size, scroll_timeout=scroll_timeout):
    """
    When the query can return more object than the ES limit (10000)
    Handle the query with ES then perform error verification related to the response

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: number of responses to return
    :param scroll_timeout: duration of scroll instance between calls
    :return: list of dictionary on success or string error code
    """
    response = init_scroll_query(es, index, query, size=size, scroll_timeout=scroll_timeout)
    if isinstance(response, str) or isinstance(response, tuple):
        # ES node related error comes out as tuple or string
        return response
    else:
        try:
            sid = response["_scroll_id"]
        except KeyError:
            pass
        try:
            data = [elem["_source"] for elem in response["hits"]["hits"]]
        except KeyError:
            data = ("Query not found", 404)
            # print(response)
        except IndexError:
            data = ("Query not found", 404)
            # print(response)
        if isinstance(data, list) and not response:
            data = ("Query not found", 404)

        new_data_size = True
        while new_data_size:
            response = next_scroll_query(es, sid, scroll_timeout)
            try:
                sid = response["_scroll_id"]
            except KeyError:
                pass
            try:
                new_data = [elem["_source"] for elem in response["hits"]["hits"]]
                new_data_size = len(new_data)
                # end of scrolling if new_data_size = 0
                data += new_data
            except KeyError:
                data = ("Query not found", 404)
                # print(response)
            except IndexError:
                data = ("Query not found", 404)
                # print(response)
            if isinstance(data, list) and not response:
                data = ("Query not found", 404)
        es.clear_scroll(scroll_id=sid)

    if not data:
        data = ("Query not found", 404)

    return data

def es_scroll(es, index, query, size=scroll_size, scroll_timeout=scroll_timeout):
    """
    When the query can return more object than the ES limit (10000)
    Handle the query with ES then perform error verification related to the response

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: number of responses to return
    :param scroll_timeout: duration of scroll instance between calls
    :return: list of dictionary on success or string error code
    """

    response_generator = es_helpers_scan(
        client=es,
        query=query,
        index=index,
        scroll=scroll_timeout,
        size=size
    )

    try:
        response = [x['_source'] for x in response_generator]
        if not response:
            return ("Query not found", 404)
        else:
            return response
    except:
        return ("Query not found", 404)


def es_get(es, index, id, **kwargs):
    """Query used to retrieve a document and its source or stored fields from a particular index

    :param es: elasticsearch client instance
    :param index: name of the index
    :param id: document id
    :param kwargs[arg]: optional parameters in the GET API of elasticsearch
        :arg    _source:            True or false to return the _source field or not,
                                    or a list of fields to return
        :arg    _source_excludes:   A list of fields to exclude from the
                                    returned _source field
        :arg    _source_includes:   A list of fields to extract and return
                                    from the _source field
        :arg    preference:         Specify the node or shard the operation should
                                    be performed on (default: random)
        :arg    realtime:           Specify whether to perform the operation in
                                    realtime or search mode
        :arg    refresh:            Refresh the shard containing the document before
                                    performing the operation
        :arg    routing:            Specific routing value
        :arg    stored_fields:      A comma-separated list of stored fields to
                                    return in the response
        :arg    version:            Explicit version number for concurrency control
        :arg    version_type:       Specific version type  Valid choices:
                                    internal, external, external_gte, force
    """

    optional_parameters = {
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "stored_fields",
        "version",
        "version_type",
    }

    try:
        if not kwargs:
            response = es.get(index=index, id=id)
        else:
            response = es.get(index=index, id=id, **kwargs)
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)
    
    return response['_source']


def if_yaml(mime_type, response):
    if mime_type == "application/yaml":
        response = make_response(yaml.dump(response), 200)
        response.mimetype = "application/yaml"
    return response
