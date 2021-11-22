# coding: utf-8
from __future__ import absolute_import
from swagger_server.tests import BaseTestCase
from swagger_server.config import URL_ENDPOINTS


class TestClassificationsEndpointsStatus(BaseTestCase):
    """Tests response status of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_hchid = 147
    invalid_hchid = 14
    valid_orphacode = 558
    invalid_orphacode = 'a'

    def test_status_200_classification_hchids(self):
        """test_status_200_classification_hchids

        SETUP: TEST STATUS 200 for /orphadata/details/rd-classification/hchids:
            - a valid url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('classification_hchids')
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_classification_by_hchid(self):
        """test_status_200_classification_by_hchid

        SETUP: TEST STATUS 200 for /orphadata/details/rd-classification/hchids/{hchid}:
            - a url endpoint
                - with a valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('classification_by_hchid').format(self.valid_hchid)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_classification_by_hchid(self):
        """test_status_404_classification_by_hchid

        SETUP: TEST STATUS 404 for /orphadata/details/rd-classification/hchids/{wrong-hchid}:
            - a url endpoint
                - with an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('classification_by_hchid').format(self.invalid_hchid)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_classification_orphacodes_by_hchid(self):
        """test_status_200_classification_orphacodes_by_hchid

        SETUP: TEST STATUS 200 /orphadata/details/rd-classification/hchids/{hchid}/orphacodes:
            - a url endpoint
                - with a valid hchid
            - response keys
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('classification_orphacodes_by_hchid').format(self.valid_hchid)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_classification_orphacodes_by_hchid(self):
        """test_status_404_classification_orphacodes_by_hchid

        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/hchids/{wrong-hchid}/orphacodes:
            - a url endpoint
                - with an invalid hchid
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('classification_orphacodes_by_hchid').format(self.invalid_hchid)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_classification_hchids_by_orphacode(self):
        """test_status_200_classification_hchids_by_orphacode

        SETUP: TEST STATUS 200 /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids:
            - a url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('classification_hchids_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_classification_hchids_by_orphacode(self):
        """test_status_404_classification_hchids_by_orphacode

        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/orphacodes/{wrong-orphacode}/hchids:
            - a url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('classification_hchids_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_classification_by_orphacode_and_hchid_11(self):
        """test_status_200_classification_by_orphacode_and_hchid_11

        SETUP: TEST STATUS 200 /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{hchid}:
            - a url endpoint
                - with a valid orphacode
                - with valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('classification_by_orphacode_and_hchid').format(self.valid_orphacode, self.valid_hchid)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_classification_by_orphacode_and_hchid_10(self):
        """test_status_404_classification_by_orphacode_and_hchid_10

        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{wrong-hchid}:
            - a url endpoint
                - with a valid orphacode and an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('classification_by_orphacode_and_hchid').format(self.valid_orphacode, self.invalid_hchid)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_404_classification_by_orphacode_and_hchid_01(self):
        """test_status_404_classification_by_orphacode_and_hchid_01

        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{wrong-hchid}:
            - a url endpoint
                - with an invalid orphacode and a valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('classification_by_orphacode_and_hchid').format(self.invalid_orphacode, self.valid_hchid)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_404_classification_by_orphacode_and_hchid_00(self):
        """test_status_404_classification_by_orphacode_and_hchid_00

        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{wrong-hchid}:
            - a url endpoint
                - with a invalid orphacode and an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('classification_by_orphacode_and_hchid').format(self.invalid_orphacode, self.invalid_hchid)
        response = self.client.get(url_endpoint)
        self.assert404(response)


if __name__ == '__main__':
    import unittest
    unittest.main()
