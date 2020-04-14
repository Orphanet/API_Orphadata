# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.list_hchid import ListHchid  # noqa: E501
from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product1_list import Product1List  # noqa: E501
from swagger_server.models.product3 import Product3  # noqa: E501
from swagger_server.models.product3_classification_list import Product3ClassificationList  # noqa: E501
from swagger_server.models.product4 import Product4  # noqa: E501
from swagger_server.models.product4_list import Product4List  # noqa: E501
from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server.models.product6_list import Product6List  # noqa: E501
from swagger_server.models.product9_ages import Product9Ages  # noqa: E501
from swagger_server.models.product9_ages_list import Product9AgesList  # noqa: E501
from swagger_server.models.product9_prev import Product9Prev  # noqa: E501
from swagger_server.models.product9_prev_list import Product9PrevList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClinicalEntityController(BaseTestCase):
    """ClinicalEntityController integration test stubs"""

    def test_associatedgene_all_orphacode(self):
        """Test case for associatedgene_all_orphacode

        Get all associatedgene
        """
        response = self.client.open(
            '/associatedgene',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_associatedgene_list_orphacode(self):
        """Test case for associatedgene_list_orphacode

        List ORPHAcode for clinical entity associated gene
        """
        response = self.client.open(
            '/associatedgene/list_orphacode',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_associatedgene_orphacode(self):
        """Test case for associatedgene_orphacode

        Disorder by ORPHAcode with associated genes
        """
        response = self.client.open(
            '/associatedgene/orphacode/{orphacode}'.format(orphacode=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_hierarchy_all_orphacode(self):
        """Test case for hierarchy_all_orphacode

        Get the full selected classification
        """
        response = self.client.open(
            '/orphaclassif/hchid/{hchid}'.format(hchid=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_by_orphacode(self):
        """Test case for hierarchy_by_orphacode

        Hierarchical classification of clinical entities by ORPHAcode in all classifications
        """
        response = self.client.open(
            '/orphaclassif/orphacode/{orphacode}'.format(orphacode=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_id_by_orphacode(self):
        """Test case for hierarchy_id_by_orphacode

        Hierarchical classification of clinical entities by ORPHAcode in selected classification
        """
        response = self.client.open(
            '/orphaclassif/orphacode/{orphacode}/hchid/{hchid}'.format(orphacode=1, hchid=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_list_hchid(self):
        """Test case for hierarchy_list_hchid

        List hierarchical ID (hchid)
        """
        response = self.client.open(
            '/orphaclassif/list_hchid',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_list_orphacode(self):
        """Test case for hierarchy_list_orphacode

        List ORPHAcode for selected classification
        """
        response = self.client.open(
            '/orphaclassif/list_orphacode/hchid/{hchid}'.format(hchid=1),
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

    def test_phenotype_all_orphacode(self):
        """Test case for phenotype_all_orphacode

        Get all phenotype in selected language
        """
        response = self.client.open(
            '/phenotype/language/{language}'.format(language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotype_by_orphacode(self):
        """Test case for phenotype_by_orphacode

        Disorder by ORPHAcode with its associated phenotype
        """
        response = self.client.open(
            '/phenotype/orphacode/{orphacode}/language/{language}'.format(orphacode=1, language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phenotype_list_orphacode(self):
        """Test case for phenotype_list_orphacode

        List ORPHAcode for phenotype in selected language
        """
        response = self.client.open(
            '/phenotype/list_orphacode/language/{language}'.format(language='language_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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
