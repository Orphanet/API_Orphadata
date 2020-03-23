import connexion
import six

from swagger_server import util


def hierarchy_by_orphacode(orphacode):  # noqa: E501
    """Hierarchical classification of disorder by ORPHAcode

    Query one disorder by its ORPHAcode and gives its Orphanet classification number, the list of its children and parents. # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int

    :rtype: None
    """
    return 'do some magic!'
