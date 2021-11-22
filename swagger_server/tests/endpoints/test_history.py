# coding: utf-8
from __future__ import absolute_import
from swagger_server.tests import BaseTestCase
from swagger_server.config import URL_ENDPOINTS


class TestEpidemiologyEndpointsStatus(BaseTestCase):
    """Tests response status of classification relative endpoints
    """
    _multiprocess_can_split_ = True

    valid_orphacode = 558
    invalid_orphacode = 'a'

    def test_status_200_history_base(self):
        """test_status_200_history_base

        SETUP: TEST STATUS 200 for /orphadata/details/rd-natural_history
            - a valid url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('history_base')
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_history_orphacodes(self):
        """test_status_200_history_orphacodes

        SETUP: TEST STATUS 200 for /orphadata/details/rd-natural_history/orphacodes
            - a url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('history_orphacodes')
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_200_history_by_orphacode(self):
        """test_status_200_history_by_orphacode

        SETUP: TEST STATUS 200 /orphadata/details/rd-natural_history/orphacodes/{}
            - a url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = URL_ENDPOINTS.get('history_by_orphacode').format(self.valid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert200(response)

    def test_status_404_history_by_orphacode(self):
        """test_status_404_history_by_orphacode

        SETUP: TEST STATUS 404 /orphadata/details/rd-natural_history/orphacodes/{}
            - a url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = URL_ENDPOINTS.get('history_by_orphacode').format(self.invalid_orphacode)
        response = self.client.get(url_endpoint)
        self.assert404(response)


if __name__ == '__main__':
    import unittest
    unittest.main()
