# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs  # noqa: E501

    OpenAPI spec version: v1.0 alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import dupr_backend
from dupr_backend.api.user_subscriptions_api import UserSubscriptionsApi  # noqa: E501
from dupr_backend.rest import ApiException


class TestUserSubscriptionsApi(unittest.TestCase):
    """UserSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = UserSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_subscriptions_using_post(self):
        """Test case for add_user_subscriptions_using_post

        addUserSubscriptions  # noqa: E501
        """
        pass

    def test_get_all_user_subscriptions_using_get(self):
        """Test case for get_all_user_subscriptions_using_get

        getAllUserSubscriptions  # noqa: E501
        """
        pass

    def test_remove_user_subscriptions_using_delete(self):
        """Test case for remove_user_subscriptions_using_delete

        removeUserSubscriptions  # noqa: E501
        """
        pass

    def test_update_user_subscriptions_using_put(self):
        """Test case for update_user_subscriptions_using_put

        updateUserSubscriptions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
