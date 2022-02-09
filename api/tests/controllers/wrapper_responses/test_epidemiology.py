from api.tests import BaseTestCase


PRODUCT_ID = 'product9_prev'


class TestEpidemiologyWrapperResponse(BaseTestCase):
    """Tests response content of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_orphacode = 558
    invalid_orphacode = 1


    def test_valid_response_content_wrapper_epidemiology_base(self):
        """test_valid_response_content_wrapper_epidemiology_base

        SETUP: TEST WRAPPER REPONSE for /orphadata/details/rd-epidemiology
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('epidemiology_base')
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['product'] == self.PRODUCTS.get(PRODUCT_ID)
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
        url_endpoint = self.URL_ENDPOINTS.get('epidemiology_orphacodes')
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['product'] == self.PRODUCTS.get(PRODUCT_ID)
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
        url_endpoint = self.URL_ENDPOINTS.get('epidemiology_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['product'] == self.PRODUCTS.get(PRODUCT_ID)
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
        url_endpoint = self.URL_ENDPOINTS.get('epidemiology_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.error_wrapper().keys()
        assert response.get_json()['error']['code'] == 404