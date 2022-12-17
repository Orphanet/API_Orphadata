from api.tests import BaseTestCase


PRODUCT_ID = 'product3'


class TestClassificationsWrapperResponse(BaseTestCase):
    """Tests response content of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_hchid = 147
    invalid_hchid = 14
    valid_orphacode = 558
    invalid_orphacode = 1

    def test_valid_response_content_wrapper_classification_hchids(self):
        """test_valid_response_content_wrapper_classification_hchids

        SETUP: TEST WRAPPER REPONSE for /orphadata/details/rd-classification/hchids:
            - a valid url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_hchids')
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['datasetCategory'] == self.PRODUCTS.get(PRODUCT_ID)
        assert not response.get_json()['parameters']['path']
        assert not response.get_json()['parameters']['query']
        assert response.get_json()['uri'] == url_endpoint

    def test_valid_response_content_wrapper_classification_by_hchid(self):
        """test_valid_response_content_wrapper_classification_by_hchid

        SETUP: TEST WRAPPER REPONSE for /orphadata/details/rd-classification/hchids/{}:
            - a valid url endpoint
            - a valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_by_hchid').format(self.valid_hchid)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['datasetCategory'] == self.PRODUCTS.get(PRODUCT_ID)
        assert list(response.get_json()['parameters']['path'].items()) == [('hchID', self.valid_hchid)]
        assert not response.get_json()['parameters']['query']
        assert response.get_json()['uri'] == url_endpoint

    def test_invalid_response_content_wrapper_classification_by_hchid(self):
        """test_valid_response_content_wrapper_classification_by_hchid

        SETUP: TEST WRAPPER REPONSE for /orphadata/details/rd-classification/hchids/{}:
            - a valid url endpoint
            - an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_by_hchid').format(self.invalid_hchid)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.error_wrapper().keys()
        assert response.get_json()['error']['code'] == 404

    def test_valid_response_content_wrapper_classification_orphacodes_by_hchid(self):
        """test_valid_response_content_wrapper_classification_orphacodes_by_hchid

        SETUP: TEST TEST WRAPPER REPONSE /orphadata/details/rd-classification/hchids/{hchid}/orphacodes:
            - a url endpoint
            - with a valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_orphacodes_by_hchid').format(self.valid_hchid)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['datasetCategory'] == self.PRODUCTS.get(PRODUCT_ID)
        assert list(response.get_json()['parameters']['path'].items()) == [('hchID', self.valid_hchid)]
        assert not response.get_json()['parameters']['query']
        assert response.get_json()['uri'] == url_endpoint

    def test_invalid_response_content_wrapper_classification_orphacodes_by_hchid(self):
        """test_invalid_response_content_wrapper_classification_orphacodes_by_hchid

        SETUP: TEST TEST WRAPPER REPONSE /orphadata/details/rd-classification/hchids/{hchid}/orphacodes:
            - a url endpoint
            - with an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_orphacodes_by_hchid').format(self.invalid_hchid)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.error_wrapper().keys()
        assert response.get_json()['error']['code'] == 404

    def test_valid_response_content_wrapper_classification_hchids_by_orphacode(self):
        """test_valid_response_content_wrapper_classification_hchids_by_orphacode

        SETUP: TEST WRAPPER REPONSE /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids:
            - a url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_hchids_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['datasetCategory'] == self.PRODUCTS.get(PRODUCT_ID)
        assert list(response.get_json()['parameters']['path'].items()) == [('ORPHAcode', self.valid_orphacode)]
        assert not response.get_json()['parameters']['query']
        assert response.get_json()['uri'] == url_endpoint

    def test_invalid_response_content_wrapper_classification_hchids_by_orphacode(self):
        """test_invalid_response_content_wrapper_classification_hchids_by_orphacode

        SETUP: TEST WRAPPER REPONSE /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids:
            - a url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_hchids_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.error_wrapper().keys()
        assert response.get_json()['error']['code'] == 404

    def test_valid_response_content_wrapper_classification_by_orphacode_and_hchid_11(self):
        """test_valid_response_content_wrapper_classification_by_orphacode_and_hchid_11

        SETUP: TEST WRAPPER REPONSE /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{hchid}:
            - a url endpoint
                - with a valid orphacode
                - with valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_by_orphacode_and_hchid').format(self.valid_orphacode, self.valid_hchid)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.valid_wrapper().keys()
        assert response.get_json()['datasetCategory'] == self.PRODUCTS.get(PRODUCT_ID)
        assert list(response.get_json()['parameters']['path'].items()) == [('ORPHAcode', self.valid_orphacode), ('hchID', self.valid_hchid)]
        assert not response.get_json()['parameters']['query']
        assert response.get_json()['uri'] == url_endpoint

    def test_invalid_response_content_wrapper_classification_by_orphacode_and_hchid_00(self):
        """test_invalid_response_content_wrapper_classification_by_orphacode_and_hchid_00

        SETUP: TEST WRAPPER REPONSE /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{hchid}:
            - a url endpoint
                - with an invalid orphacode
                - with an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response content of the wrapper
        """
        url_endpoint = self.URL_ENDPOINTS.get('classification_by_orphacode_and_hchid').format(self.invalid_orphacode, self.invalid_hchid)
        response = self.client.get(url_endpoint)

        assert response.is_json == True
        assert response.get_json().keys() == self.wrapper.error_wrapper().keys()
        assert response.get_json()['error']['code'] == 404

