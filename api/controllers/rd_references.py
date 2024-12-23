import elasticsearch.exceptions as es_exceptions
from flask import request, current_app
import json

from api.controllers import query_controller as qc
from api.controllers.response_handler import ResponseWrapper
from api.controllers import PRODUCTS
from api.util import build_query_elements


PRODUCT = PRODUCTS.get('product1')
index_base = "orphadata_{}_product1"


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

    index = index_base.format(lang.lower())

    query = {
        'query': {
            'match_all': {}
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_references_orphacodes():
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

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

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "term": {
                "ORPHAcode": int(orphacode)
            }
        },
        # "_source": ["ORPHAcode"]
    }

    es_client = current_app.config.get('ES_NODE')
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

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "match": {
                "Preferred term": str(name)
                }
            }
        }

    es_client = current_app.config.get('ES_NODE')
    response = qc.single_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_references_omims():  # noqa: E501
    """Get the list of OMIMs available in the selected language.

    The result is a collection of OMIM references in the selected language. 
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "nested": {
                "path": 'ExternalReference',
                "query": {
                    "bool": {
                        "must": {
                            "match": {"ExternalReference.Source": "OMIM"}
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

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)

    if not isinstance(response, tuple):      
        response_parsed = []
        for res in response:
            for ele in res["ExternalReference"]:
                if ele["Source"] == 'OMIM':
                    response_parsed.append(ele["Reference"])
        wrapped_response = ResponseWrapper(ctl_response=sorted(list(set(response_parsed))), request=request, product=PRODUCT)
    else:
        wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()    


def query_references_by_omim(omim):
    request.args.params = {'omim': omim}
    
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

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

    es_client = current_app.config.get('ES_NODE')
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

    index = index_base.format(lang.lower())

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

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)

    if not isinstance(response, tuple):      
        response_parsed = []
        for res in response:
            for ele in res["ExternalReference"]:
                if ele["Source"] == 'ICD-10':
                    response_parsed.append(ele["Reference"])
        wrapped_response = ResponseWrapper(ctl_response=sorted(list(set(response_parsed))), request=request, product=PRODUCT)
    else:
        wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()    


def query_references_by_icd(icd):
    request.args.params = {'icd': icd}
    
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    # query = {
    #     "query": {
    #         "nested": {
    #             "path": 'ExternalReference',
    #             "query": {
    #                 "bool": {
    #                     "must": {
    #                         "match": {"ExternalReference.Source": "ICD-10"}
    #                     },
    #                     'filter': {
    #                         "regexp": {
    #                             "ExternalReference.Reference.keyword": {
    #                                 'value': '{}'.format(str(icd).upper()),
    #                                 "flags": "ALL",
    #                                 "case_insensitive": True,
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }

    query = {
        "query": {
            "nested": {
                "path": 'ExternalReference',
                "query": {
                    "bool": {
                        "must": [
                            {
                                "match": {"ExternalReference.Source": "ICD-10"}
                            },
                            {
                                'query_string': {
                                    "default_field": "ExternalReference.Reference.keyword",
                                    "query": '{}'.format(str(icd).upper())            
                                }
                            }
                        ]
                    }
                }
            }
        }
    }    

    es_client = current_app.config.get('ES_NODE')
    response = qc.multiple_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_references_icd11s():  # noqa: E501
    """Get the list of ICD-11 available in the selected language.

    The result is a collection of ICD-11 references in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "nested": {
                "path": 'ExternalReference',
                "query": {
                    "bool": {
                        "must": {
                            "match": {"ExternalReference.Source": "ICD-11"}
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

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)

    if not isinstance(response, tuple):      
        response_parsed = []
        for res in response:
            for ele in res["ExternalReference"]:
                if ele["Source"] == 'ICD-11':
                    response_parsed.append(ele["Reference"])
        wrapped_response = ResponseWrapper(ctl_response=sorted(list(set(response_parsed))), request=request, product=PRODUCT)
    else:
        wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()    


def query_references_by_icd11(icd):
    request.args.params = {'icd': icd}
    
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    index = index_base.format(lang.lower())

    query = {
        "query": {
            "nested": {
                "path": 'ExternalReference',
                "query": {
                    "bool": {
                        "must": [
                            {
                                "match": {"ExternalReference.Source": "ICD-11"}
                            },
                            {
                                'query_string': {
                                    "default_field": "ExternalReference.Reference.keyword",
                                    "query": '{}'.format(str(icd).upper())            
                                }
                            }
                        ]
                    }
                }
            }
        }
    }    

    es_client = current_app.config.get('ES_NODE')
    response = qc.multiple_res(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


def query_references_by_multiple_fields():  # noqa: E501
    """Get information and cross-referencing of clinical entities searching by multiple fields in the selected language.

    Allowed fields are:
        - Disorder name, definition and synonyms
        - Nomenclature type
        - Code relative to the nomenclature
        - Type of mapping between the nomenclature and disorder

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    lang = request.args.get("lang", "en")
    if PRODUCT['lang'] != lang.lower():
        PRODUCT['lang'] = lang.lower()

    query_elements = build_query_elements(args=request.args)
    query = {        
        "query": {
            "bool": {
                "must": query_elements
            }
        }
    }
    # print(json.dumps(query, indent=2))

    index = index_base.format(lang.lower())

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)

    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)

    return wrapped_response.get()


