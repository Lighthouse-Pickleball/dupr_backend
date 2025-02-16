# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.user_settings_request import UserSettingsRequest

class TestUserSettingsRequest(unittest.TestCase):
    """UserSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSettingsRequest:
        """Test UserSettingsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSettingsRequest`
        """
        model = UserSettingsRequest()
        if include_optional:
            return UserSettingsRequest(
                settings = {
                    'key' : ''
                    }
            )
        else:
            return UserSettingsRequest(
                settings = {
                    'key' : ''
                    },
        )
        """

    def testUserSettingsRequest(self):
        """Test UserSettingsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
