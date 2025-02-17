# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.team_update_request import TeamUpdateRequest

class TestTeamUpdateRequest(unittest.TestCase):
    """TeamUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamUpdateRequest:
        """Test TeamUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamUpdateRequest`
        """
        model = TeamUpdateRequest()
        if include_optional:
            return TeamUpdateRequest(
                game1 = 11,
                game2 = -1,
                game3 = -1,
                game4 = -1,
                game5 = -1,
                id = 56,
                player1 = 56,
                player2 = 56,
                winner = True
            )
        else:
            return TeamUpdateRequest(
                player1 = 56,
        )
        """

    def testTeamUpdateRequest(self):
        """Test TeamUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
