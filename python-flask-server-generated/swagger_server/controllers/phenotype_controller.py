import connexion
import six

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product4 import Product4  # noqa: E501
from swagger_server.models.product4_list import Product4List  # noqa: E501
from swagger_server import util


def phenotype_all_orphacode(language):  # noqa: E501
    """Get all phenotype in selected language

    Get the list of all clinical entity referenced in phenotype for the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4List
    """
    return 'do some magic!'


def phenotype_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with its associated phenotype

    Access every information related to a clinical entity by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4
    """
    return 'do some magic!'


def phenotype_list_orphacode(language):  # noqa: E501
    """List ORPHAcode for phenotype in selected language

    Get the list of ORPHAcode usable to query phenotype in selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'
