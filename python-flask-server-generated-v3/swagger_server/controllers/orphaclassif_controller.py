import connexion
import six

from swagger_server.models.product3_classification import Product3Classification  # noqa: E501
from swagger_server.models.product3_classification_list import Product3ClassificationList  # noqa: E501
from swagger_server import util


def hierarchy_by_orphacode(orphacode):  # noqa: E501
    """Hierarchical classification of disorder by ORPHAcode in all classifications

    Query one disorder by its ORPHAcode and gives the list of occurences in Orphanet&#x27;s classifications with parents and childs disorder ORPHAcode number, the list of its children and parents. # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int

    :rtype: Product3ClassificationList
    """
    return 'do some magic!'


def hierarchy_id_by_orphacode(orphacode, hchid):  # noqa: E501
    """Hierarchical classification of disorder by ORPHAcode in selected classification

    Query one disorder by its ORPHAcode and gives the list of parents and childs disorder in the selected Orphanet&#x27;s classification # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: Product3Classification
    """
    return 'do some magic!'
