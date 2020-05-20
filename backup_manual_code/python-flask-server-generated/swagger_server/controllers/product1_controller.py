import connexion
import six

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product1_list import Product1List  # noqa: E501
from swagger_server import util


def product1_all_orphacode(language):  # noqa: E501
    """Get all product 1 in selected language

    Get the list of all clinical entity referenced in product 1 for the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1List
    """
    return 'do some magic!'


def product1_by_orphacode(orphacode, language):  # noqa: E501
    """clinical entity by ORPHAcode for product 1

    Access every information related to a clinical entity object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1
    """
    return 'do some magic!'


def product1_list_orphacode(language):  # noqa: E501
    """List ORPHAcode for product 1 in selected language

    Get the list of ORPHAcode usable to query product 1 in selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'
