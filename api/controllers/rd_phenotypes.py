import elasticsearch.exceptions as es_exceptions
from flask import request

from api.controllers import query_controller as qc
from api.controllers.response_handler import ResponseWrapper
from api.controllers import PRODUCTS, es_client


PRODUCT = PRODUCTS.get('product4')
index_base = "orphadata_{}_product4"


def query_phenotypes_base():  # noqa: E501
    """Get all clinical entities with their associated phenotypes in the selected language.

    The result is a collection of clinical entities with their associated HPO phenotypes characterized by frequency (obligate, very frequent, frequent, occasional, very rare or excluded) and whether the annotated HPO term is a major diagnostic criterion or a pathognomonic sign of the rare disease. Source (PMID references), the date and the validation’s status of the association between the rare disease and HPO terms is also available. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4List
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    query = {
        'query': {
            'match_all': {}
        }
    }

    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_phenotypes_orphacodes_old():  # noqa: E501
    """Get list of ORPHAcodes associated to HPO phenotypes in the selected language.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = "orphadata_generic"

    query = {
        'query': {
            'bool': {
                'filter': {
                    'term': {
                        "productId.keyword": {
                            'value': index_base.format(lang.lower()).replace("orphadata_", '')
                        }
                    }

                }
            }
        },
        '_source': ['items.ORPHAcode', 'items.PreferredTerm']
    }

    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response[0]['items'], request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_phenotypes_orphacodes():
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "match_all": {}
        },
        '_source': ['Disorder.ORPHAcode', 'Disorder.Preferred term']
    }

    response = qc.es_scroll(es_client, index, query)

    parsed_response = []
    for hit in response:
        parsed_response.append(hit.pop('Disorder'))

    wrapped_response = ResponseWrapper(ctl_response=parsed_response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_phenotypes_by_orphacode(orphacode):  # noqa: E501
    """Get informations and associated HPO phenotypes of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, the group and type, and the associated HPO phenotypes. The annotation is characterized by frequency (obligate, very frequent, frequent, occasional, very rare or excluded) and whether the annotated HPO term is a major diagnostic criterion or a pathognomonic sign of the rare disease. Source (PMID references), the date and the validation’s status of the association between the rare disease and HPO terms is also made available. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4
    """
    request.args.params = {'ORPHAcode': orphacode}

    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "term": {
                "Disorder.ORPHAcode": int(orphacode)
            }
        },
        # "_source": ["ORPHAcode"]
    }

    response = qc.single_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_phenotypes_by_hpoids(hpoids):
    """
    hpoids = ['HP:0000768', 'HP:0001065', 'HP:0001166', 'HP:0001763']
    HP:0000768,HP:0001065,HP:0001166,HP:0001763
    """
    request.args.params = {'hpoids': hpoids}

    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "match": {
                "Disorder.HPODisorderAssociation.HPO.HPOId": {
                    "query": ' '.join(hpoids),
                    "operator": "AND"
                }
            }
        },
        # '_source': ['Disorder.ORPHAcode']
    }

    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()