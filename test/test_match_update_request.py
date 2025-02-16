# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import dupr_backend
from dupr_backend.models.match_update_request import MatchUpdateRequest  # noqa: E501
from dupr_backend.rest import ApiException

class TestMatchUpdateRequest(unittest.TestCase):
    """MatchUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MatchUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchUpdateRequest`
        """
        model = dupr_backend.models.match_update_request.MatchUpdateRequest()  # noqa: E501
        if include_optional :
            return MatchUpdateRequest(
                bracket_id = 6806605627, 
                confirmed = False, 
                created = '2020-03-04T17:21:16.000Z', 
                event_date = 'yyyy-MM-dd', 
                event_name = 'event name', 
                league = 'Example League', 
                league_id = 7396161624, 
                league_match_id = 2090230022, 
                location = 'Newport Beach, CA', 
                match_id = 7737603024, 
                match_source = 'DUPR/MANUAL/LEAGUE', 
                reason = 'requested by player', 
                requested_by = 'KO8731', 
                teams = [
                    dupr_backend.models.team_update_request.TeamUpdateRequest(
                        game1 = 11, 
                        game2 = -1, 
                        game3 = -1, 
                        game4 = -1, 
                        game5 = -1, 
                        id = 56, 
                        player1 = 56, 
                        player2 = 56, 
                        winner = True, )
                    ], 
                venue = 'Dreamland Pickleball'
            )
        else :
            return MatchUpdateRequest(
                teams = [
                    dupr_backend.models.team_update_request.TeamUpdateRequest(
                        game1 = 11, 
                        game2 = -1, 
                        game3 = -1, 
                        game4 = -1, 
                        game5 = -1, 
                        id = 56, 
                        player1 = 56, 
                        player2 = 56, 
                        winner = True, )
                    ],
        )
        """

    def testMatchUpdateRequest(self):
        """Test MatchUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
