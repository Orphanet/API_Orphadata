import connexion
import six
from flask import json
import requests
from swagger_server import util


def disorder_by_orphanumber(orphanumber):  # noqa: E501
    """Disorder by ORPHAnumber

    Access every information related to a disorder object by its ORPHAnumber # noqa: E501

    :param orphanumber: Access information about a disorder object by its ORPHAnumber
    :type orphanumber: int

    :rtype: None
    """
    # Only if served by docker
    # host = "host.docker.internal:9200"

    host = "localhost:9200"
    index = "product1"
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&pretty".format(host, index, orphanumber)

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


def disorder_by_orphanumber_and_product(orphanumber, product):  # noqa: E501
    """Disorder by ORPHAnumber and product

    Access information related to a disorder object by its ORPHAnumber on a specific subject # noqa: E501

    :param orphanumber: Access information about a disorder object by its ORPHAnumber
    :type orphanumber: int
    :param product: Specify the information bundle
    :type product: str

    :rtype: None
    """
    # Only if served by docker
    # host = "host.docker.internal:9200"

    host = "localhost:9200"
    index = product
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&pretty".format(host, index, orphanumber)

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
