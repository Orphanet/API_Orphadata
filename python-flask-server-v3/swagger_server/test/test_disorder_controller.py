# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDisorderController(BaseTestCase):
    """DisorderController integration test stubs"""

    def test_disorder_by_orphanumber(self):
        """Test case for disorder_by_orphanumber

        Disorder by ORPHAnumber
        """
        response = self.client.open(
            '/disorder/{orphaNumber}'.format(orpha_number=1),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
