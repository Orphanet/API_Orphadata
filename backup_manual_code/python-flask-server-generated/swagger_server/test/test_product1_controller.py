# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product1_list import Product1List  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProduct1Controller(BaseTestCase):
    """Product1Controller integration test stubs"""

    def test_product1_all_orphacode(self):
        """Test case for product1_all_orphacode

        Get all product 1 in selected language
        """
        response = self.client.open(
            '/product1/language/{language}'.format(language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_product1_by_orphacode(self):
        """Test case for product1_by_orphacode

        clinical entity by ORPHAcode for product 1
        """
        response = self.client.open(
            '/product1/orphacode/{orphacode}/language/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_product1_list_orphacode(self):
        """Test case for product1_list_orphacode

        List ORPHAcode for product 1 in selected language
        """
        response = self.client.open(
            '/product1/list_orphacode/language/{language}'.format(language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
