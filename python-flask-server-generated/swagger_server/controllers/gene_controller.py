import connexion

from swagger_server.models.list_symbol import ListSymbol  # noqa: E501
from swagger_server.models.product6_gene import Product6Gene  # noqa: E501
from swagger_server.models.product6_gene_list import Product6GeneList  # noqa: E501
from swagger_server import util

import config
from controllers.query_controller import *


def gene_all_symbol():  # noqa: E501
    """Get all genes

    Get the list of all clinical entity referenced in gene # noqa: E501


    :rtype: Product6GeneList
    """
    es = config.elastic_server

    index = "en_product6_gene"

    query = "{\"query\": {\"match_all\": {}}}"

    size = 1000

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    return response


def gene_by_symbol(symbol):  # noqa: E501
    """Gene by gene symbol with associated rare disorder

    Access every information related to a gene by its symbol # noqa: E501

    :param symbol: The symbol is an identifier to reference a gene
    :type symbol: str

    :rtype: Product6Gene
    """
    es = config.elastic_server

    index = "en_product6_gene"

    query = "{\"query\": {\"match\": {\"Symbol\": \"" + symbol + "\"}}}"

    # query = "{\"query\": {\"bool\":{\"should\": [{\"match\": {\"Symbol\": \"" + symbol + "\"}}," \
    #                                            " {\"match\": {\"Synonym\": \"" + symbol + "\"}}]" \
    #                                                                                       "}}}"

    response = single_res(es, index, query)
    return response


def gene_list_symbol():  # noqa: E501
    """List gene symbol to query by gene

    Get the list of gene symbol usable to query by gene # noqa: E501


    :rtype: ListSymbol
    """
    es = config.elastic_server

    index = "en_product6_gene"

    query = "{\"query\": {\"match_all\": {}}, \"_source\":[\"Symbol\"]}"

    size = 1000

    scroll_timeout = config.scroll_timeout

    response = uncapped_res(es, index, query, size, scroll_timeout)
    if isinstance(response, str) or isinstance(response, tuple):
        pass
    else:
        response = [elem["Symbol"] for elem in response]
    return response
