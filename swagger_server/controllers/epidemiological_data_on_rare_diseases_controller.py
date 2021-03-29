from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product9_ages import Product9Ages  # noqa: E501
from swagger_server.models.product9_ages_list import Product9AgesList  # noqa: E501
from swagger_server.models.product9_prev import Product9Prev  # noqa: E501
from swagger_server.models.product9_prev_list import Product9PrevList  # noqa: E501

import config
from controllers.query_controller import *


def epidemiology_all_orphacode(language):  # noqa: E501
    """Get all clinical entities with their epidemiological dataset in the selected language.

    The result is a collection of clinical entities (ORPhacode, preferred term, expertlink) and associated epidemiological data characterized as point prevalence, birth prevalence, lifelong prevalence and incidence, or the number of cases/families reported together with their respective intervals per geographical area (country, continent) and translated in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9PrevList
    """
    es = config.elastic_server

    index = "product9_prev"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"

    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    return response


def epidemiology_by_orphacode(orphacode, language):  # noqa: E501
    """Get epideliological informations of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, the group and type, and the associated point prevalence, birth prevalence, lifelong prevalence and incidence, or the number of cases/families reported together with their respective intervals per geographical area (country, continent) when exist. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9Prev
    """
    es = config.elastic_server

    index = "product9_prev"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response


def epidemiology_list_orphacode(language):  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one epidemiological data.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    es = config.elastic_server

    index = "product9_prev"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}, \"_source\":[\"ORPHAcode\"]}"

    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    if isinstance(response, str) or isinstance(response, tuple):
        pass
    else:
        response = [elem["ORPHAcode"] for elem in response]
    return response


def natural_history_all_orphacode(language):  # noqa: E501
    """Get all clinical entities with their natural history data in the selected language.

    The result is a collection of clinical entities (ORPhacode, preferred term, expertlink) and associated natural history data characterized by informations on inheritance, interval average age of onset and interval average age of death. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9AgesList
    """
    es = config.elastic_server

    index = "product9_ages"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"

    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    return response


def natural_history_by_orphacode(orphacode, language):  # noqa: E501
    """Get natural history informations of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, the group and type, and the associated inheritance, age of onset and age of death when exist. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9Ages
    """
    es = config.elastic_server

    index = "product9_ages"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response


def natural_history_list_orphacode(language):  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one natural history data.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    es = config.elastic_server

    index = "product9_ages"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}, \"_source\":[\"ORPHAcode\"]}"

    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    if isinstance(response, str) or isinstance(response, tuple):
        pass
    else:
        response = [elem["ORPHAcode"] for elem in response]
    return response
