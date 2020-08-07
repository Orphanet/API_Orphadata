from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product1_list import Product1List  # noqa: E501

import config
from controllers.query_controller import *


def product1_all_orphacode(language):  # noqa: E501
    """Get all clinical entities informations and their cross-referencing in the selected language.

    The result is a collection of rare diseases informations including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1List
    """
    es = config.elastic_server

    index = "product1"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"

    size = 1000

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    return response


def product1_by_orphacode(orphacode, language):  # noqa: E501
    """Get informations and cross-referencing of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1
    """
    es = config.elastic_server

    index = "product1"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response


def product1_list_orphacode(language):  # noqa: E501
    """Get the list of ORPHAcodes available in the selected language.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    es = config.elastic_server

    index = "product1"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}, \"_source\":[\"ORPHAcode\"]}"

    size = 1000

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    if isinstance(response, str) or isinstance(response, tuple):
        pass
    else:
        response = [elem["ORPHAcode"] for elem in response]
    return response
