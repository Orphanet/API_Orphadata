# coding: utf-8

from __future__ import absolute_import
from logging import BASIC_FORMAT

from flask import json
from six import BytesIO

from swagger_server.tests import BaseTestCase

import nose


class TestRDClassifications(BaseTestCase):
    """Tests endpoints and functions from controllers.rd_classification.py
    """
    _multiprocess_can_split_ = True

    BASE_URL_API = '/orphadata/details/rd-classification'
    valid_hchid = 147
    invalid_hchid = 14
    valid_orphacode = 558
    invalid_orphacode = 'a'

    def test_hchids_endpoint_status(self):
        """
        SETUP: TEST STATUS 200 for /orphadata/details/rd-classification/hchids:
            - a valid url endpoint
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = '{}/hchids'.format(self.BASE_URL_API)

        response = self.client.get(url_endpoint)

        self.assert200(response)


    def test_hchids_by_valid_hchid_endpoint_status(self):
        """
        SETUP: TEST STATUS 200 for /orphadata/details/rd-classification/hchids/{hchid}:
            - a url endpoint
                - with a valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = '{}/hchids/{}'.format(self.BASE_URL_API, self.valid_hchid)
        
        response = self.client.get(url_endpoint)

        self.assert200(response)


    def test_hchids_by_valid_hchid_response(self):
        """
        SETUP: TEST RESPONSE for /orphadata/details/rd-classification/hchids/{hchid}:
            - a url endpoint
                - with a valid hchid
            - response keys
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response json is a list
            - response json element has valid keys
        """
        url_endpoint = '{}/hchids/{}'.format(self.BASE_URL_API, self.valid_hchid)        
        response_element_keys = ['ORPHAcode', 'childs', 'hch_id', 'hch_tag', 'name', 'parents']

        response = self.client.get(url_endpoint)

        assert isinstance(response.json, list)
        assert False not in [x in response.json[0] for x in response_element_keys]


    def test_hchids_by_invalid_hchid_endpoint_status(self):
        """
        SETUP: TEST STATUS 404 for /orphadata/details/rd-classification/hchids/{wrong-hchid}:
            - a url endpoint
                - with an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = '{}/hchids/{}'.format(self.BASE_URL_API, self.invalid_hchid)

        response = self.client.get(url_endpoint)

        self.assert404(response)


    def test_hchids_orphacodes_by_valid_hchid_status(self):
        """
        SETUP: TEST STATUS 200 /orphadata/details/rd-classification/hchids/{hchid}/orphacodes:
            - a url endpoint
                - with a valid hchid
            - response keys
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = '{}/hchids/{}/orphacodes'.format(self.BASE_URL_API, self.valid_hchid)

        response = self.client.get(url_endpoint)

        self.assert200(response)


    def test_hchids_orphacodes_by_valid_hchid_response(self):
        """
        SETUP: TEST RESPONSE /orphadata/details/rd-classification/hchids/{hchid}/orphacodes:
            - a url endpoint
                - with a valid hchid
            - response keys
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response json is a list
            - response json element has valid keys
        """
        url_endpoint = '{}/hchids/{}/orphacodes'.format(self.BASE_URL_API, self.valid_hchid)
        response_element_keys = ['ORPHAcode', 'name']

        response = self.client.get(url_endpoint)

        assert isinstance(response.json, list)
        assert False not in [x in response.json[0] for x in response_element_keys]


    def test_hchids_orphacodes_by_invalid_hchid_status(self):
        """
        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/hchids/{wrong-hchid}/orphacodes:
            - a url endpoint
                - with an invalid hchid
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = '{}/hchids/{}/orphacodes'.format(self.BASE_URL_API, self.invalid_hchid)

        response = self.client.get(url_endpoint)

        self.assert404(response)


    def test_hchids_by_valid_orphacode_status(self):
        """
        SETUP: TEST STATUS 200 /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids:
            - a url endpoint
                - with a valid orphacode
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = '{}/orphacodes/{}/hchids'.format(self.BASE_URL_API, self.valid_orphacode)

        response = self.client.get(url_endpoint)

        self.assert200(response)


    def test_hchids_by_valid_orphacode_response(self):
        """
        SETUP: TEST RESPONSE /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids:
            - a url endpoint
                - with a valid hchid
            - response keys
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response json is a list
            - response json element has valid keys
        """
        url_endpoint = '{}/orphacodes/{}/hchids'.format(self.BASE_URL_API, self.valid_orphacode)
        response_element_keys = ['ORPHAcode', 'childs', 'hch_id', 'hch_tag', 'name', 'parents']

        response = self.client.get(url_endpoint)

        assert isinstance(response.json, list)
        assert False not in [x in response.json[0] for x in response_element_keys]


    def test_hchids_by_invalid_orphacode_status(self):
        """
        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/orphacodes/{wrong-orphacode}/hchids:
            - a url endpoint
                - with an invalid orphacode
        ACTION:
            - GET request on invalid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = '{}/orphacodes/{}/hchids'.format(self.BASE_URL_API, self.invalid_orphacode)

        response = self.client.get(url_endpoint)

        self.assert404(response)


    def test_hchids_by_valid_orphacode_and_valid_hchid_status(self):
        """
        SETUP: TEST STATUS 200 /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{hchid}:
            - a url endpoint
                - with a valid orphacode
                - with valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 200
        """
        url_endpoint = '{}/orphacodes/{}/hchids/{}'.format(self.BASE_URL_API, self.valid_orphacode, self.valid_hchid)
        
        response = self.client.get(url_endpoint)

        self.assert200(response)


    def test_hchids_by_valid_orphacode_and_invalid_hchid_status(self):
        """
        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{wrong-hchid}:
            - a url endpoint
                - with a valid orphacode
                - with an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = '{}/orphacodes/{}/hchids/{}'.format(self.BASE_URL_API, self.valid_orphacode, self.invalid_hchid)
        
        response = self.client.get(url_endpoint)

        self.assert404(response)
        

    def test_hchids_by_invalid_orphacode_and_valid_hchid_status(self):
        """
        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/orphacodes/{wrong-orphacode}/hchids/{hchid}:
            - a url endpoint
                - with an invalid orphacode
                - with valid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = '{}/orphacodes/{}/hchids/{}'.format(self.BASE_URL_API, self.invalid_orphacode, self.valid_hchid)
        
        response = self.client.get(url_endpoint)

        self.assert404(response)


    def test_hchids_by_invalid_orphacode_and_invalid_hchid_status(self):
        """
        SETUP: TEST STATUS 404 /orphadata/details/rd-classification/orphacodes/{wrong-orphacode}/hchids/{wrong-hchid}:
            - a url endpoint
                - with an invalid orphacode
                - with an invalid hchid
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response status is 404
        """
        url_endpoint = '{}/orphacodes/{}/hchids/{}'.format(self.BASE_URL_API, self.invalid_orphacode, self.invalid_hchid)
        
        response = self.client.get(url_endpoint)

        self.assert404(response)


    def test_hchids_by_valid_orphacode_and_valid_hchid_response(self):
        """
        SETUP: TEST RESPONSE /orphadata/details/rd-classification/orphacodes/{orphacode}/hchids/{hchid}:
            - a url endpoint
                - with a valid orphacode
                - with valid hchid
            - response keys
        ACTION:
            - GET request on valid url endpoint
        CHECK:
            - response json is a dict
            - response json element has expected elements
        """
        url_endpoint = '{}/orphacodes/{}/hchids/{}'.format(self.BASE_URL_API, self.valid_orphacode, self.valid_hchid)
        response_element_keys = ['ORPHAcode', 'childs', 'hch_id', 'hch_tag', 'name', 'parents']

        response = self.client.get(url_endpoint)

        assert isinstance(response.json, dict)
        assert False not in [x in response.json for x in response_element_keys]


if __name__ == '__main__':
    import unittest
    unittest.main()
