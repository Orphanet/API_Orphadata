# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestEpidemiologyController(BaseTestCase):
    """EpidemiologyController integration test stubs"""

    def test_age_by_orphacode(self):
        """Test case for age_by_orphacode

        Disorder by ORPHAcode with age of onset
        """
        response = self.client.open(
            '/age/orphacode/{orphacode}/{language}'.format(orphacode=1, language='language_example'),
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


if __name__ == '__main__':
    import unittest
    unittest.main()
