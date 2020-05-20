import connexion
import six

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product9_ages import Product9Ages  # noqa: E501
from swagger_server.models.product9_ages_list import Product9AgesList  # noqa: E501
from swagger_server.models.product9_prev import Product9Prev  # noqa: E501
from swagger_server.models.product9_prev_list import Product9PrevList  # noqa: E501
from swagger_server import util


def epidemiology_all_orphacode(language):  # noqa: E501
    """Get all epidemiology in selected language

    Get the list of all clinical entity referenced in epidemiology for the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9PrevList
    """
    return 'do some magic!'


def epidemiology_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with epidemiological data

    Access every information related to a clinical entity by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9Prev
    """
    return 'do some magic!'


def epidemiology_list_orphacode(language):  # noqa: E501
    """List ORPHAcode for epidemiology in selected language

    Get the list of ORPHAcode usable to query epidemiology in selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'


def natural_history_all_orphacode(language):  # noqa: E501
    """Get all natural_history in selected language

    Get the list of all clinical entity referenced in natural_history for the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9AgesList
    """
    return 'do some magic!'


def natural_history_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with age of onset

    Access every information related to a clinical entity by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9Ages
    """
    return 'do some magic!'


def natural_history_list_orphacode(language):  # noqa: E501
    """List ORPHAcode for natural history in selected language

    Get the list of ORPHAcode usable to query natural history of clinical entity in selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'
