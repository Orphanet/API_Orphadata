import connexion
import six

from swagger_server.models.list_symbol import ListSymbol  # noqa: E501
from swagger_server.models.product6_gene import Product6Gene  # noqa: E501
from swagger_server.models.product6_gene_list import Product6GeneList  # noqa: E501
from swagger_server import util


def gene_all_symbol():  # noqa: E501
    """Get all genes

    Get the list of all clinical entity referenced in gene # noqa: E501


    :rtype: Product6GeneList
    """
    return 'do some magic!'


def gene_by_symbolv(symbol):  # noqa: E501
    """Gene by gene symbol with associated rare disorder

    Access every information related to a gene by its symbol # noqa: E501

    :param symbol: The symbol is an identifier to reference a gene
    :type symbol: str

    :rtype: Product6Gene
    """
    return 'do some magic!'


def gene_list_symbol():  # noqa: E501
    """List gene symbol to query by gene

    Get the list of gene symbol usable to query by gene # noqa: E501


    :rtype: ListSymbol
    """
    return 'do some magic!'
