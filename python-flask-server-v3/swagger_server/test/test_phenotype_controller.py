# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestPhenotypeController(BaseTestCase):
    """PhenotypeController integration test stubs"""

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
