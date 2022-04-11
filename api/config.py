from elasticsearch import Elasticsearch
import os


def get_es_instance(_type: str='local'):
    es_url = 'http://localhost:9200/'
    es_node = Elasticsearch(
        hosts=["localhost"],
        port=9200,
        timeout=20
    )

    if _type == 'remote':
        es_url = os.getenv('ELASTIC_URL', 'Elastic URL not found.')
        es_node = Elasticsearch(
            hosts=[es_url],
            port=9243,
            http_auth=(os.getenv('ELASTIC_USER', 'Elastic user not found.'), os.getenv('ELASTIC_PASS', 'Elastic pass not found.')),
            timeout=20
        )

    return es_url, es_node


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    DEBUG = False
    JSON_SORT_KEYS = True

    ES_SIZE = 2000
    ES_SCROLL_TIMEOUT = '1m'

    URL_ENDPOINTS = { 
        'references_base': '/rd-cross-referencing',
        'references_orphacodes': '/rd-cross-referencing/orphacodes',
        'references_by_orphacode': '/rd-cross-referencing/orphacodes/{}',
        'references_by_name': '/rd-cross-referencing/orphacodes/names/{}',
        'references_by_omim': '/rd-cross-referencing/omims/{}',
        'references_icds': '/rd-cross-referencing/icds',
        'references_by_icd': '/rd-cross-referencing/icds/{}',
        'classification_hchids': '/rd-classification/hchids',
        'classification_by_hchid': '/rd-classification/hchids/{}',
        'classification_orphacodes_by_hchid': '/rd-classification/hchids/{}/orphacodes',
        'classification_hchids_by_orphacode': '/rd-classification/orphacodes/{}/hchids',
        'classification_by_orphacode_and_hchid': '/rd-classification/orphacodes/{}/hchids/{}',
        'phenotypes_base': '/rd-phenotypes',
        'phenotypes_orphacodes': '/rd-phenotypes/orphacodes',
        'phenotypes_by_orphacode': '/rd-phenotypes/orphacodes/{}',
        'phenotypes_by_hpoids': '/rd-phenotypes/hpoids/{}',
        'genes_base': '/rd-associated-genes',
        'genes_orphacodes': '/rd-associated-genes/orphacodes',
        'genes_by_orphacode': '/rd-associated-genes/orphacodes/{}',
        'genes_genes': '/rd-associated-genes/genes',
        'genes_by_symbol': '/rd-associated-genes/genes/symbols/{}',
        'genes_by_name': '/rd-associated-genes/genes/names/{}',
        'linearization_by_orphacode': '/rd-medical-specialties/orphacodes/{}',
        'linearization_parents': '/rd-medical-specialties/parents',
        'linearization_by_parent': '/rd-medical-specialties/parents/{}',
        'epidemiology_base': '/rd-epidemiology',
        'epidemiology_orphacodes': '/rd-epidemiology/orphacodes',
        'epidemiology_by_orphacode': '/rd-epidemiology/orphacodes/{}',
        'history_base': '/rd-natural_history',
        'history_orphacodes': '/rd-natural_history/orphacodes',
        'history_by_orphacode': '/rd-natural_history/orphacodes/{}'
    }
    

class DevelopmentConfig(Config):
    DEBUG = True

    ES_URL, ES_NODE = get_es_instance(_type='remote')


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    ES_URL, ES_NODE = get_es_instance(_type='local')


class ProductionConfig(Config):
    DEBUG = False

    ES_URL, ES_NODE = get_es_instance(_type='remote')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY
