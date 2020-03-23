import connexion
import six

from swagger_server import util


def age_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with age of onset

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CZ DE EN ES FR IT NL PL PT)
    :type language: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        language = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def epidemiology_by_orphacode(orphacode, language):  # noqa: E501
    """Disorder by ORPHAcode with epidemiological data

    Access every information related to a disorder object by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CZ DE EN ES FR IT NL PL PT)
    :type language: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        language = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
