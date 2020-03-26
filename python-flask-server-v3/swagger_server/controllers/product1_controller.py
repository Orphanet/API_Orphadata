import connexion
import six

from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server import util


def disorder_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode for product 1

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1
    """
    return 'do some magic!'
