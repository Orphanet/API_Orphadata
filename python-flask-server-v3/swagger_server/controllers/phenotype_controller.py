import connexion
import six

from swagger_server.models.product4_hpo import Product4HPO  # noqa: E501
from swagger_server import util


def phenotype_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with its associated phenotype

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4HPO
    """
    return 'do some magic!'
