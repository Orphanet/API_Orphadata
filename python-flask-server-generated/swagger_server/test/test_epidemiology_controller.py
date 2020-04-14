# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product9_ages import Product9Ages  # noqa: E501
from swagger_server.models.product9_ages_list import Product9AgesList  # noqa: E501
from swagger_server.models.product9_prev import Product9Prev  # noqa: E501
from swagger_server.models.product9_prev_list import Product9PrevList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEpidemiologyController(BaseTestCase):
    """EpidemiologyController integration test stubs"""

    def test_epidemiology_all_orphacode(self):
        """Test case for epidemiology_all_orphacode

        Get all epidemiology in selected language
        """
        response = self.client.open(
            '/epidemiology/language/{language}'.format(language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epidemiology_by_orphacode(self):
        """Test case for epidemiology_by_orphacode

        Disorder by ORPHAcode with epidemiological data
        """
        response = self.client.open(
            '/epidemiology/orphacode/{orphacode}/language/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epidemiology_list_orphacode(self):
        """Test case for epidemiology_list_orphacode

        List ORPHAcode for epidemiology in selected language
        """
        response = self.client.open(
            '/epidemiology/list_orphacode/language/{language}'.format(language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_natural_history_all_orphacode(self):
        """Test case for natural_history_all_orphacode

        Get all natural_history in selected language
        """
        response = self.client.open(
            '/natural_history/language/{language}'.format(language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_natural_history_by_orphacode(self):
        """Test case for natural_history_by_orphacode

        Disorder by ORPHAcode with age of onset
        """
        response = self.client.open(
            '/natural_history/orphacode/{orphacode}/language/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_natural_history_list_orphacode(self):
        """Test case for natural_history_list_orphacode

        List ORPHAcode for natural history in selected language
        """
        response = self.client.open(
            '/natural_history/list_orphacode/language/{language}'.format(language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
