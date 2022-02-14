from flask import current_app
from flask_testing import TestCase

import api
from api.controllers import PRODUCTS


class BaseTestCase(TestCase):

    def create_app(self):
        app = api.create_app(config_name='test')
        self.URL_ENDPOINTS = app.config.get('URL_ENDPOINTS')
        self.PRODUCTS = PRODUCTS

        try:
            from api.controllers.response_handler import ResponseWrapper
            self.wrapper = ResponseWrapper(ctl_response=None, request=None, product=None)
        except:
            print('Error from import ResponseWrapper')

        return app