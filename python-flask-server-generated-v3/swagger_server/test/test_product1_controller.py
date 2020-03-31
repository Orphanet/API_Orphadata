# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProduct1Controller(BaseTestCase):
    """Product1Controller integration test stubs"""

    def test_disorder_by_orphacode(self):
        """Test case for disorder_by_orphacode

        Disorder by ORPHAcode for product 1
        """
        response = self.client.open(
            '/product1/orphacode/{orphacode}/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
