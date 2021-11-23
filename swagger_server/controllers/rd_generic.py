import elasticsearch.exceptions as es_exceptions
from flask import request

from swagger_server import config
import swagger_server.controllers.query_controller as qc
from swagger_server.controllers.response_handler import ResponseWrapper


es_client = config.elastic_server
index = "orphadata"


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

    response = qc.multiple_res(es, index, query)

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
    lang = request.args.get("lang", "en")

    doc_id = '{}_product1'.format(lang.lower())

    response = qc.es_get(es=es_client, index=index, id=doc_id)
    wrapped_response = ResponseWrapper(ctl_response=response['items'], request=request, product=config.PRODUCTS.get('product1'))

    return wrapped_response.get()


def generic_product3():
    doc_id = 'product3'.format()

    response = qc.es_get(es=es_client, index=index, id=doc_id)
    wrapped_response = ResponseWrapper(ctl_response=response['items'], request=request, product=config.PRODUCTS.get('product3'))

    return wrapped_response.get()


def generic_product4():
    doc_id = 'en_product4'.format()

    response = qc.es_get(es=es_client, index=index, id=doc_id)
    wrapped_response = ResponseWrapper(ctl_response=response['items'], request=request, product=config.PRODUCTS.get('product4'))

    return wrapped_response.get()


def generic_product6():
    doc_id = 'en_product6'.format()

    response = qc.es_get(es=es_client, index=index, id=doc_id)
    wrapped_response = ResponseWrapper(ctl_response=response['items'], request=request, product=config.PRODUCTS.get('product6'))

    return wrapped_response.get()


def generic_product7():
    doc_id = 'en_product7'.format()

    response = qc.es_get(es=es_client, index=index, id=doc_id)
    wrapped_response = ResponseWrapper(ctl_response=response['items'], request=request, product=config.PRODUCTS.get('product7'))

    return wrapped_response.get()


def generic_product9_ages():
    doc_id = 'en_product9_ages'.format()

    response = qc.es_get(es=es_client, index=index, id=doc_id)
    wrapped_response = ResponseWrapper(ctl_response=response['items'], request=request, product=config.PRODUCTS.get('product9_ages'))

    return wrapped_response.get()


def generic_product9_prev():
    doc_id = 'en_product9_prev'.format()

    response = qc.es_get(es=es_client, index=index, id=doc_id)
    wrapped_response = ResponseWrapper(ctl_response=response['items'], request=request, product=config.PRODUCTS.get('product9_prev'))

    return wrapped_response.get()
