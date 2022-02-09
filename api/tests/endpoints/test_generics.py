# coding: utf-8
"""
Only 200 status code is tested for generics endpoints.

The general SAC (Setup, Action, Check) procedure is as follow:
    SETUP: TEST STATUS 200 for /orphadata/generics
        - a valid url endpoint
    ACTION:
        - GET request on valid url endpoint
    CHECK:
        - response status is 200
"""
from api.tests import BaseTestCase


class TestGenericsEndpointsStatus(BaseTestCase):
    """Tests response status of generics relative endpoints
    """
    _multiprocess_can_split_ = True

    def test_status_200_generics_base(self):
        url_endpoint = self.URL_ENDPOINTS.get('generics_base')
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_generics_references(self):
        url_endpoint = self.URL_ENDPOINTS.get('generics_references')     
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_generics_classification(self):
        url_endpoint = self.URL_ENDPOINTS.get('generics_classification')     
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_generics_phenotypes(self):
        url_endpoint = self.URL_ENDPOINTS.get('generics_phenotypes')     
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_generics_genes(self):
        url_endpoint = self.URL_ENDPOINTS.get('generics_genes')     
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_generics_linearization(self):
        url_endpoint = self.URL_ENDPOINTS.get('generics_linearization')     
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_generics_history(self):
        url_endpoint = self.URL_ENDPOINTS.get('generics_history')     
        response = self.client.get(url_endpoint)
        self.assert200(response)        

    def test_status_200_generics_epidemiology(self):
        url_endpoint = self.URL_ENDPOINTS.get('generics_epidemiology')     
        response = self.client.get(url_endpoint)
        self.assert200(response)


if __name__ == '__main__':
    import unittest
    unittest.main()