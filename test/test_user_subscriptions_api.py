# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
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

    def test_add_user_subscriptions(self) -> None:
        """Test case for add_user_subscriptions

        """
        pass

    def test_get_all_user_subscriptions(self) -> None:
        """Test case for get_all_user_subscriptions

        """
        pass

    def test_remove_user_subscriptions(self) -> None:
        """Test case for remove_user_subscriptions

        """
        pass

    def test_update_user_subscriptions(self) -> None:
        """Test case for update_user_subscriptions

        """
        pass


if __name__ == '__main__':
    unittest.main()
