import logging
import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('openapi_spec_validator').setLevel('INFO')
        logging.getLogger('connexion').setLevel('INFO')
        logging.getLogger('urllib3').setLevel('INFO')
        logging.getLogger('elasticsearch').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app


URL_ENDPOINTS = {    
	'generics_base': '/orphadata/generics',
	'generics_references': '/orphadata/generics/rd-cross-referencing',
	'generics_classification': '/orphadata/generics/rd-classification',
	'generics_phenotypes': '/orphadata/generics/rd-phenotypes',
	'generics_genes': '/orphadata/generics/rd-associated-genes',
	'generics_linearization': '/orphadata/generics/rd-medical-specialties',
	'generics_history': '/orphadata/generics/rd-natural-history',
	'generics_epidemiology': '/orphadata/generics/rd-epidemiology',
	'references_base': '/orphadata/details/rd-cross-referencing',
	'references_orphacodes': '/orphadata/details/rd-cross-referencing/orphacodes',
	'references_by_orphacode': '/orphadata/details/rd-cross-referencing/orphacodes/{}',
	'references_by_name': '/orphadata/details/rd-cross-referencing/names/{}',
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

