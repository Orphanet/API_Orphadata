import json

import connexion
import elasticsearch
import requests
import six
from swagger_server import config

from swagger_server import util
from swagger_server import models
from elasticsearch import Elasticsearch


def age_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with age of onset

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet's concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (EN, FR, ES, DE, IT, PT, NL, PL)
    :type language: dict | bytes

    :rtype: None
    """
    es = config.elastic_server

    index = "product9_ages"
    loc_index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = es.search(index=loc_index, body=query)
    # print(response)

    try:
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        response = "404"
        print(response)
    except IndexError:
        response = "404"
        print(response)
    return response


def disorder_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode for product 1

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet's concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (EN, FR, ES, DE, IT, PT, NL, PL)
    :type language: dict | bytes

    :rtype: None
    """
    es = config.elastic_server

    index = "product1"
    loc_index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = es.search(index=loc_index, body=query)
    # print(response)

    try:
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        response = "404"
        print(response)
    except IndexError:
        response = "404"
        print(response)

    return response


def epidemiology_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with epidemiological data

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet's concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (EN, FR, ES, DE, IT, PT, NL, PL)
    :type language: dict | bytes

    :rtype: None
    """
    es = config.elastic_server

    index = "product9_prev"
    loc_index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = es.search(index=loc_index, body=query)
    # print(response)

    try:
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        response = "404"
        print(response)
    except IndexError:
        response = "404"
        print(response)
    return response


def gene_by_disorder_orphacode(orphacode):  # noqa: E501
    """Disorder by ORPHAcode with associated genes

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet's concept
    :type orphacode: int

    :rtype: None
    """
    es = config.elastic_server

    index = "new_product6_04032020"

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    try:
        response = es.search(index=index, body=query)
        # print(response)
    except:
        print("500")

    try:
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        response = "404"
        print(response)
    except IndexError:
        response = "404"
        print(response)
    return response


def hierarchy_by_orphacode(orphacode):  # noqa: E501
    """Hierarchical classification of disorder by ORPHAcode

    Query one disorder by its ORPHAcode and gives its Orphanet classification number, the list of its children and parents. # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet's concept
    :type orphacode: int

    :rtype: None
    """
    es = config.elastic_server

    index = "en_product3_146"

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = es.search(index=index, body=query)
    # print(response)

    try:
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        response = "404"
        print(response)
    except IndexError:
        response = "404"
        print(response)
    return response


def phenotype_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with its associated phenotype

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet's concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (EN, FR, ES, DE, IT, PT, NL, PL)
    :type language: dict | bytes

    :rtype: None
    """
    es = config.elastic_server

    index = "product4_hpo"
    loc_index = "{}_{}".format(language.lower(), index)

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = es.search(index=loc_index, body=query)
    # print(response)

    try:
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        response = "404"
        print(response)
    except IndexError:
        response = "404"
        print(response)
    return response
