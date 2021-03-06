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
from swagger_client.apis.connections_api import ConnectionsApi


class TestConnectionsApi(unittest.TestCase):
    """ ConnectionsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.connections_api.ConnectionsApi()

    def tearDown(self):
        pass

    def test_delete_connection(self):
        """
        Test case for delete_connection

        Deletes a connection
        """
        pass

    def test_get_connection(self):
        """
        Test case for get_connection

        Gets a connection
        """
        pass

    def test_update_connection(self):
        """
        Test case for update_connection

        Updates a connection
        """
        pass


if __name__ == '__main__':
    unittest.main()
