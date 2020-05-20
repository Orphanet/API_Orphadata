import connexion
import six

from swagger_server.models.list_symbol import ListSymbol  # noqa: E501
from swagger_server.models.product6_gene import Product6Gene  # noqa: E501
from swagger_server.models.product6_gene_list import Product6GeneList  # noqa: E501
from swagger_server import util


def gene_all_symbol():  # noqa: E501
    """Get all genes associated to at leat one clinical entity and its information.

    The result is a set of data includes symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases of selected genes and their relationship to clinical entities. For clinical entity, ORPhacode, preferred term, expertlink, group and type are also available. # noqa: E501


    :rtype: Product6GeneList
    """
    return 'do some magic!'


def gene_by_symbol(symbol):  # noqa: E501
    """Get genes informations and associated clinical entity searching by gene symbol.

    The result is a set of data includes symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases of selected genes and their relationship to clinical entities. For clinical entity, ORPhacode, preferred term, expertlink, group and type are also available. # noqa: E501

    :param symbol: The symbol is an identifier to reference a gene
    :type symbol: str

    :rtype: Product6Gene
    """
    return 'do some magic!'


def gene_list_symbol():  # noqa: E501
    """Get all symbols of genes associated to at leat one clinical entity.

    The result is a list of gene symbols (official HGNC-approved gene symbols) associated to at least one clinical entity. # noqa: E501


    :rtype: ListSymbol
    """
    return 'do some magic!'
