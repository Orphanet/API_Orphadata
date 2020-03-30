import elasticsearch


def handle_query(es, index, query):
    """
    Fetch the ES query and handle a first layer of error

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :return: elasticsearch response object on success or error string
    """
    try:
        response = es.search(index=index, body=query)
        # print(response)
    except elasticsearch.exceptions.NotFoundError:
        response = "Server Error: Index not found"
        print(response)
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
    if isinstance(response, str):
        pass
    else:
        try:
            response = response["hits"]["hits"][0]["_source"]
        except KeyError:
            response = "404"
            print(response)
        except IndexError:
            response = "404"
            print(response)
    return response


def multiple_res(es, index, query):
    """
    When the query can return multiple object
    Handle the query with ES then perform error verification related to the response

    :param es: elasticsearch instance see elasticsearch module
    :param index: elasticsearch index name (handle wildcard)
    :param query: elasticsearch valid query
    :return: list of dictionary on success or string error code
    """
    response = handle_query(es, index, query)
    if isinstance(response, str):
        pass
    else:
        try:
            response = [elem["_source"] for elem in response["hits"]["hits"]]
        except KeyError:
            response = "404"
            print(response)
        except IndexError:
            response = "404"
            print(response)
    return response
