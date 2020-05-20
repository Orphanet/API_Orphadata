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


def init_scroll_query(es, index, query, size, scroll_timeout):
    """
    Init a scrollable ES query and handle a first layer of error

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: optional number of responses to return
    :param scroll_timeout: duration of scroll instance between calls
    :return: elasticsearch response object on success or error string
    """
    try:
        response = es.search(index=index, body=query, size=size, scroll=scroll_timeout)
        # print(response)
    except elasticsearch.exceptions.NotFoundError:
        response = ("Server Error: Index not found", 404)
        # print(response)
    except elasticsearch.exceptions.ConnectionError:
        response = ("Elasticsearch node unavailable", 503)
    return response


def next_scroll_query(es, sid, scroll_timeout):
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


def multiple_res(es, index, query, size):
    """
    When the query can return a reasonable (N << 10000) number of object (ES limit = 10000)
    Handle the query with ES then perform error verification related to the response

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :param size: number of responses to return
    :return: list of dictionary on success or string error code
    """
    response = handle_query(es, index, query, size=size)
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


def uncapped_res(es, index, query, size, scroll_timeout):
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
    response = init_scroll_query(es, index, query, size, scroll_timeout)
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
        es.clear_scroll(scroll_id=sid)
    return data
