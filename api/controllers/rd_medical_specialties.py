import elasticsearch.exceptions as es_exceptions
from flask import request, current_app

import api.controllers.query_controller as qc
from api.controllers.response_handler import ResponseWrapper
from api.controllers import PRODUCTS


PRODUCT = PRODUCTS.get('product7')
index = "orphadata_en_product7"


def query_linearization_base():
    """Get medical specialties associated with all ORPHAcodes

    The result is a collection of information relative to all ORPHAcodes and their medical specialy.
    """
    query = {
        'query': {
            'match_all': {}
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()



def query_linearization_orphacodes():
    """Get all orphacodes for product 7
    """
    query = {
        "query": {
            "match_all": {}
        },
        "_source": ["ORPHAcode", "Preferred term"]
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)

    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_linearization_by_orphacode(orphacode):  # noqa: E501
    """Get associated genes and genes information of a clinical entity searching by its ORPHAcode.

    The result is a set of data includes ORPhacode, preferred term, expertlink, group and type of the selected clinical entity, relationship between genes and the searched disease and symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases of selected genes. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int

    :rtype: Product6
    """
    request.args.params = {'ORPHAcode': orphacode}

    query = {
        "query": {
            "term": {
                "ORPHAcode": int(orphacode)
            }
        },
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.single_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_linearization_parents():

    query = {
        "query": {
            "match_all": {}
        },
        "_source": ["DisorderDisorderAssociation.TargetDisorder"]
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)

    if not isinstance(response, tuple):      
        response_parsed = []
        for hit in response:
            if not hit:
                continue
            parent = {
                "ORPHAcode": hit["DisorderDisorderAssociation"][0]["TargetDisorder"]["ORPHAcode"],
                "Preferred term": hit["DisorderDisorderAssociation"][0]["TargetDisorder"]["Preferred term"]
                }
            if parent not in response_parsed:
                response_parsed.append(parent)
    else:
        response_parsed = response

    wrapped_response = ResponseWrapper(ctl_response=sorted(response_parsed, key=lambda x: x["ORPHAcode"]), request=request, product=PRODUCT)

    return wrapped_response.get()
    

def query_linearization_by_parent(parentcode):  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one gene.

    The result is a collection of ORPHAcodes associated to at least one gene. # noqa: E501

    """
    request.args.params = {'ORPHAcode': parentcode}

    query = {
        "query": {
            "term": {
                "DisorderDisorderAssociation.TargetDisorder.ORPHAcode": int(parentcode)
            }
        },
        # "_source": ["ORPHAcode"]
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()
