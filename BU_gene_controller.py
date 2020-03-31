import connexion
import six

import config
from swagger_server.models.product6_gene import Product6Gene  # noqa: E501
from swagger_server import util

from controllers.query_handlers import *


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
