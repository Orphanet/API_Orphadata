import connexion
import six
import requests
import json

from swagger_server import util


def disorder_by_orphanumber(orpha_number):  # noqa: E501
    """Disorder by ORPHAnumber

    Access informations related to a disorder object by its ORPHAnumber # noqa: E501

    :param orpha_number: 
    :type orpha_number: int

    :rtype: None
    """
    # Only if served by docker
    # host = "host.docker.internal:9200"

    host = "localhost:9200"
    index = "product1"
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&pretty".format(host, index, orpha_number)

    response = requests.get(url, timeout=None).text

    try:
        response = json.loads(response)
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        print(response)
    except IndexError:
        print(response)

    return response
