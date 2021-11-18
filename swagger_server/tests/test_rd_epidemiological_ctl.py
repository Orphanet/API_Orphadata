# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.tests import BaseTestCase


class TestEpidemiologicalDataOnRareDiseasesController(BaseTestCase):
    """EpidemiologicalDataOnRareDiseasesController integration test stubs"""

    def test_epidemiology_all_orphacode(self):
        """Test case for epidemiology_all_orphacode

        Get all clinical entities with their epidemiological dataset in the selected language.
        """
        response = self.client.open(
            '/epidemiology/language/{language}'.format(language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epidemiology_by_orphacode(self):
        """Test case for epidemiology_by_orphacode

        Get epideliological informations of a clinical entity searching by its ORPHAcode in the selected language.
        """
        response = self.client.open(
            '/epidemiology/orphacode/{orphacode}/language/{language}'.format(orphacode=558, language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_epidemiology_list_orphacode(self):
        """Test case for epidemiology_list_orphacode

        Get the list of ORPHAcodes associated to at least one epidemiological data.
        """
        response = self.client.open(
            '/epidemiology/list_orphacode/language/{language}'.format(language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_natural_history_all_orphacode(self):
        """Test case for natural_history_all_orphacode

        Get all clinical entities with their natural history data in the selected language.
        """
        response = self.client.open(
            '/natural_history/language/{language}'.format(language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_natural_history_by_orphacode(self):
        """Test case for natural_history_by_orphacode

        Get natural history informations of a clinical entity searching by its ORPHAcode in the selected language.
        """
        response = self.client.open(
            '/natural_history/orphacode/{orphacode}/language/{language}'.format(orphacode=558, language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_natural_history_list_orphacode(self):
        """Test case for natural_history_list_orphacode

        Get the list of ORPHAcodes associated to at least one natural history data.
        """
        response = self.client.open(
            '/natural_history/list_orphacode/language/{language}'.format(language='EN'),
            method='GET', headers={"SIMPLE-API-KEY": "test"})
        if isinstance(response.json, str):
            response.status = "500"
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
