# coding: utf-8
"""
200 & 404 status code are tested for RD cross-referencing products endpoints.

The general SAC (Setup, Action, Check) procedures are as follow:
    SETUP: TEST STATUS 200 for /orphadata/details/rd-cross-referencing/orphacodes/{}
        - a valid url endpoint
        - a valid orphacode
    ACTION:
        - GET request on valid url endpoint
    CHECK:
        - response status is 200

    -----------------------------------------------------------------

    SETUP: TEST STATUS 404 for /orphadata/details/rd-cross-referencing/orphacodes/{}
        - a valid url endpoint
        - a invalid orphacode
    ACTION:
        - GET request on valid url endpoint
    CHECK:
        - response status is 404
       
"""
from api.tests import BaseTestCase


class TestReferencesEndpointsStatus(BaseTestCase):
    """Tests response status of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_orphacode = 558
    invalid_orphacode = 'a'
    valid_name = 'marfan'
    invalid_name = 99999
    valid_omim = 100100
    invalid_omim = 0
    valid_icd = 'Q87.4'
    invalid_icd = 'x'

    # def test_status_200_references_base(self):
    #     """test_status_200_references_base

    #     SETUP: TEST STATUS 200 for /orphadata/details/rd-cross-referencing
    #         - a valid url endpoint
    #     ACTION:
    #         - GET request on valid url endpoint
    #     CHECK:
    #         - response status is 200
    #     """
    #     url_endpoint = self.URL_ENDPOINTS.get('references_base')
    #     response = self.client.get(url_endpoint)
    #     self.assert200(response)

    def test_status_200_references_orphacodes(self):
        """test_status_200_references_orphacodes

        SETUP: TEST STATUS 200 for /orphadata/details/rd-cross-referencing/orphacodes'
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_orphacodes')        
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_references_by_orphacode(self):
        """test_status_200_references_by_orphacode

        SETUP: TEST STATUS 200 for /orphadata/details/rd-cross-referencing/orphacodes/{}
            - a url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_references_by_orphacode(self):
        """test_status_404_references_by_orphacode

        SETUP: TEST STATUS 200 for /orphadata/details/rd-cross-referencing/orphacodes/{}
            - a url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_references_by_name(self):
        """test_status_200_references_by_name

        SETUP: TEST STATUS 200 /orphadata/details/rd-cross-referencing/names/{}
            - a url endpoint
                - with a valid name
            - response keys
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_by_name').format(self.valid_name)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_references_by_name(self):
        """test_status_404_references_by_name

        SETUP: TEST STATUS 44 /orphadata/details/rd-cross-referencing/names/{}
            - a url endpoint
                - with an invalid name
            - response keys
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_by_name').format(self.invalid_name)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_references_by_omim(self):
        """test_status_200_references_by_omim

        SETUP: TEST STATUS 200 /orphadata/details/rd-cross-referencing/omims/{}
            - a url endpoint
                - with a valid omim
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_by_omim').format(self.valid_omim)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_references_by_omim(self):
        """test_status_404_references_by_omim

        SETUP: TEST STATUS 404 /orphadata/details/rd-cross-referencing/omims/{}
            - a url endpoint
                - with an invalid omim
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_by_omim').format(self.invalid_omim)
        response = self.client.get(url_endpoint)
        self.assert404(response)

    def test_status_200_references_icds(self):
        """test_status_200_references_icds

        SETUP: TEST STATUS 200 for /orphadata/details/rd-cross-referencing/icds'
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_icds')        
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_references_by_icd(self):
        """test_status_200_references_by_icd

        SETUP: TEST STATUS 200 /orphadata/details/rd-cross-referencing/icds/{}
            - a url endpoint
                - with a valid icd
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_by_icd').format(self.valid_icd)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_references_by_icd(self):
        """test_status_404_references_by_icd

        SETUP: TEST STATUS 404 /orphadata/details/rd-cross-referencing/icds/{}
            - a url endpoint
                - with an invalid icd
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = self.URL_ENDPOINTS.get('references_by_icd').format(self.invalid_icd)
        response = self.client.get(url_endpoint)
        self.assert404(response)


if __name__ == '__main__':
    import unittest
    unittest.main()
