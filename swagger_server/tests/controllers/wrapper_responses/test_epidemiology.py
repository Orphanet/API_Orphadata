from __future__ import absolute_import

from swagger_server.tests import BaseTestCase
from swagger_server.config import URL_ENDPOINTS, PRODUCTS
from swagger_server.controllers.response_handler import ResponseWrapper


PRODUCT_ID = 'product9_prev'
PRODUCT = PRODUCTS.get(PRODUCT_ID)


class TestEpidemiologyWrapperResponse(BaseTestCase):
    """Tests response content of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_orphacode = 558
    invalid_orphacode = 1

    wrapper = ResponseWrapper(ctl_response=None, request=None, product=None)

    def test_valid_response_content_wrapper_epidemiology_base(self):
        """test_valid_response_content_wrapper_epidemiology_base

        SETUP: TEST WRAPPER REPONSE for /orphadata/details/rd-epidemiology
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = URL_ENDPOINTS.get('epidemiology_base')
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['product'] == PRODUCT
        assert not response.get_json()['parameters']['path']
        assert not response.get_json()['parameters']['query']
        assert response.get_json()['uri'] == url_endpoint

    def test_valid_response_content_wrapper_epidemiology_orphacodes(self):
        """test_valid_response_content_wrapper_epidemiology_orphacodes

        SETUP: TEST WRAPPER REPONSE for /orphadata/details/rd-epidemiology/orphacodes
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = URL_ENDPOINTS.get('epidemiology_orphacodes')
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['product'] == PRODUCT
        assert not response.get_json()['parameters']['path']
        assert not response.get_json()['parameters']['query']
        assert response.get_json()['uri'] == url_endpoint

    def test_valid_response_content_wrapper_epidemiology_by_orphacode(self):
        """test_valid_response_content_wrapper_epidemiology_by_orphacode

        SETUP: TEST WRAPPER REPONSE /orphadata/details/rd-epidemiology/orphacodes/{}
            - a url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = URL_ENDPOINTS.get('epidemiology_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['product'] == PRODUCT
        assert list(response.get_json()['parameters']['path'].items()) == [('ORPHAcode', self.valid_orphacode)]
        assert not response.get_json()['parameters']['query']
        assert response.get_json()['uri'] == url_endpoint

    def test_invalid_response_content_wrapper_classification_hchids_by_orphacode(self):
        """test_invalid_response_content_wrapper_classification_hchids_by_orphacode

        SETUP: TEST WRAPPER REPONSE /orphadata/details/rd-epidemiology/orphacodes/{}
            - a url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = URL_ENDPOINTS.get('epidemiology_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.error_wrapper().keys()
        assert response.get_json()['error']['code'] == 404