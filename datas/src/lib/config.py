from pathlib import Path


# get absolute root path of the project repository (-> orphadata) 
ROOT_DIR = Path(__file__).parent.parent.parent.parent


# URLs of JSONs containing orphadata XML URLs for each product of interest
PATH_PRODUCTS_INFOS = {
    'product1': "http://www.orphadata.org/cgi-bin/free_product1_cross_xml.json",
    'product3': "http://www.orphadata.org/cgi-bin/free_product3_class.json",
    'product4': "http://www.orphadata.org/cgi-bin/free_product4_hpo.json",
    'product6':"http://www.orphadata.org/cgi-bin/free_product6_genes.json",
    'product7':"http://www.orphadata.org/cgi-bin/free_product7_linear.json",
    'product9_prev':"http://www.orphadata.org/cgi-bin/free_product9_prev.json",
    'product9_ages':"http://www.orphadata.org/cgi-bin/free_product9_ages.json"
}

# Product full names (used by GenericEsDoc class in generic_parser.py)
PRODUCT_DEF = {
    "product1": "Rare diseases and alignment with terminologies and databases",
    "product3": "Clinical classifications of rare diseases",
    "product4": "Phenotypes associated with rare diseases",
    "product6": "Genes associated with rare diseases",
    "product7": "Linearisation of rare diseases",
    "product9": "Epidemiological data associated with rare diseases",
}