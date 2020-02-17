import connexion
import six
import requests
import json

from swagger_server.models.orpha_number import OrphaNumber  # noqa: E501
from swagger_server import util


def get_orpha_number_by_id(OrphaNumber):  # noqa: E501
    """Find a disorder by ORPHAnumber

    Returns a single OrphaNumber # noqa: E501

    :param OrphaNumber: Disorder with OrphaNumber to return
    :type OrphaNumber: int

    :rtype: OrphaNumber
    """
    host = "host.docker.internal:9200"
    index = "product1"
    url = "http://{}/{}/_search?q=fields.OrphaNumber={}&pretty".format(host, index, OrphaNumber)
    response = requests.get(url, timeout=None).text
    response = json.loads(response)
    response = response["hits"]["hits"][0]["_source"]
    return response
