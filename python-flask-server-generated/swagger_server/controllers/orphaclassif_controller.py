import connexion
import six

from swagger_server.models.list_hchid import ListHchid  # noqa: E501
from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product3 import Product3  # noqa: E501
from swagger_server.models.product3_classification_list import Product3ClassificationList  # noqa: E501
from swagger_server import util


def hierarchy_all_orphacode(hchid):  # noqa: E501
    """Get the full selected classification

    Get the list of all clinical entity referenced in orphaclassif for the selected classification # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: Product3ClassificationList
    """
    return 'do some magic!'


def hierarchy_by_orphacode(orphacode):  # noqa: E501
    """Hierarchical classification of clinical entities by ORPHAcode in all classifications

    Query one clinical entity by its ORPHAcode and gives the list of occurences in Orphanet&#x27;s classifications with parents and childs clinical entity ORPHAcode number, the list of its children and parents. # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int

    :rtype: Product3ClassificationList
    """
    return 'do some magic!'


def hierarchy_id_by_orphacode(orphacode, hchid):  # noqa: E501
    """Hierarchical classification of clinical entities by ORPHAcode in selected classification

    Query one clinical entity by its ORPHAcode and gives the list of parents and childs clinical entity in the selected Orphanet&#x27;s classification # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int
    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: Product3
    """
    return 'do some magic!'


def hierarchy_list_hchid(hchid):  # noqa: E501
    """List hierarchical ID (hchid)

    Get the list of hierarchical ID (hchid) usable to select an Orphanet&#x27;s classification # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: ListHchid
    """
    return 'do some magic!'


def hierarchy_list_orphacode(hchid):  # noqa: E501
    """List ORPHAcode for selected classification

    Get the list of ORPHAcode usable to query the selected classification # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a number which refers to an Orphanet classification
    :type hchid: int

    :rtype: ListOrphacode
    """
    return 'do some magic!'
