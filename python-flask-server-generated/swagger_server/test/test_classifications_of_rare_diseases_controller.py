# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.list_hchid import ListHchid  # noqa: E501
from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product3 import Product3  # noqa: E501
from swagger_server.models.product3_classification_list import Product3ClassificationList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClassificationsOfRareDiseasesController(BaseTestCase):
    """ClassificationsOfRareDiseasesController integration test stubs"""

    def test_hierarchy_all_orphacode(self):
        """Test case for hierarchy_all_orphacode

        Get the organisation of all ORPHAcodes available for a selected classification.
        """
        response = self.client.open(
            '/classification/hchid/{hchid}'.format(hchid=146),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_by_orphacode(self):
        """Test case for hierarchy_by_orphacode

        Hierarchical classification of clinical entities by ORPHAcode in all classifications
        """
        response = self.client.open(
            '/classification/orphacode/{orphacode}'.format(orphacode=558),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_id_by_orphacode(self):
        """Test case for hierarchy_id_by_orphacode

        Hierarchical classification of clinical entities by ORPHAcode in selected classification
        """
        response = self.client.open(
            '/classification/orphacode/{orphacode}/hchid/{hchid}'.format(orphacode=558, hchid=147),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_list_hchid(self):
        """Test case for hierarchy_list_hchid

        Get the list of identifiers of all Orphanet Rare Diseases Classifications available.
        """
        response = self.client.open(
            '/classification/list_hchid',
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_list_orphacode(self):
        """Test case for hierarchy_list_orphacode

        Get the list of ORPHAcodes available for a selected classification.
        """
        response = self.client.open(
            '/classification/list_orphacode/hchid/{hchid}'.format(hchid=146),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
