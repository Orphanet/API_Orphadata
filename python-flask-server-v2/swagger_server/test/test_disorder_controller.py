# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.orpha_number import OrphaNumber  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDisorderController(BaseTestCase):
    """DisorderController integration test stubs"""

    def test_get_orpha_number_by_id(self):
        """Test case for get_orpha_number_by_id

        Find a disorder by ORPHAnumber
        """
        response = self.client.open(
            '//disorder/{OrphaNumber}'.format(OrphaNumber=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
