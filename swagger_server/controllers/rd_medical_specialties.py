import elasticsearch.exceptions as es_exceptions
from flask import request

from swagger_server import config
import swagger_server.controllers.query_controller as qc
from swagger_server.controllers.response_handler import ResponseWrapper


PRODUCT = config.PRODUCTS.get('product7')

es_client = config.elastic_server
index = "en_product7"


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
        # "_source": ["ORPHAcode"]
    }

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

    response = qc.multiple_res(es_client, index, query)

    if not isinstance(response, tuple):      
        response_parsed = []
        for hit in response:
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

    response = qc.multiple_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()
