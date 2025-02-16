# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.league_match_confirm_request import LeagueMatchConfirmRequest

class TestLeagueMatchConfirmRequest(unittest.TestCase):
    """LeagueMatchConfirmRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeagueMatchConfirmRequest:
        """Test LeagueMatchConfirmRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeagueMatchConfirmRequest`
        """
        model = LeagueMatchConfirmRequest()
        if include_optional:
            return LeagueMatchConfirmRequest(
                league_match_id = 4684651981,
                match_id = 4684651981,
                user_id = 297323232
            )
        else:
            return LeagueMatchConfirmRequest(
                match_id = 4684651981,
                user_id = 297323232,
        )
        """

    def testLeagueMatchConfirmRequest(self):
        """Test LeagueMatchConfirmRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
