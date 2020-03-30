import connexion
import six

import config
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product3_classification import Product3Classification  # noqa: E501
from swagger_server.models.product3_classification_list import Product3ClassificationList  # noqa: E501
from swagger_server.models.product4_hpo import Product4HPO  # noqa: E501
from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server.models.product9_ages import Product9Ages  # noqa: E501
from swagger_server.models.product9_prev import Product9Prev  # noqa: E501
from swagger_server import util

from controllers.query_handlers import *


def age_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with age of onset

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

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


def disorder_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode for product 1

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

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


def epidemiology_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with epidemiological data

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

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


def gene_by_disorder_orphacode(orphacode):  # noqa: E501
    """Disorder by ORPHAcode with associated genes

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int

    :rtype: Product6
    """
    es = config.elastic_server

    index = "en_product6"

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response


def hierarchy_by_orphacode(orphacode):  # noqa: E501
    """Hierarchical classification of disorder by ORPHAcode in all classifications

    Query one disorder by its ORPHAcode and gives the list of occurences in Orphanet&#x27;s classifications with parents and childs disorder ORPHAcode number, the list of its children and parents. # noqa: E501

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
    """Hierarchical classification of disorder by ORPHAcode in selected classification

    Query one disorder by its ORPHAcode and gives the list of parents and childs disorder in the selected Orphanet&#x27;s classification # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: Product3Classification
    """
    es = config.elastic_server

    index = "en_product3_{}".format(hchid)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response


def phenotype_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with its associated phenotype

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4HPO
    """
    es = config.elastic_server

    index = "product4"
    index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"Disorder.ORPHAcode\": " + str(orphacode) + "}}}"

    response = single_res(es, index, query)
    return response
