# coding: utf-8
from __future__ import absolute_import
from swagger_server.tests import BaseTestCase, URL_ENDPOINTS


class TestLineariztionEndpointsStatus(BaseTestCase):
    """Tests response status of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_orphacode = 558
    invalid_orphacode = 'a'
    valid_parent = 93890
    invalid_parent = 1

    def test_status_200_linearization_by_orphacode(self):
        """test_status_200_linearization_by_orphacode

        SETUP: TEST STATUS 200 for /orphadata/details/rd-medical-specialties/orphacodes/{}
            - a valid url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('linearization_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_linearization_by_orphacode(self):
        """test_status_404_linearization_by_orphacode

        SETUP: TEST STATUS 404 for /orphadata/details/rd-medical-specialties/orphacodes/{}
            - a valid url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('linearization_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_linearization_parents(self):
        """test_status_200_linearization_parents

        SETUP: TEST STATUS 200 /orphadata/details/rd-medical-specialties/parents
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('linearization_parents')
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_linearization_by_parent(self):
        """test_status_200_linearization_by_parent

        SETUP: TEST STATUS 200 /orphadata/details/rd-medical-specialties/parents/{}
            - a url endpoint
                - with a valid parent orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('linearization_by_parent').format(self.valid_parent)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_linearization_by_parent(self):
        """test_status_404_linearization_by_parent

        SETUP: TEST STATUS 404 /orphadata/details/rd-medical-specialties/parents/{}
            - a url endpoint
                - with an invalid parent orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('linearization_by_parent').format(self.invalid_parent)
        response = self.client.get(url_endpoint)
        self.assert404(response)


if __name__ == '__main__':
    import unittest
    unittest.main()
