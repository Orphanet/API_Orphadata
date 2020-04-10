import connexion
import six

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server.models.product6_list import Product6List  # noqa: E501
from swagger_server import util


def associatedgene_all_orphacode():  # noqa: E501
    """Get all associatedgene

    Get the list of all clinical entity referenced in associatedgene # noqa: E501


    :rtype: Product6List
    """
    return 'do some magic!'


def associatedgene_list_orphacode():  # noqa: E501
    """List ORPHAcode for clinical entity associated gene

    Get the list of ORPHAcode usable to query clinical entity associated gene in selected language # noqa: E501


    :rtype: ListOrphacode
    """
    return 'do some magic!'


def associatedgene_orphacode(orphacode):  # noqa: E501
    """Disorder by ORPHAcode with associated genes

    Access every information related to a clinical entity by its ORPHAcode # noqa: E501

    :param orphacode: The ORPHAcode is a unique identifier to reference an Orphanet&#x27;s concept
    :type orphacode: int

    :rtype: Product6
    """
    return 'do some magic!'
