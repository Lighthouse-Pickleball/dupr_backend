# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.set_club_settings_request import SetClubSettingsRequest

class TestSetClubSettingsRequest(unittest.TestCase):
    """SetClubSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetClubSettingsRequest:
        """Test SetClubSettingsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetClubSettingsRequest`
        """
        model = SetClubSettingsRequest()
        if include_optional:
            return SetClubSettingsRequest(
                club_id = 56,
                settings = dupr_backend.models.club_settings.ClubSettings(
                    auto_approve_join_requests = True, )
            )
        else:
            return SetClubSettingsRequest(
                settings = dupr_backend.models.club_settings.ClubSettings(
                    auto_approve_join_requests = True, ),
        )
        """

    def testSetClubSettingsRequest(self):
        """Test SetClubSettingsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
