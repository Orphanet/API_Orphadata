import connexion
import six

from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server import util


def gene_by_disorder_orphacode(orphacode):  # noqa: E501
    """Disorder by ORPHAcode with associated genes

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int

    :rtype: Product6
    """
    return 'do some magic!'
