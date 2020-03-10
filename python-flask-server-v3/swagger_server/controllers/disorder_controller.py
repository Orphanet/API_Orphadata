import json

import connexion
import requests
import six
from swagger_server import config

from swagger_server import util
from swagger_server import models


def age_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with age of onset

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet's concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (EN, FR, ES, DE, IT, PT, NL, PL)
    :type language: dict | bytes

    :rtype: None
    """
    # if connexion.request.is_json:
    #     language = models.from_dict(connexion.request.get_json())  # noqa: E501
    host = config.elastichost
    index = "product1"
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&filter_path=hits.hits._source&pretty".format(host, index, orphacode)

    response = requests.get(url, timeout=None).text

    try:
        response = json.loads(response)
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
    # if connexion.request.is_json:
    #     language = models.from_dict(connexion.request.get_json())  # noqa: E501
    host = config.elastichost
    index = "product1"
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&filter_path=hits.hits._source&pretty".format(host, index, orphacode)

    response = requests.get(url, timeout=None).text

    try:
        response = json.loads(response)
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
    # if connexion.request.is_json:
    #     language = models.from_dict(connexion.request.get_json())  # noqa: E501
    host = config.elastichost
    index = "product1"
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&filter_path=hits.hits._source&pretty".format(host, index, orphacode)

    response = requests.get(url, timeout=None).text

    try:
        response = json.loads(response)
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
    host = config.elastichost
    index = "product1"
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&filter_path=hits.hits._source&pretty".format(host, index, orphacode)

    response = requests.get(url, timeout=None).text

    try:
        response = json.loads(response)
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
    host = config.elastichost
    index = "classification_orphanet"

    # url = "http://{}/{}/_search?q=fields.OrphaNumber={}&filter_path=hits.hits._source&pretty".format(host, index, orphacode)
    # response = requests.get(url, timeout=None).text

    url = "http://{}/{}/_search?filter_path=hits.hits._source".format(host, index)

    query = {
        "query": {
            "term": {"OrphaNumber": orphacode}
        }
    }

    response = requests.post(url, json=query).text
    # print(response)
    try:
        response = json.loads(response)
        response = response["hits"]["hits"]
        response = [elem["_source"] for elem in response]
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
    # if connexion.request.is_json:
    #     language = models.from_dict(connexion.request.get_json())  # noqa: E501
    host = config.elastichost
    index = "product1"
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&filter_path=hits.hits._source&pretty".format(host, index, orphacode)

    response = requests.get(url, timeout=None).text

    try:
        response = json.loads(response)
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        response = "404"
        print(response)
    except IndexError:
        response = "404"
        print(response)

    return response
