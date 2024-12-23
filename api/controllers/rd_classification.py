import elasticsearch.exceptions as es_exceptions
from flask import request, current_app

import api.controllers.query_controller as qc
from api.controllers.response_handler import ResponseWrapper
from api.controllers import PRODUCTS


PRODUCT = PRODUCTS.get('product3')
index_base = "orphadata_en_product3_{}"


def query_classification_base():  # noqa: E501
    """Get all clinical entities information for all hierarchical classification.

    """

    index = index_base.format("*")

    query = {
        'query': {
            'match_all': {}
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()



def query_classification_orphacodes():

    index = index_base.format("*")

    query = {
        "query": {
            "match_all": {}
        },
        "_source": ["ORPHAcode", "preferredTerm"]
}

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)

    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_classification_by_hchid(hchid):  # noqa: E501
    """Get the organisation of all ORPHAcodes available for a selected classification.

    The result is a collection of ORPHAcodes organised as children and parents in the selected classification. # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a specific identifier attributed to an Orphanet classification.
    :type hchid: int
    """
    request.args.params = {'hchID': hchid}

    index = index_base.format(hchid)

    query = {
        'query': {
            'match_all': {}
        }
    }

    es_client = current_app.config.get('ES_NODE')
    # response = qc.multiple_res(es_client, index, query)
    response = qc.es_scroll(es=es_client, index=index, query=query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_classification_hchids_by_orphacode(orphacode):  # noqa: E501
    """Hierarchical classification of clinical entities by ORPHAcode in all classifications

    Query one clinical entity by its ORPHAcode and gives the list of occurences in Orphanet&#x27;s classifications with parents and childs clinical entity ORPHAcode number, the list of its children and parents. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int

    :rtype: Product3ClassificationList
    """
    request.args.params = {'ORPHAcode': orphacode}

    index = index_base.format('*')

    query = {
        "query": {
            "match": {"ORPHAcode": str(orphacode)}
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.multiple_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_classification_by_orphacode_and_hchid(orphacode, hchid):  # noqa: E501
    """Hierarchical classification of clinical entities by ORPHAcode in selected classification

    Query one clinical entity by its ORPHAcode and gives the list of parents and childs clinical entity in the selected Orphanet&#x27;s classification # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param hchid: The hierarchy ID (hchID) is a specific identifier attributed to an Orphanet classification.
    :type hchid: int

    :rtype: Product3
    """
    request.args.params = {'ORPHAcode': orphacode, 'hchID': hchid}

    index = index_base.format(hchid)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    es_client = current_app.config.get('ES_NODE')
    response = qc.single_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()
    

def query_classification_hchids():
    index = "orphadata_en_product3"

    query = {
        'query': {
            'match_all': {}
        },
        '_source': {
            'includes': ['hchId', 'hchTag'],
        },
    }
    es_client = current_app.config.get('ES_NODE')
    response = qc.multiple_res(es=es_client, index=index, query=query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_classification_orphacodes_by_hchid(hchid):  # noqa: E501
    """Get the list of ORPHAcodes available for a selected classification.

    The result is a collection of ORPHAcodes present in the selected classification. # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a specific identifier attributed to an Orphanet classification.
    :type hchid: int

    :rtype: ListOrphacode
    """
    request.args.params = {'hchID': hchid}

    index = index_base.format(hchid)

    query = {
        "query": {
            "match_all": {}
        },
        "_source":["ORPHAcode", "preferredTerm"]
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.uncapped_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()
