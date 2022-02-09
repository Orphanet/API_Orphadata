import logging
from flask import current_app
from flask_testing import TestCase
import unittest

import api

# logging.getLogger('openapi_spec_validator').setLevel('WARNING')
# logging.getLogger('connexion').setLevel('INFO')
# logging.getLogger('urllib3').setLevel('INFO')
# logging.getLogger('elasticsearch').setLevel('ERROR')


class BaseTestCase(TestCase):
    def create_app(self):
        app = api.create_app(config_name='test')
        self.URL_ENDPOINTS = app.config.get('URL_ENDPOINTS')
        self.PRODUCTS = app.config.get('PRODUCTS')

        try:
            from api.controllers.response_handler import ResponseWrapper
            self.wrapper = ResponseWrapper(ctl_response=None, request=None, product=None)
        except:
            print('Error from import ResponseWrapper')

        return app
