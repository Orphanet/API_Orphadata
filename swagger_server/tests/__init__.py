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
