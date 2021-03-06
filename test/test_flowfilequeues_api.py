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
from swagger_client.apis.flowfilequeues_api import FlowfilequeuesApi


class TestFlowfilequeuesApi(unittest.TestCase):
    """ FlowfilequeuesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.flowfilequeues_api.FlowfilequeuesApi()

    def tearDown(self):
        pass

    def test_create_drop_request(self):
        """
        Test case for create_drop_request

        Creates a request to drop the contents of the queue in this connection.
        """
        pass

    def test_create_flow_file_listing(self):
        """
        Test case for create_flow_file_listing

        Lists the contents of the queue in this connection.
        """
        pass

    def test_delete_listing_request(self):
        """
        Test case for delete_listing_request

        Cancels and/or removes a request to list the contents of this connection.
        """
        pass

    def test_download_flow_file_content(self):
        """
        Test case for download_flow_file_content

        Gets the content for a FlowFile in a Connection.
        """
        pass

    def test_get_drop_request(self):
        """
        Test case for get_drop_request

        Gets the current status of a drop request for the specified connection.
        """
        pass

    def test_get_flow_file(self):
        """
        Test case for get_flow_file

        Gets a FlowFile from a Connection.
        """
        pass

    def test_get_listing_request(self):
        """
        Test case for get_listing_request

        Gets the current status of a listing request for the specified connection.
        """
        pass

    def test_remove_drop_request(self):
        """
        Test case for remove_drop_request

        Cancels and/or removes a request to drop the contents of this connection.
        """
        pass


if __name__ == '__main__':
    unittest.main()
