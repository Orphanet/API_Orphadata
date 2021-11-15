import elasticsearch.exceptions as es_exceptions
from flask import request

import config
import controllers.query_controller as qc


def products_description():  # noqa: E501
    """Get the organisation of all ORPHAcodes available for a selected classification.

    The result is a collection of ORPHAcodes organised as children and parents in the selected classification. # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a specific identifier attributed to an Orphanet classification.
    :type hchid: int

    :rtype: Product3ClassificationList
    """
    es = config.elastic_server

    index = "orphadata"

    query = {
        "query": {
            "match_all": {}
            },
        "_source": ["productId", "productName"]
        }

    size = config.scroll_size  # per scroll, not limiting
    response = qc.multiple_res(es, index, query, size)

    all_products = []
    for p in response:
        p_id_tmp = p['productId'].split('_')[1:]
        if p_id_tmp[-1] not in ['ages', 'prev']:
            p_id = p_id_tmp[0]
        else:
            p_id = '_'.join(p_id_tmp)
        p_lang = p['productId'].split('_')[0]

        if not all_products:
            dic = {
                # "Description": p['Description'],
                "productId": p_id,
                "productName": p['productName'],
                "languages": [p_lang]
            }
            all_products.append(dic)
        else:
            dic_in = [x for x in all_products if x["productId"]==p_id]
            if not dic_in:
                dic = {
                    # "Description": p['Description'],
                    "productId": p_id,
                    "productName": p['productName'],
                    "languages": [p_lang]
                }
                all_products.append(dic)
            else:
                if p_lang not in dic_in[0]["languages"]:
                    dic_in[0]["languages"].append(p_lang)

    return all_products


def generic_product1():
    es = config.elastic_server
    lang = request.args.get("lang", "en")


    index = "orphadata"
    doc_id = '{}_product1'.format(lang.lower())

    try:
        response = es.get(index=index, id=doc_id)
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)

    return response['_source']


def generic_product3():
    es = config.elastic_server

    index = "orphadata"
    doc_id = 'product3'.format()

    try:
        response = es.get(
            index=index,
            id=doc_id,
            _source_excludes=['items.clinicalEntities']
        )
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)

    return response['_source']


def generic_product4():
    es = config.elastic_server
    lang = request.args.get("lang", "en")


    index = "orphadata"
    doc_id = '{}_product4'.format(lang.lower())

    try:
        response = es.get(index=index, id=doc_id)
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)

    return response['_source']


def generic_product6():
    es = config.elastic_server

    index = "orphadata"
    doc_id = 'en_product6'

    try:
        response = es.get(index=index, id=doc_id)
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)

    return response['_source']


def generic_product7():
    es = config.elastic_server

    index = "orphadata"
    doc_id = 'en_product7'

    try:
        response = es.get(index=index, id=doc_id)
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)

    return response['_source']


def generic_product9_ages():
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "orphadata"
    doc_id = '{}_product9_ages'.format(lang.lower())

    try:
        response = es.get(index=index, id=doc_id)
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)

    return response['_source']


def generic_product9_prev():
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "orphadata"
    doc_id = '{}_product9_prev'.format(lang.lower())

    try:
        response = es.get(index=index, id=doc_id)
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)

    return response['_source']
