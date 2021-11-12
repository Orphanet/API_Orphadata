from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server.models.product6_list import Product6List  # noqa: E501

import config
import controllers.query_controller as qc


def associatedgene_all_orphacode():  # noqa: E501
    """Get all rare diseases associated to at least one gene.

    The result is a collection of clinical entities (ORPHAcode, preferred term, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, group and type) and their genes associations. For each gene, symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases are also available. # noqa: E501


    :rtype: Product6List
    """
    es = config.elastic_server

    index = "en_product6"

    query = "{\"query\": {\"match_all\": {}}}"

    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = qc.uncapped_res(es, index, query, size, scroll_timeout)
    return response


def associatedgene_list_orphacode():  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one gene.

    The result is a collection of ORPHAcodes associated to at least one gene. # noqa: E501


    :rtype: ListOrphacode
    """
    es = config.elastic_server

    index = "en_product6"

    query = "{\"query\": {\"match_all\": {}}, \"_source\":[\"ORPHAcode\"]}"

    size = config.scroll_size  # per scroll, not limiting

    scroll_timeout = config.scroll_timeout

    response = qc.uncapped_res(es, index, query, size, scroll_timeout)
    if isinstance(response, str) or isinstance(response, tuple):
        pass
    else:
        response = sorted([elem["ORPHAcode"] for elem in response])
    return response


def associatedgene_orphacode(orphacode):  # noqa: E501
    """Get associated genes and genes information of a clinical entity searching by its ORPHAcode.

    The result is a set of data includes ORPhacode, preferred term, expertlink, group and type of the selected clinical entity, relationship between genes and the searched disease and symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases of selected genes. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int

    :rtype: Product6
    """
    es = config.elastic_server

    index = "en_product6"

    query = "{\"query\": {\"match\": {\"ORPHAcode\": " + str(orphacode) + "}}}"

    response = qc.single_res(es, index, query)
    return response


def associatedgene_list_genes():  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one gene.

    The result is a collection of ORPHAcodes associated to at least one gene. # noqa: E501


    :rtype: ListOrphacode
    """
    es = config.elastic_server

    index = "en_product6"

    query = {
        "query": {
            "match_all": {}
        }, 
        "_source":["DisorderGeneAssociation"]
    }

    size = config.scroll_size  # per scroll, not limiting
    scroll_timeout = config.scroll_timeout

    response = qc.uncapped_res(es, index, query, size, scroll_timeout)
    if isinstance(response, str) or isinstance(response, tuple):
        pass
    else:
        response_parsed = []
        for hit in response:
            for gene in hit["DisorderGeneAssociation"]:
                response_parsed.append({'preferredTerm': gene["Gene"]["Preferred term"], 'symbol': gene["Gene"]["Symbol"]})
    
    return sorted(list(set(response_parsed)))


def associatedgene_by_gene_symbol(gene_symbol):
    es = config.elastic_server
    index = "en_product6"

    query = {
        "query": {
            "bool": {
                "filter": {
                    "match": {"DisorderGeneAssociation.Gene.Symbol": str(gene_symbol)}
                }
            }
        },
        # "_source": ["ORPHAcode"]
    }

    response = qc.multiple_res(es, index, query, size=5000)

    return response


def associatedgene_by_gene_name(gene_name):
    es = config.elastic_server
    index = "en_product6"

    # query = {
    #     "query": {
    #         "bool": {
    #             "must": {
    #                 "match": {"DisorderGeneAssociation.Gene.Preferred term": str(gene_name)}
    #             }
    #         }
    #     },
    #     "_source": ["ORPHAcode", "DisorderGeneAssociation.Gene.Preferred term", "DisorderGeneAssociation.Gene.Symbol"]
    # }

    query = {
        "query": {
            "match_phrase": {
                "DisorderGeneAssociation.Gene.Preferred term": {
                    "query": str(gene_name),
                    "slop": 0,
                }
            }
        },
        # "_source": ["ORPHAcode", "DisorderGeneAssociation.Gene.Preferred term", "DisorderGeneAssociation.Gene.Symbol"]
    }

    response = qc.multiple_res(es, index, query, size=5000)

    return response
