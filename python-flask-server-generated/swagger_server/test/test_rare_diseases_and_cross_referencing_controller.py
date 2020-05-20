# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product1_list import Product1List  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRareDiseasesAndCrossReferencingController(BaseTestCase):
    """RareDiseasesAndCrossReferencingController integration test stubs"""

    def test_product1_all_orphacode(self):
        """Test case for product1_all_orphacode

        Get all clinical entities informations and their cross-referencing in the selected language.
        """
        response = self.client.open(
            '/product1/language/{language}'.format(language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_product1_by_orphacode(self):
        """Test case for product1_by_orphacode

        Get informations and cross-referencing of a clinical entity searching by its ORPHAcode in the selected language.
        """
        response = self.client.open(
            '/product1/orphacode/{orphacode}/language/{language}'.format(orphacode=558, language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_product1_list_orphacode(self):
        """Test case for product1_list_orphacode

        Get the list of ORPHAcodes available in the selected language.
        """
        response = self.client.open(
            '/product1/list_orphacode/language/{language}'.format(language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
