import connexion
import six

from swagger_server.models.list_hchid import ListHchid  # noqa: E501
from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product1_list import Product1List  # noqa: E501
from swagger_server.models.product3 import Product3  # noqa: E501
from swagger_server.models.product3_classification_list import Product3ClassificationList  # noqa: E501
from swagger_server.models.product4 import Product4  # noqa: E501
from swagger_server.models.product4_list import Product4List  # noqa: E501
from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server.models.product6_list import Product6List  # noqa: E501
from swagger_server.models.product9_ages import Product9Ages  # noqa: E501
from swagger_server.models.product9_ages_list import Product9AgesList  # noqa: E501
from swagger_server.models.product9_prev import Product9Prev  # noqa: E501
from swagger_server.models.product9_prev_list import Product9PrevList  # noqa: E501
from swagger_server import util

import config
from controllers.query_controller import *


def associatedgene_all_orphacode():  # noqa: E501
    """Get all associatedgene

    Get the list of all clinical entity referenced in associatedgene # noqa: E501


    :rtype: Product6List
    """
    es = config.elastic_server

    index = "en_product6"

    query = "{\"query\": {\"match_all\": {}}}"

    response = multiple_res(es, index, query)
    return response


def associatedgene_list_orphacode():  # noqa: E501
    """List ORPHAcode for clinical entity associated gene

    Get the list of ORPHAcode usable to query clinical entity associated gene in selected language # noqa: E501


    :rtype: ListOrphacode
    """
    return 'do some magic!'


def associatedgene_orphacode(orphacode):  # noqa: E501
    """Disorder by ORPHAcode with associated genes

    Access every information related to a clinical entity by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int

    :rtype: Product6
    """
    es = config.elastic_server

    index = "en_product6"

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response


def epidemiology_all_orphacode(language):  # noqa: E501
    """Get all epidemiology in selected language

    Get the list of all clinical entity referenced in epidemiology for the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9PrevList
    """
    es = config.elastic_server

    index = "product9_prev"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"

    response = multiple_res(es, index, query)
    return response


def epidemiology_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with epidemiological data

    Access every information related to a clinical entity by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
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
    """List ORPHAcode for epidemiology in selected language

    Get the list of ORPHAcode usable to query epidemiology in selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'


def hierarchy_all_orphacode(hchid):  # noqa: E501
    """Get the full selected classification

    Get the list of all clinical entity referenced in orphaclassif for the selected classification # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: Product3ClassificationList
    """
    es = config.elastic_server

    index = "product3"
    index = "{}_{}".format(index, hchid)

    query = "{\"query\": {\"match_all\": {}}}"

    response = multiple_res(es, index, query)
    return response


def hierarchy_by_orphacode(orphacode):  # noqa: E501
    """Hierarchical classification of clinical entities by ORPHAcode in all classifications

    Query one clinical entity by its ORPHAcode and gives the list of occurences in Orphanet&#x27;s classifications with parents and childs clinical entity ORPHAcode number, the list of its children and parents. # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int

    :rtype: Product3ClassificationList
    """
    es = config.elastic_server

    index = "en_product3_*"

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = multiple_res(es, index, query)
    return response


def hierarchy_id_by_orphacode(orphacode, hchid):  # noqa: E501
    """Hierarchical classification of clinical entities by ORPHAcode in selected classification

    Query one clinical entity by its ORPHAcode and gives the list of parents and childs clinical entity in the selected Orphanet&#x27;s classification # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: Product3
    """
    es = config.elastic_server

    index = "en_product3_{}".format(hchid)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response


def hierarchy_list_hchid(hchid):  # noqa: E501
    """List hierarchical ID (hchid)

    Get the list of hierarchical ID (hchid) usable to select an Orphanet&#x27;s classification # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: ListHchid
    """
    return 'do some magic!'


def hierarchy_list_orphacode(hchid):  # noqa: E501
    """List ORPHAcode for selected classification

    Get the list of ORPHAcode usable to query the selected classification # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: ListOrphacode
    """
    return 'do some magic!'


def natural_history_all_orphacode(language):  # noqa: E501
    """Get all natural_history in selected language

    Get the list of all clinical entity referenced in natural_history for the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9AgesList
    """
    es = config.elastic_server

    index = "product9_ages"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"

    response = multiple_res(es, index, query)
    return response


def natural_history_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with age of onset

    Access every information related to a clinical entity by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
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
    """List ORPHAcode for natural history in selected language

    Get the list of ORPHAcode usable to query natural history of clinical entity in selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'


def phenotype_all_orphacode(language):  # noqa: E501
    """Get all phenotype in selected language

    Get the list of all clinical entity referenced in phenotype for the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4List
    """
    es = config.elastic_server

    index = "product4"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"

    response = multiple_res(es, index, query)
    return response


def phenotype_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with its associated phenotype

    Access every information related to a clinical entity by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4
    """
    es = config.elastic_server

    index = "product4"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"Disorder.ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response


def phenotype_list_orphacode(language):  # noqa: E501
    """List ORPHAcode for phenotype in selected language

    Get the list of ORPHAcode usable to query phenotype in selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'


def product1_all_orphacode(language):  # noqa: E501
    """Get all product 1 in selected language

    Get the list of all clinical entity referenced in product 1 for the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1List
    """
    es = config.elastic_server

    index = "product1"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match_all\": {}}}"

    response = multiple_res(es, index, query)
    return response


def product1_by_orphacode(orphacode, language):  # noqa: E501
    """clinical entity by ORPHAcode for product 1

    Access every information related to a clinical entity object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
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
    """List ORPHAcode for product 1 in selected language

    Get the list of ORPHAcode usable to query product 1 in selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'
