# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server.models.product6_list import Product6List  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClinicalEntityAssociatedGeneController(BaseTestCase):
    """ClinicalEntityAssociatedGeneController integration test stubs"""

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


if __name__ == '__main__':
    import unittest
    unittest.main()
