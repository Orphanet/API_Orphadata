from flask import request, current_app

import api.controllers.query_controller as qc
from api.controllers.response_handler import ResponseWrapper
from api.controllers import PRODUCTS


PRODUCT = PRODUCTS.get('product9_prev')
index_base = "orphadata_{}_product9_prev"


def query_epidemiology_base():  # noqa: E501
    """Get all clinical entities with their epidemiological dataset in the selected language.

    The result is a collection of clinical entities (ORPhacode, preferred term, expertlink) and associated epidemiological data characterized as point prevalence, birth prevalence, lifelong prevalence and incidence, or the number of cases/families reported together with their respective intervals per geographical area (country, continent) and translated in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9PrevList
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "match_all": {}
        },
        # '_source': 'ORPHAcode'
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_epidemiology_orphacodes():
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = 'orphadata_{}_product9_prev'.format(lang.lower())

    query = {
        "query": {
            "match_all": {}
        },
        '_source': ['ORPHAcode', 'Preferred term']
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_epidemiology_by_orphacode(orphacode):  # noqa: E501
    """Get epideliological informations of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, the group and type, and the associated point prevalence, birth prevalence, lifelong prevalence and incidence, or the number of cases/families reported together with their respective intervals per geographical area (country, continent) when exist. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9Prev
    """
    
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    request.args.params = {'ORPHAcode': orphacode}

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "match": {
                "ORPHAcode": str(orphacode)
            }
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.single_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()