# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.product3_classification import Product3Classification  # noqa: E501
from swagger_server.models.product3_classification_list import Product3ClassificationList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrphaclassifController(BaseTestCase):
    """OrphaclassifController integration test stubs"""

    def test_hierarchy_by_orphacode(self):
        """Test case for hierarchy_by_orphacode

        Hierarchical classification of disorder by ORPHAcode in all classifications
        """
        response = self.client.open(
            '/orphaclassif/orphacode/{orphacode}'.format(orphacode=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hierarchy_id_by_orphacode(self):
        """Test case for hierarchy_id_by_orphacode

        Hierarchical classification of disorder by ORPHAcode in selected classification
        """
        response = self.client.open(
            '/orphaclassif/orphacode/{orphacode}/hchid/{hchid}'.format(orphacode=1, hchid=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
