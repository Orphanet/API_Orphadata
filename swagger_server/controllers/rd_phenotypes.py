from flask import request
import elasticsearch.exceptions as es_exceptions

import config
import controllers.query_controller as qc


def phenotype_all_orphacode():  # noqa: E501
    """Get all clinical entities with their associated phenotypes in the selected language.

    The result is a collection of clinical entities with their associated HPO phenotypes characterized by frequency (obligate, very frequent, frequent, occasional, very rare or excluded) and whether the annotated HPO term is a major diagnostic criterion or a pathognomonic sign of the rare disease. Source (PMID references), the date and the validation’s status of the association between the rare disease and HPO terms is also available. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4List
    """
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product4"
    index = "{}_{}".format(lang.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"

    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = qc.uncapped_res(es, index, query, size, scroll_timeout)
    return response


def phenotype_by_orphacode(orphacode):  # noqa: E501
    """Get informations and associated HPO phenotypes of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, the group and type, and the associated HPO phenotypes. The annotation is characterized by frequency (obligate, very frequent, frequent, occasional, very rare or excluded) and whether the annotated HPO term is a major diagnostic criterion or a pathognomonic sign of the rare disease. Source (PMID references), the date and the validation’s status of the association between the rare disease and HPO terms is also made available. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4
    """
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product4"
    index = "{}_{}".format(lang.lower(), index)

    query = "{\"query\": {\"match\": {\"Disorder.ORPHAcode\": " + str(orphacode) + "}}}"

    response = qc.single_res(es, index, query)
    return response

def phenotype_by_hpo_id(hpoids):
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "product4"
    index = "{}_{}".format(lang.lower(), index)

    # query = {
    #     "query":{
    #         "match": {
    #             "Disorder.HPODisorderAssociation.HPO.HPOId": str(hpoids)
    #         }
    #     },
    #     '_source': {
    #         'includes': ["Disorder"],
    #         'excludes': [
    #             "Disorder.HPO*",
    #             "Disorder.Typolo*",
    #             "Disorder.Dis*",
    #             "Disorder.OrphanetURL",
    #             ]
    #     }
    # }

    # query = {
    #     "query":{
    #         "constant_score": {
    #             "filter": {
    #                 "match": {
    #                     "Disorder.HPODisorderAssociation.HPO.HPOId": str(hpoids)
    #                 }
    #             }
    #         }
    #     },
    #     '_source': {
    #         'includes': ["Disorder"],
    #         'excludes': [
    #             "Disorder.HPO*",
    #             "Disorder.Typolo*",
    #             "Disorder.Dis*",
    #             "Disorder.OrphanetURL",
    #             ]
    #     }
    # }
    # hpoids = ['HP:0001249', 'HP:0001257', 'HP:0001250']

    # filter = []
    # for hpo_id in hpoids:
    #     filter.append(
    #         {
    #             "match": {
    #                 "Disorder.HPODisorderAssociation.HPO.HPOId": str(hpo_id) 
    #             }
    #         }
    #     )


    # query = {
    #     "query": {
    #         "bool": {
    #             "filter": {
    #                 "terms": {
    #                     "Disorder.HPODisorderAssociation.HPO.HPOId.keyword": hpoids,
    #                     "operator": "AND"
    #                 }
    #             }
    #         }
    #     }
    # }

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

    # response = qc.uncapped_res(es, index, query, size=config.scroll_size, scroll_timeout=config.scroll_timeout)
    response = qc.es_scroll(es, index, query)

    return response


def phenotype_list_orphacode():  # noqa: E501
    """Get list of ORPHAcodes associated to HPO phenotypes in the selected language.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    es = config.elastic_server
    lang = request.args.get("lang", "en")

    index = "orphadata"
    doc_id = '{}_product4'.format(lang.lower())

    query = {
        'query': {
            'bool': {
                'filter': {
                    'term': {
                        "productId.keyword": {
                            'value': 'en_product4'
                        }
                    }

                }
            }
        },
        '_source': ['items.ORPHAcode', 'items.PreferredTerm']
    }

    size = config.scroll_size  # per scroll, not limiting
    scroll_timeout = config.scroll_timeout

    try:
        # response = es.get(index=index, id=doc_id)
        response = qc.uncapped_res(es, index, query, size, scroll_timeout)
    except es_exceptions.NotFoundError:
        return ("Server Error: Index not found", 404)
        # print(response)
    except es_exceptions.ConnectionError:
        return ("Elasticsearch node unavailable", 503)
    except es_exceptions.TransportError:
        return ("Elasticsearch node unavailable", 503)

    return response[0]



# es = config.elastic_server
# lang = "en"

# index = "product4"
# index = "{}_{}".format(lang.lower(), index)

# hpoids = ['HP:0000137']

# query = {
#     "query": {
#         "match": {
#             "Disorder.HPODisorderAssociation.HPO.HPOId": {
#                 "query": ' '.join(hpoids),
#                 "operator": "AND"
#             }
#         }
#     }
# }

# from elasticsearch.helpers import scan as es_helpers_scan

# response = [x['_source'] for x in es_helpers_scan(es, query=query, index=index)]


# for ele in response:
#     print(ele['Disorder']['ORPHAcode'])