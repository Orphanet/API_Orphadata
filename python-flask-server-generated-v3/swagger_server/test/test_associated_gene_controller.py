# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAssociatedGeneController(BaseTestCase):
    """AssociatedGeneController integration test stubs"""

    def test_gene_by_disorder_orphacode(self):
        """Test case for gene_by_disorder_orphacode

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
