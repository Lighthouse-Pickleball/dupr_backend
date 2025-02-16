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
from dupr_backend.models.edit_match_request import EditMatchRequest  # noqa: E501
from dupr_backend.rest import ApiException

class TestEditMatchRequest(unittest.TestCase):
    """EditMatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EditMatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditMatchRequest`
        """
        model = dupr_backend.models.edit_match_request.EditMatchRequest()  # noqa: E501
        if include_optional :
            return EditMatchRequest(
                bracket_id = 56168168161, 
                is_forfeited = True, 
                league_match_id = 56168168161, 
                match_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                match_id = 56168168161, 
                team1_score = dupr_backend.models.edit_score_request.EditScoreRequest(
                    game1 = 7, 
                    game2 = 11, 
                    game3 = 0, 
                    game4 = 0, 
                    game5 = 0, 
                    team_id = 56168168161, 
                    winner = True, ), 
                team2_score = dupr_backend.models.edit_score_request.EditScoreRequest(
                    game1 = 7, 
                    game2 = 11, 
                    game3 = 0, 
                    game4 = 0, 
                    game5 = 0, 
                    team_id = 56168168161, 
                    winner = True, )
            )
        else :
            return EditMatchRequest(
                match_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                match_id = 56168168161,
                team1_score = dupr_backend.models.edit_score_request.EditScoreRequest(
                    game1 = 7, 
                    game2 = 11, 
                    game3 = 0, 
                    game4 = 0, 
                    game5 = 0, 
                    team_id = 56168168161, 
                    winner = True, ),
                team2_score = dupr_backend.models.edit_score_request.EditScoreRequest(
                    game1 = 7, 
                    game2 = 11, 
                    game3 = 0, 
                    game4 = 0, 
                    game5 = 0, 
                    team_id = 56168168161, 
                    winner = True, ),
        )
        """

    def testEditMatchRequest(self):
        """Test EditMatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
