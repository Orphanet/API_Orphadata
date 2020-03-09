# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDisorderController(BaseTestCase):
    """DisorderController integration test stubs"""

    def test_age_by_orphacode(self):
        """Test case for age_by_orphacode

        Disorder by ORPHAcode with age of onset
        """
        response = self.client.open(
            '/age/orphacode/{orphacode}/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disorder_by_orphacode(self):
        """Test case for disorder_by_orphacode

        Disorder by ORPHAcode for product 1
        """
        response = self.client.open(
            '/product1/orphacode/{orphacode}/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epidemiology_by_orphacode(self):
        """Test case for epidemiology_by_orphacode

        Disorder by ORPHAcode with epidemiological data
        """
        response = self.client.open(
            '/epidemiology/orphacode/{orphacode}/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_gene_by_disorder_orphacode(self):
        """Test case for gene_by_disorder_orphacode

        Disorder by ORPHAcode with associated genes
        """
        response = self.client.open(
            '/associatedgene/orphacode/{orphacode}'.format(orphacode=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_by_orphacode(self):
        """Test case for hierarchy_by_orphacode

        Hierarchical classification of disorder by ORPHAcode
        """
        response = self.client.open(
            '/orphaclassif/orphacode/{orphacode}'.format(orphacode=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotype_by_orphacode(self):
        """Test case for phenotype_by_orphacode

        Disorder by ORPHAcode with its associated phenotype
        """
        response = self.client.open(
            '/phenotype/orphacode/{orphacode}/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
