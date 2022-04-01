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
        'references_base': '/orphadata/details/rd-cross-referencing',
        'references_orphacodes': '/orphadata/details/rd-cross-referencing/orphacodes',
        'references_by_orphacode': '/orphadata/details/rd-cross-referencing/orphacodes/{}',
        'references_by_name': '/orphadata/details/rd-cross-referencing/orphacodes/names/{}',
        'references_by_omim': '/orphadata/details/rd-cross-referencing/omims/{}',
        'references_icds': '/orphadata/details/rd-cross-referencing/icds',
        'references_by_icd': '/orphadata/details/rd-cross-referencing/icds/{}',
        'classification_hchids': '/orphadata/details/rd-classification/hchids',
        'classification_by_hchid': '/orphadata/details/rd-classification/hchids/{}',
        'classification_orphacodes_by_hchid': '/orphadata/details/rd-classification/hchids/{}/orphacodes',
        'classification_hchids_by_orphacode': '/orphadata/details/rd-classification/orphacodes/{}/hchids',
        'classification_by_orphacode_and_hchid': '/orphadata/details/rd-classification/orphacodes/{}/hchids/{}',
        'phenotypes_base': '/orphadata/details/rd-phenotypes',
        'phenotypes_orphacodes': '/orphadata/details/rd-phenotypes/orphacodes',
        'phenotypes_by_orphacode': '/orphadata/details/rd-phenotypes/orphacodes/{}',
        'phenotypes_by_hpoids': '/orphadata/details/rd-phenotypes/hpoids/{}',
        'genes_base': '/orphadata/details/rd-associated-genes',
        'genes_orphacodes': '/orphadata/details/rd-associated-genes/orphacodes',
        'genes_by_orphacode': '/orphadata/details/rd-associated-genes/orphacodes/{}',
        'genes_genes': '/orphadata/details/rd-associated-genes/genes',
        'genes_by_symbol': '/orphadata/details/rd-associated-genes/genes/symbols/{}',
        'genes_by_name': '/orphadata/details/rd-associated-genes/genes/names/{}',
        'linearization_by_orphacode': '/orphadata/details/rd-medical-specialties/orphacodes/{}',
        'linearization_parents': '/orphadata/details/rd-medical-specialties/parents',
        'linearization_by_parent': '/orphadata/details/rd-medical-specialties/parents/{}',
        'epidemiology_base': '/orphadata/details/rd-epidemiology',
        'epidemiology_orphacodes': '/orphadata/details/rd-epidemiology/orphacodes',
        'epidemiology_by_orphacode': '/orphadata/details/rd-epidemiology/orphacodes/{}',
        'history_base': '/orphadata/details/rd-natural_history',
        'history_orphacodes': '/orphadata/details/rd-natural_history/orphacodes',
        'history_by_orphacode': '/orphadata/details/rd-natural_history/orphacodes/{}'
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
