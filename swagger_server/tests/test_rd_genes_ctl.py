# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.tests import BaseTestCase


class TestRareDiseasesAndAssociatedGeneController(BaseTestCase):
    """RareDiseasesAndAssociatedGeneController integration test stubs"""

    def test_associatedgene_all_orphacode(self):
        """Test case for associatedgene_all_orphacode

        Get all rare diseases associated to at least one gene.
        """
        response = self.client.open(
            '/associatedgene',
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_associatedgene_list_orphacode(self):
        """Test case for associatedgene_list_orphacode

        Get the list of ORPHAcodes associated to at least one gene.
        """
        response = self.client.open(
            '/associatedgene/list_orphacode',
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_associatedgene_orphacode(self):
        """Test case for associatedgene_orphacode

        Get associated genes and genes information of a clinical entity searching by its ORPHAcode.
        """
        response = self.client.open(
            '/associatedgene/orphacode/{orphacode}'.format(orphacode=93),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
