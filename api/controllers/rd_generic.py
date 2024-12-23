import elasticsearch.exceptions as es_exceptions
from flask import request, current_app

import api.controllers.query_controller as qc
from api.controllers.response_handler import ResponseWrapper
from api.controllers import PRODUCTS


index = "orphadata_generic"


def products_description():
    es_client = current_app.config.get('ES_NODE')

    orphadata_products = es_client.indices.get('orphadata*product*').keys()
    orphadata_products = sorted(orphadata_products, key=lambda x: (x.split('_')[2], x.split('_')[1]))

    parsed_response = []
    for product in orphadata_products:
        product_id = '_'.join(product.split('_')[2:]) if 'product3' not in product else product.split('_')[2]
        product_lang = product.split('_')[1]

        if not parsed_response:
            parsed_response.append(
                {
                    'productId': product_id,
                    'languages': [product_lang],
                    'productName': PRODUCTS.get(product_id)['name']
                }
            )
        
        else:
            if product_id not in [ x['productId'] for x in parsed_response ]:
                parsed_response.append(
                    {
                        'productId': product_id,
                        'languages': [product_lang],
                        'productName': PRODUCTS.get(product_id)['name']
                    }
                )
            else:
                dict_item = [ x for x in parsed_response if x['productId'] == product_id ][0]
                if product_lang not in dict_item['languages']:  
                    dict_item['languages'].append(product_lang)

    wrapped_response = ResponseWrapper(ctl_response=parsed_response, request=request, product=PRODUCTS.get('generic'))

    return wrapped_response.get()


def generic_product1():
    lang = request.args.get("lang", "en")
    index = "orphadata_{}_product1".format(lang)

    query = {
        'query': {
            'match_all': {}
        },
        '_source': {
            'includes': ['ORPHAcode', 'Preferred term', 'ExternalReference'],
            'excludes': [
                '.*'
            ]
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)

    parsed_response = []

    for hit in response:
        item = {
                "ORPHAcode": hit["ORPHAcode"],
                "preferredTerm": hit["Preferred term"],
                "externalReference": []
                }

        if hit['ExternalReference']:        
            omim_lst = [ x['Reference'] for x in hit['ExternalReference'] if x['Source'] == 'OMIM' ]
            icd_lst = [ x['Reference'] for x in hit['ExternalReference'] if x['Source'] == 'ICD-10' ]

            item["externalReference"].append(
                {
                    "OMIM": [ x for x in omim_lst],
                    "ICD-10": [ x for x in icd_lst],
                }
            )            

        parsed_response.append(item)

    wrapped_response = ResponseWrapper(ctl_response=parsed_response, request=request, product=PRODUCTS.get('product1'))

    return wrapped_response.get()


def generic_product3():
    index = ["orphadata_en_product3_*"]

    query = {
        'query': {
            'match_all': {}
        },
        '_source': ['ORPHAcode', 'name', 'hch_id', 'hch_tag'],
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)

    parsed_response = []
    for hit in response:
        if not parsed_response:
            parsed_response.append(
                {
                    'hchId': hit['hch_id'],
                    'hchTag': hit['hch_tag'],
                    'clinicalEntities': [
                        {
                            'preferredTerm': hit['name'],
                            'ORPHAcode': hit['ORPHAcode']
                        }
                    ],
                }
            )
        else:
            if hit['hch_id'] not in [ x['hchId'] for x in parsed_response ]:
                    parsed_response.append(
                        {
                            'hchId': hit['hch_id'],
                            'hchTag': hit['hch_tag'],
                            'clinicalEntities': [
                                {
                                    'preferredTerm': hit['name'],
                                    'ORPHAcode': hit['ORPHAcode']
                                }
                            ],
                        }
                    )
            else:
                clinical_entites = [ x['clinicalEntities'] for x in parsed_response if hit['hch_id'] == x['hchId'] ][0]
                clinical_entites.append(
                    {
                        'preferredTerm': hit['name'],
                        'ORPHAcode': hit['ORPHAcode']
                    }
                )

    wrapped_response = ResponseWrapper(ctl_response=parsed_response, request=request, product=PRODUCTS.get('product3'))

    return wrapped_response.get()


def generic_product4():
    lang = request.args.get('lang', 'en')
    index = "orphadata_{}_product4".format(lang)

    query = {
        'query': {
            'match_all': {}
        },
        '_source': {
            'includes': ['Disorder.ORPHAcode', 'Disorder.Preferred term', 'Disorder.HPODisorderAssociation'],
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)
    parsed_response = []

    for hit in response:
        item = {
                "ORPHAcode": hit["Disorder"]["ORPHAcode"] or None,
                "preferredTerm": hit["Disorder"]["Preferred term"] or None,
                "associatedHPOs": []
                }

        if hit["Disorder"]['HPODisorderAssociation']:        
            for associated_hpos in hit["Disorder"]['HPODisorderAssociation']:
                hpo_id = associated_hpos['HPO']['HPOId']
                hpo_term = associated_hpos['HPO']['HPOTerm']
                hpo_frequency = associated_hpos['HPOFrequency']

                item["associatedHPOs"].append(
                    {
                        "HPOId": hpo_id,
                        "HPOTerm": hpo_term,
                        "HPOFrequency": hpo_frequency
                    }
                )
        parsed_response.append(item)

    wrapped_response = ResponseWrapper(ctl_response=parsed_response, request=request, product=PRODUCTS.get('product7'))

    return wrapped_response.get()


def generic_product6():
    index = ["orphadata_en_product6"]

    query = {
        'query': {
            'match_all': {}
        },
        '_source': {
            'includes': ['ORPHAcode', 'Preferred term', 'DisorderGeneAssociation.*'],
            'excludes': [
                'DisorderGeneAssociation.SourceOfValidation',
                'DisorderGeneAssociation.DisorderGeneAssociationType',
                'DisorderGeneAssociation.DisorderGeneAssociationStatus',
                'DisorderGeneAssociation.Gene.Locus',
            ]
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)

    parsed_response = []

    for hit in response:
        item = {
                "ORPHAcode": hit["ORPHAcode"],
                "preferredTerm": hit["Preferred term"],
                "associatedGenes": []
                }
        if hit['DisorderGeneAssociation']:        
            for associated_genes in hit['DisorderGeneAssociation']:
                gene_name = associated_genes['Gene']['Preferred term']
                gene_symbol = associated_genes['Gene']['Symbol']

                if associated_genes['Gene']['ExternalReference']:
                    hgnc_lst = [ x['Reference'] for x in associated_genes['Gene']['ExternalReference'] if x['Source'] == 'HGNC' ]
                    if hgnc_lst:
                        item["associatedGenes"].append(
                            {
                                "geneName": gene_name,
                                "geneSymbol": gene_symbol,
                                "HGNC": hgnc_lst[0]
                            }
                        )   

        parsed_response.append(item)

    wrapped_response = ResponseWrapper(ctl_response=parsed_response, request=request, product=PRODUCTS.get('product6'))

    return wrapped_response.get()


def generic_product7():
    index = "orphadata_en_product7"

    query = {
        'query': {
            'match_all': {}
        },
        '_source': {
            'includes': ['ORPHAcode', 'Preferred term', 'DisorderDisorderAssociation'],
            'excludes': [
                'DisorderDisorderAssociation.DisorderDisorderAssociationType',
                'DisorderDisorderAssociation.RootDisorder',
            ]
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)

    parsed_response = []
    for hit in response:
        item = {
                "ORPHAcode": hit["ORPHAcode"],
                "preferredTerm": hit["Preferred term"],
                "preferentialParent": []
                }

        if hit['DisorderDisorderAssociation']:
            for parent in hit['DisorderDisorderAssociation']:
                orphacode = parent['TargetDisorder']['ORPHAcode']
                preferred_term = parent['TargetDisorder']['Preferred term']

                item["preferentialParent"].append(
                    {
                        "ORPHAcode": orphacode,
                        "preferredTerm": preferred_term,
                    }
                )

        parsed_response.append(item)

    wrapped_response = ResponseWrapper(ctl_response=parsed_response, request=request, product=PRODUCTS.get('product7'))

    return wrapped_response.get()


def generic_product9_ages():
    lang = request.args.get('lang', 'en')
    index = "orphadata_{}_product9_ages".format(lang)

    query = {
        'query': {
            'match_all': {}
        },
        '_source': {
            'includes': ['ORPHAcode', 'Preferred term'],
            'excludes': [
                '.*'
            ]
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)
    for hit in response:
        hit['preferredTerm'] = hit.pop('Preferred term')
    
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCTS.get('product9_ages'))

    return wrapped_response.get()


def generic_product9_prev():
    lang = request.args.get('lang', 'en')
    index = "orphadata_{}_product9_prev".format(lang)

    query = {
        'query': {
            'match_all': {}
        },
        '_source': {
            'includes': ['ORPHAcode', 'Preferred term'],
            'excludes': [
                '.*'
            ]
        }
    }

    es_client = current_app.config.get('ES_NODE')
    response = qc.es_scroll(es=es_client, index=index, query=query)
    for hit in response:
        hit['preferredTerm'] = hit.pop('Preferred term')
    
    wrapped_response = ResponseWrapper(ctl_response=response, request=request, product=PRODUCTS.get('product9_prev'))

    return wrapped_response.get()
