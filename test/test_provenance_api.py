# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.2.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.provenance_api import ProvenanceApi


class TestProvenanceApi(unittest.TestCase):
    """ ProvenanceApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.provenance_api.ProvenanceApi()

    def tearDown(self):
        pass

    def test_delete_lineage(self):
        """
        Test case for delete_lineage

        Deletes a lineage query
        """
        pass

    def test_delete_provenance(self):
        """
        Test case for delete_provenance

        Deletes a provenance query
        """
        pass

    def test_get_lineage(self):
        """
        Test case for get_lineage

        Gets a lineage query
        """
        pass

    def test_get_provenance(self):
        """
        Test case for get_provenance

        Gets a provenance query
        """
        pass

    def test_get_search_options(self):
        """
        Test case for get_search_options

        Gets the searchable attributes for provenance events
        """
        pass

    def test_submit_lineage_request(self):
        """
        Test case for submit_lineage_request

        Submits a lineage query
        """
        pass

    def test_submit_provenance_request(self):
        """
        Test case for submit_provenance_request

        Submits a provenance query
        """
        pass


if __name__ == '__main__':
    unittest.main()
