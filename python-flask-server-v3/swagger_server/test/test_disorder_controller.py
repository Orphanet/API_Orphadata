# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDisorderController(BaseTestCase):
    """DisorderController integration test stubs"""

    def test_disorder_by_orphanumber(self):
        """Test case for disorder_by_orphanumber

        Disorder by ORPHAnumber
        """
        response = self.client.open(
            '/disorder/{orphanumber}'.format(orphanumber=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disorder_by_orphanumber_and_product(self):
        """Test case for disorder_by_orphanumber_and_product

        Disorder by ORPHAnumber and product
        """
        response = self.client.open(
            '/disorder/{orphanumber}/{product}'.format(orphanumber=1, product='product_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
