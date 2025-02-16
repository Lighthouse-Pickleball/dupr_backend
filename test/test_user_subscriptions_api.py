# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.api.user_subscriptions_api import UserSubscriptionsApi


class TestUserSubscriptionsApi(unittest.TestCase):
    """UserSubscriptionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserSubscriptionsApi()

    def tearDown(self) -> None:
        pass

    def test_add_user_subscriptions_using_post(self) -> None:
        """Test case for add_user_subscriptions_using_post

        addUserSubscriptions
        """
        pass

    def test_get_all_user_subscriptions_using_get(self) -> None:
        """Test case for get_all_user_subscriptions_using_get

        getAllUserSubscriptions
        """
        pass

    def test_remove_user_subscriptions_using_delete(self) -> None:
        """Test case for remove_user_subscriptions_using_delete

        removeUserSubscriptions
        """
        pass

    def test_update_user_subscriptions_using_put(self) -> None:
        """Test case for update_user_subscriptions_using_put

        updateUserSubscriptions
        """
        pass


if __name__ == '__main__':
    unittest.main()
