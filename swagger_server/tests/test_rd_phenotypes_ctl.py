# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.tests import BaseTestCase


class TestRareDiseasesAndAssociatedPhenotypesController(BaseTestCase):
    """RareDiseasesAndAssociatedPhenotypesController integration test stubs"""

    def test_phenotype_all_orphacode(self):
        """Test case for phenotype_all_orphacode

        Get all clinical entities with their associated phenotypes in the selected language.
        """
        response = self.client.open(
            '/phenotype/language/{language}'.format(language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotype_by_orphacode(self):
        """Test case for phenotype_by_orphacode

        Get informations and associated HPO phenotypes of a clinical entity searching by its ORPHAcode in the selected language.
        """
        response = self.client.open(
            '/phenotype/orphacode/{orphacode}/language/{language}'.format(orphacode=558, language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotype_list_orphacode(self):
        """Test case for phenotype_list_orphacode

        Get list of ORPHAcodes associated to HPO phenotypes in the selected language.
        """
        response = self.client.open(
            '/phenotype/list_orphacode/language/{language}'.format(language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
