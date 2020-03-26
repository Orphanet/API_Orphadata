import connexion
import six

import config
from swagger_server.models.product6_gene import Product6Gene  # noqa: E501
from swagger_server import util


def gene_by_symbol(symbol):  # noqa: E501
    """Gene by gene symbol with associated rare disorder

    Access every information related to a gene by its symbol # noqa: E501

    :param symbol: The symbol is an identifier to reference a gene
    :type symbol: str

    :rtype: Product6Gene
    """
    es = config.elastic_server

    index = "new_product6_04032020_gene"

    query = "{\"query\": {\"match\": {\"Symbol\": \"" + symbol.upper() + "\"}}}"

    response = es.search(index=index, body=query)
    print(response)

    try:
        response = response["hits"]["hits"][0]["_source"]
    except KeyError:
        response = "404"
        print(response)
    except IndexError:
        response = "404"
        print(response)
    return response
