import elasticsearch.exceptions as es_exceptions
from flask import request, current_app

from api.controllers import query_controller as qc
from api.controllers.response_handler import ResponseWrapper
from api.controllers import PRODUCTS


PRODUCT = PRODUCTS.get('product6')
index = "orphadata_en_product6"


def query_genes_base():  # noqa: E501
    """Get all rare diseases associated to at least one gene.

    The result is a collection of clinical entities (ORPHAcode, preferred term, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, group and type) and their genes associations. For each gene, symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases are also available. # noqa: E501


    :rtype: Product6List
    """
    query = {
        "query": {
            "match_all": {}
        },
        # '_source': 'ORPHAcode'
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_genes_orphacodes():
    query = {
        "query": {
            "match_all": {}
        },
        '_source': ['ORPHAcode', 'Preferred term']
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_genes_by_orphacode(orphacode):  # noqa: E501
    """Get associated genes and genes information of a clinical entity searching by its ORPHAcode.

    The result is a set of data includes ORPhacode, preferred term, expertlink, group and type of the selected clinical entity, relationship between genes and the searched disease and symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases of selected genes. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int

    :rtype: Product6
    """
    request.args.params = {'ORPHAcode': orphacode}

    query = {
        "query": {
            "match": {
                "ORPHAcode": str(orphacode)
            }
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.single_res(es_client, index, query)

    if not isinstance(response, tuple):
        for i in range(len(response["DisorderGeneAssociation"])):
            response["DisorderGeneAssociation"][i]["Gene"]["name"] = response["DisorderGeneAssociation"][i]["Gene"].pop("Preferred term")
    
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_genes_genes():  # noqa: E501
    """Get the list of genes associated to at least one clinical entity.

    The result is a collection of genes associated to at least one clinical entity. Each gene is presented by its name(s) and symbol(s)

    """
    query = {
        "query": {
            "match_all": {}
        }, 
        "_source":["DisorderGeneAssociation"]
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es_client, index, query)
    if not isinstance(response, tuple):      
        response_parsed = []
        is_seen = []
        for hit in response:
            for gene in hit["DisorderGeneAssociation"]:
                if gene["Gene"]["Preferred term"] not in is_seen:
                    is_seen.append(gene["Gene"]["Preferred term"])
                    try:
                        gene_hgnc = ', '.join([ x["Reference"] for x in gene["Gene"]["ExternalReference"] if x["Source"] == "HGNC" ])
                    except:
                        gene_hgnc = None
                    response_parsed.append({'name': gene["Gene"]["Preferred term"], 'symbol': gene["Gene"]["Symbol"], "HGNC": gene_hgnc})
    else:
        response_parsed = response

    wrapped_response = ResponseWrapper(ctl_response=sorted(response_parsed, key=lambda x: x["name"]), request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_genes_by_symbol(symbol):
    request.args.params = {'symbol': symbol}

    query = {
        "query": {
            "term": {
                "DisorderGeneAssociation.Gene.Symbol": {
                    'value': str(symbol)
                }
            }
        },
        # "_source": ["ORPHAcode"]
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.multiple_res(es_client, index, query, size=5000)

    if not isinstance(response, tuple):
        for hit in response:
            for i in range(len(hit["DisorderGeneAssociation"])):
                hit["DisorderGeneAssociation"][i]["Gene"]["name"] = hit["DisorderGeneAssociation"][i]["Gene"].pop("Preferred term")

    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()


def query_genes_by_name(name):
    request.args.params = {'name': name}

    query = {
        "query": {
            "match_phrase": {
                "DisorderGeneAssociation.Gene.Preferred term": {
                    "query": str(name),
                    "slop": 0,
                }
            }
        },
        # "_source": ["ORPHAcode", "DisorderGeneAssociation.Gene.Preferred term", "DisorderGeneAssociation.Gene.Symbol"]
    }
    
    es_client = current_app.config.get('ES_NODE')
    response = qc.multiple_res(es_client, index, query, size=5000)

    if not isinstance(response, tuple):
        for hit in response:
            for i in range(len(hit["DisorderGeneAssociation"])):
                hit["DisorderGeneAssociation"][i]["Gene"]["name"] = hit["DisorderGeneAssociation"][i]["Gene"].pop("Preferred term")
            
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCT)
    
    return wrapped_response.get()
