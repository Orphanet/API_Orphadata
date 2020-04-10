import elasticsearch


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
    except elasticsearch.exceptions.NotFoundError:
        response = ("Server Error: Index not found", 404)
        # print(response)
    except elasticsearch.exceptions.ConnectionError:
        response = ("Elasticsearch node unavailable", 503)
    return response


def handle_scroll_query(es, index, query):
    """
    Fetch a scrollable ES query and handle a first layer of error

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: optional number of responses to return
    :return: elasticsearch response object on success or error string
    """
    try:
        response = es.search(index=index, body=query, size=1000)
        # print(response)
    except elasticsearch.exceptions.NotFoundError:
        response = ("Server Error: Index not found", 404)
        # print(response)
    except elasticsearch.exceptions.ConnectionError:
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
    if isinstance(response, tuple):
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


def multiple_res(es, index, query, size):
    """
    When the query can return multiple object
    Handle the query with ES then perform error verification related to the response

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: number of responses to return
    :return: list of dictionary on success or string error code
    """
    response = handle_query(es, index, query, size=size)
    if isinstance(response, str):
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
    return response


def uncapped_res(es, index, query):
    """
    When the query can return more object than the ES limit (10000)
    Handle the query with ES then perform error verification related to the response

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: number of responses to return
    :return: list of dictionary on success or string error code
    """
    response = handle_scroll_query(es, index, query)
    if isinstance(response, str):
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
    return response
