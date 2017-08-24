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
from swagger_client.apis.tenants_api import TenantsApi


class TestTenantsApi(unittest.TestCase):
    """ TenantsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.tenants_api.TenantsApi()

    def tearDown(self):
        pass

    def test_create_user(self):
        """
        Test case for create_user

        Creates a user
        """
        pass

    def test_create_user_group(self):
        """
        Test case for create_user_group

        Creates a user group
        """
        pass

    def test_get_user(self):
        """
        Test case for get_user

        Gets a user
        """
        pass

    def test_get_user_group(self):
        """
        Test case for get_user_group

        Gets a user group
        """
        pass

    def test_get_user_groups(self):
        """
        Test case for get_user_groups

        Gets all user groups
        """
        pass

    def test_get_users(self):
        """
        Test case for get_users

        Gets all users
        """
        pass

    def test_remove_user(self):
        """
        Test case for remove_user

        Deletes a user
        """
        pass

    def test_remove_user_group(self):
        """
        Test case for remove_user_group

        Deletes a user group
        """
        pass

    def test_search_cluster(self):
        """
        Test case for search_cluster

        Searches for a tenant with the specified identity
        """
        pass

    def test_update_user(self):
        """
        Test case for update_user

        Updates a user
        """
        pass

    def test_update_user_group(self):
        """
        Test case for update_user_group

        Updates a user group
        """
        pass


if __name__ == '__main__':
    unittest.main()