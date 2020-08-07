# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.list_symbol import ListSymbol  # noqa: E501
from swagger_server.models.product6_gene import Product6Gene  # noqa: E501
from swagger_server.models.product6_gene_list import Product6GeneList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGenesAssociatedToRareDiseasesController(BaseTestCase):
    """GenesAssociatedToRareDiseasesController integration test stubs"""

    def test_gene_all_symbol(self):
        """Test case for gene_all_symbol

        Get all genes associated to at leat one clinical entity and its information.
        """
        response = self.client.open(
            '/gene',
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_gene_by_symbol(self):
        """Test case for gene_by_symbol

        Get genes informations and associated clinical entity searching by gene symbol.
        """
        response = self.client.open(
            '/gene/symbol/{symbol}'.format(symbol="KIF7"),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_gene_by_invalid_symbol(self):
        """Test case for gene_by_symbol

        Invalid symbol

        Gene by gene symbol with associated rare disorder
        """
        response = self.client.open(
            '/gene/symbol/{symbol}'.format(symbol='not_possible'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_gene_list_symbol(self):
        """Test case for gene_list_symbol

        Get all symbols of genes associated to at leat one clinical entity.
        """
        response = self.client.open(
            '/gene/list_symbol',
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
