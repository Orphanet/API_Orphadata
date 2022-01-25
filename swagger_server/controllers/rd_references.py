import elasticsearch.exceptions as es_exceptions
from flask import request

from swagger_server import config
from swagger_server.controllers import query_controller as qc
from swagger_server.controllers.response_handler import ResponseWrapper


PRODUCT = config.PRODUCTS.get('product1')

es_client = config.elastic_server
index_base = "product1"


def query_references_base():  # noqa: E501
    """Get all clinical entities informations and their cross-referencing in the selected language.

    The result is a collection of rare diseases informations including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1List
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = "{}_{}".format(lang.lower(), index_base)

    query = {
        'query': {
            'match_all': {}
        }
    }

    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_references_orphacodes():  # noqa: E501
    """Get the list of ORPHAcodes available in the selected language.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = "orphadata"

    query = {
        'query': {
            'bool': {
                'filter': {
                    'term': {
                        "productId.keyword": {
                            'value': '{}_{}'.format(lang.lower(), index_base)
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


def query_references_by_orphacode(orphacode):  # noqa: E501
    """Get informations and cross-referencing of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1
    """
    request.args.params = {'ORPHAcode': orphacode}

    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = "{}_{}".format(lang.lower(), index_base)

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


def query_references_by_name(name):  # noqa: E501
    """Get informations and cross-referencing of a clinical entity searching by its name in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language. # noqa: E501

    :param name: The preferred name of a disease
    :type name: str
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1
    """
    request.args.params = {'name': name}

    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = "{}_{}".format(lang.lower(), index_base)

    query = {
        "query": {
            "match": {
                "Preferred term": str(name)
                }
            }
        }

    response = qc.single_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_references_by_omim(omim):
    request.args.params = {'omim': omim}
    
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = "{}_{}".format(lang.lower(), index_base)

    query = {
        "query": {
            "nested": {
                "path": 'ExternalReference',
                "query": {
                    "bool": {
                        "must": [
                        {
                            "match": {"ExternalReference.Source": "OMIM"}
                        },
                        {
                            "match": {"ExternalReference.Reference": str(omim)}
                        }
                        ]
                    }
                }
            }
        }
    }

    response = qc.multiple_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_references_icds():  # noqa: E501
    """Get the list of ICD-10 available in the selected language.

    The result is a collection of ICD-10 references in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = "{}_{}".format(lang.lower(), index_base)

    query = {
        "query": {
            "nested": {
                "path": 'ExternalReference',
                "query": {
                    "bool": {
                        "must": {
                            "match": {"ExternalReference.Source": "ICD-10"}
                        },
                        'should': {
                            "regexp": {
                                "ExternalReference.Reference": {
                                    'value': '*',
                                }
                            }
                        }
                    }
                }
            }
        },
        "_source": ['ExternalReference.Source','ExternalReference.Reference']
    }

    response = qc.es_scroll(es_client, index, query)

    if not isinstance(response, tuple):      
        response_parsed = []
        for res in response:
            for ele in res["ExternalReference"]:
                if ele["Source"] == 'ICD-10':
                    response_parsed.append(ele["Reference"])
    else:
        response_parsed = response

    wrapped_response = ResponseWrapper(ctl_response=sorted(list(set(response_parsed))), request=request, product=PRODUCT)

    return wrapped_response.get()    


def query_references_by_icd(icd):
    request.args.params = {'icd': icd}
    
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = "{}_{}".format(lang.lower(), index_base)

    query = {
        "query": {
            "nested": {
                "path": 'ExternalReference',
                "query": {
                    "bool": {
                        "must": {
                            "match": {"ExternalReference.Source": "ICD-10"}
                        },
                        'filter': {
                            "regexp": {
                                "ExternalReference.Reference": {
                                    'value': '{}'.format(str(icd)),
                                    "flags": "ALL",
                                    "case_insensitive": True,
                                }
                            }
                        }
                    }
                }
            }
        },
        # "_source": ['ExternalReference.Source','ExternalReference.Reference']
    }    

    response = qc.multiple_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()