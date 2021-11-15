from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product4 import Product4  # noqa: E501
from swagger_server.models.product4_list import Product4List  # noqa: E501
from flask import request

import config
from controllers.query_controller import *


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

    response = uncapped_res(es, index, query, size, scroll_timeout)
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

    response = single_res(es, index, query)
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
        }
    }


    size = config.scroll_size  # per scroll, not limiting
    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    # response_parsed = [{"ORPHAcode": x["Disorder"]["ORPHAcode"], "PreferredTerm": x["Disorder"]["Preferred term"], "HPOs": x["Disorder"]["HPODisorderAssociation"]} for x in response]
    # response_parsed = []
    # for res in response:
    #     dic = {"ORPHAcode": res["Disorder"]["ORPHAcode"], "PreferredTerm": res["Disorder"]["Preferred term"]}
    #     dic["HPOs"] = sorted([ x["HPO"]["HPOId"] for x in res["Disorder"]["HPODisorderAssociation"] ])
    #     response_parsed.append(dic)

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

    index = "product4"
    index = "{}_{}".format(lang.lower(), index)

    query = "{\"query\": {\"match_all\": {}}, \"_source\":[\"Disorder.ORPHAcode\"]}"

    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    if isinstance(response, str) or isinstance(response, tuple):
        pass
    else:
        response = [elem["Disorder"]["ORPHAcode"] for elem in response]
    return response
