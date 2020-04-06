# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.product6_gene import Product6Gene  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGeneController(BaseTestCase):
    """GeneController integration test stubs"""

    def test_gene_by_valid_symbol(self):
        """Test case for gene_by_symbol

        Valid symbol

        Gene by gene symbol with associated rare disorder
        """
        response = self.client.open(
            '/gene/symbol/{symbol}'.format(symbol='KIF7'),
            method='GET', headers={"ADMIN-API-KEY": "u"})
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_gene_by_invalid_symbol(self):
        """Test case for gene_by_symbol

        Invalid symbol

        Gene by gene symbol with associated rare disorder
        """
        response = self.client.open(
            '/gene/symbol/{symbol}'.format(symbol='not_possible'),
            method='GET', headers={"ADMIN-API-KEY": "u"})
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
