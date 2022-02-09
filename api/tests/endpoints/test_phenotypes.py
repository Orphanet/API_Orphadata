# coding: utf-8
from __future__ import absolute_import
from api.tests import BaseTestCase


class TestPhenotypesEndpointsStatus(BaseTestCase):
    """Tests response status of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_orphacode = 558
    invalid_orphacode = 'a'
    valid_hpoids = 'HP:0000768,HP:0001065,HP:0001166,HP:0001763'
    invalid_hpoid = 'abcd'

    def test_status_200_phenotypes_base(self):
        """test_status_200_phenotypes_base

        SETUP: TEST STATUS 200 for /orphadata/details/rd-phenotypes
            - a valid url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('phenotypes_base')
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_phenotypes_orphacodes(self):
        """test_status_200_phenotypes_orphacodes

        SETUP: TEST STATUS 200 for /orphadata/details/rd-phenotypes/orphacodes
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('phenotypes_orphacodes')
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_phenotypes_by_orphacode(self):
        """test_status_200_phenotypes_by_orphacode

        SETUP: TEST STATUS 200 /orphadata/details/rd-phenotypes/orphacodes/{}
            - a url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('phenotypes_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_phenotypes_by_orphacode(self):
        """test_status_404_phenotypes_by_orphacode

        SETUP: TEST STATUS 404 /orphadata/details/rd-phenotypes/orphacodes/{}
            - a url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = self.URL_ENDPOINTS.get('phenotypes_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_phenotypes_by_hpoids(self):
        """test_status_200_phenotypes_by_hpoids

        SETUP: TEST STATUS 200 /orphadata/details/rd-phenotypes/hpoids/{}
            - a url endpoint
                - with valid hpoids
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('phenotypes_by_hpoids').format(self.valid_hpoids)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_phenotypes_by_hpoids(self):
        """test_status_404_phenotypes_by_hpoids

        SETUP: TEST STATUS 404 /orphadata/details/rd-phenotypes/hpoids/{}
            - a url endpoint
                - with an invalid hpoid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = self.URL_ENDPOINTS.get('phenotypes_by_hpoids').format(self.invalid_hpoid)
        response = self.client.get(url_endpoint)
        self.assert404(response)


if __name__ == '__main__':
    import unittest
    unittest.main()
