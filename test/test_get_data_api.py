# coding: utf-8

"""
    Buxfer API

    Buxfer API based on their website.  -----------  Attention! --------------  THIS IS NOT AN OFFICIAL BUXFER.COM API  ----------- Attention! --------------  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: robbiegal@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.get_data_api import GetDataApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGetDataApi(unittest.TestCase):
    """GetDataApi unit test stubs"""

    def setUp(self):
        self.api = GetDataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounts_get(self):
        """Test case for accounts_get

        Get Accounts information  # noqa: E501
        """
        pass

    def test_budgets_get(self):
        """Test case for budgets_get

        Get Budgets information  # noqa: E501
        """
        pass

    def test_contacts_get(self):
        """Test case for contacts_get

        Get Contacts information  # noqa: E501
        """
        pass

    def test_groups_get(self):
        """Test case for groups_get

        Get Groups information  # noqa: E501
        """
        pass

    def test_loans_get(self):
        """Test case for loans_get

        Get Loans information  # noqa: E501
        """
        pass

    def test_reminders_get(self):
        """Test case for reminders_get

        Get Reminders information  # noqa: E501
        """
        pass

    def test_tags_get(self):
        """Test case for tags_get

        Get Tags information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()