from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product1_list import Product1List  # noqa: E501

import config
from controllers import query_controller as qc
from flask import request



def product1_all_orphacode():  # noqa: E501
    """Get all clinical entities informations and their cross-referencing in the selected language.

    The result is a collection of rare diseases informations including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1List
    """
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product1"
    index = "{}_{}".format(lang.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"    

    size = config.scroll_size  # per scroll, not limiting
    scroll_timeout = config.scroll_timeout

    response = qc.uncapped_res(es, index, query, size, scroll_timeout)
    return response


def product1_by_orphacode(orphacode):  # noqa: E501
    """Get informations and cross-referencing of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1
    """
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product1"
    index = "{}_{}".format(lang.lower(), index)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = qc.single_res(es, index, query)
    return response


def product1_by_name(name):  # noqa: E501
    """Get informations and cross-referencing of a clinical entity searching by its name in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language. # noqa: E501

    :param name: The preferred name of a disease
    :type name: str
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1
    """
    # print(request.args)
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product1"
    index = "{}_{}".format(lang.lower(), index)

    query = {
        "query": {
            "match": {
                "Preferred term": str(name)
                }
            }
        }

    response = qc.single_res(es, index, query)
    return response


def product1_list_orphacode():  # noqa: E501
    """Get the list of ORPHAcodes available in the selected language.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product1"
    index = "{}_{}_args".format(lang.lower(), index)

    # query = "{\"query\": {\"match_all\": {}}, \"_source\":[\"ORPHAcode\"]}"

    query = {
        "query": {
            "match_all": {}
            },
            "_source": [
                "ORPHAcode",
                "Preferred term",
                "ExternalReference.Source"]
        }


    size = config.scroll_size  # per scroll, not limiting
    scroll_timeout = config.scroll_timeout

    response = qc.uncapped_res(es, index, query, size, scroll_timeout)
    return response
    # if isinstance(response, str) or isinstance(response, tuple):
    #     pass
    # else:
    #     response = [elem["ORPHAcode"] for elem in response]
    #     response.sort()
    # return response


def product1_by_omim(omim):
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product1"
    index = "{}_{}".format(lang.lower(), index)

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

    response = qc.multiple_res(es, index, query, 2000)
    return response


def product1_list_icds():  # noqa: E501
    """Get the list of ICD-10 available in the selected language.

    The result is a collection of ICD-10 references in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product1"
    index = "{}_{}".format(lang.lower(), index)

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


    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = qc.uncapped_res(es, index, query, size, scroll_timeout)
    response_parsed = []
    for res in response:
        for ele in res["ExternalReference"]:
            if ele["Source"] == 'ICD-10':
                response_parsed.append(ele["Reference"])
    
    return sorted(list(set(response_parsed)))


def product1_by_icd(icd):
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product1"
    index = "{}_{}".format(lang.lower(), index)

    # query = {
    #     "query": {
    #         "nested": {
    #             "path": 'ExternalReference',
    #             "query": {
    #                 "bool": {
    #                     "must": {
    #                         "match": {"ExternalReference.Source": "ICD-10"}
    #                     },
    #                     'must': {
    #                         "match": {"ExternalReference.Reference": '{}'.format(icd)}
    #                     }
    #                 }
    #             }
    #         }
    #     },
    #     "_source": ['ExternalReference.Source','ExternalReference.Reference']
    # }

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
        "_source": ['ExternalReference.Source','ExternalReference.Reference']
    }    

    response = qc.multiple_res(es=es, index=index, query=query, size=2000)
    return response


    # query = {
    #     "query": {
    #         "nested": {
    #             "path": 'ExternalReference',
    #             "query": {
    #                 "bool": {
    #                     "must": {
    #                         "match": {"ExternalReference.Source": "ICD-10"}
    #                     },
    #                     'must': {
    #                         "wildcard": {
    #                             "ExternalReference.Reference": {
    #                                 'value': '{}'.format(icd),
    #                                 'boost': 1.0
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     },
    #     "_source": ['ExternalReference.Source','ExternalReference.Reference']
    # }
