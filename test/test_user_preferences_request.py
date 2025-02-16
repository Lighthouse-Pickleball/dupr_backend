# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.user_preferences_request import UserPreferencesRequest

class TestUserPreferencesRequest(unittest.TestCase):
    """UserPreferencesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserPreferencesRequest:
        """Test UserPreferencesRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserPreferencesRequest`
        """
        model = UserPreferencesRequest()
        if include_optional:
            return UserPreferencesRequest(
                enable_email = False,
                enable_newsletter = False,
                enable_privacy = False,
                enable_push = False,
                enable_sms = False
            )
        else:
            return UserPreferencesRequest(
        )
        """

    def testUserPreferencesRequest(self):
        """Test UserPreferencesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
