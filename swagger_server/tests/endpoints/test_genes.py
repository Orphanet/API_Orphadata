# coding: utf-8
"""
200 & 404 status code are tested for RD cross-referencing products endpoints.

The general SAC (Setup, Action, Check) procedures are as follow:
    SETUP: TEST STATUS 200 for /orphadata/details/rd-associated-genes/orphacodes/{}
        - a valid url endpoint
        - a valid orphacode
    ACTION:
        - GET request on valid url endpoint
    CHECK:
        - response status is 200

    -----------------------------------------------------------------

    SETUP: TEST STATUS 404 for /orphadata/details/rd-associated-genes/orphacodes/{}
        - a valid url endpoint
        - a invalid orphacode
    ACTION:
        - GET request on valid url endpoint
    CHECK:
        - response status is 404
       
"""
from __future__ import absolute_import
from swagger_server.tests import BaseTestCase
from swagger_server.config import URL_ENDPOINTS


class TestGenesEndpointsStatus(BaseTestCase):
    """Tests response status of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_orphacode = 166024
    invalid_orphacode = 'a'
    valid_name = 'kinesin family'
    invalid_name = 'abc123'
    valid_symbol = 'kif7'
    invalid_symbol = 'abc123'

    def test_status_200_genes_base(self):
        """test_status_200_genes_base

        SETUP: TEST STATUS 200 for /orphadata/details/rd-associated-genes
            - a valid url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('genes_base')
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_genes_orphacodes(self):
        """test_status_200_genes_orphacodes

        SETUP: TEST STATUS 200 for /orphadata/details/rd-associated-genes/orphacodes
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('genes_orphacodes')        
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_genes_by_orphacode(self):
        """test_status_200_genes_by_orphacode

        SETUP: TEST STATUS 200 for /orphadata/details/rd-associated-genes/orphacodes/{}
            - a url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('genes_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_genes_by_orphacode(self):
        """test_status_404_genes_by_orphacode

        SETUP: TEST STATUS 404 for /orphadata/details/rd-associated-genes/orphacodes/{}
            - a url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('genes_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_genes_by_symbol(self):
        """test_status_200_genes_by_symbol

        SETUP: TEST STATUS 200 /orphadata/details/rd-associated-genes/symbols/{}
            - a url endpoint
                - with a valid name
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('genes_by_symbol').format(self.valid_symbol)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_genes_by_symbol(self):
        """test_status_404_genes_by_symbol

        SETUP: TEST STATUS 404 /orphadata/details/rd-associated-genes/symbols/{}
            - a url endpoint
                - with an invalid symbol
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('references_by_name').format(self.invalid_symbol)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_genes_genes(self):
        """test_status_200_genes_genes

        SETUP: TEST STATUS 200 for /orphadata/details/rd-associated-genes/genes'
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('genes_genes')        
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_genes_by_name(self):
        """test_status_200_genes_by_name

        SETUP: TEST STATUS 200 /orphadata/details/rd-associated-genes/names/{}
            - a url endpoint
                - with a valid name
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('genes_by_name').format(self.valid_name)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_genes_by_name(self):
        """test_status_404_genes_by_name

        SETUP: TEST STATUS 404 /orphadata/details/rd-associated-genes/genes/{}
            - a url endpoint
                - with an invalid name
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('genes_by_name').format(self.invalid_name)
        response = self.client.get(url_endpoint)
        self.assert404(response)


if __name__ == '__main__':
    import unittest
    unittest.main()
