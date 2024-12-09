from pathlib import Path


# get absolute root path of the project repository (-> orphadata) 
ROOT_DIR = Path(__file__).parent.parent.parent.parent


# URLs of JSONs containing orphadata XML URLs for each product of interest
PATH_PRODUCTS_INFOS = {
    'product1': "https://www.orphadata.com/data/json_api/product1_cross.json",
    'product3': "https://www.orphadata.com/data/json_api/product3_class.json",
    'product4': "https://www.orphadata.com/data/json_api/product4_hpo.json",
    'product6': "https://www.orphadata.com/data/json_api/product6_genes.json",
    'product7': "https://www.orphadata.com/data/json_api/product7_linear.json",
    'product9_prev': "https://www.orphadata.com/data/json_api/product9_prev.json",
    'product9_ages': "https://www.orphadata.com/data/json_api/product9_ages.json",
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