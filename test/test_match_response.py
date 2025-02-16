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
from dupr_backend.models.match_response import MatchResponse  # noqa: E501
from dupr_backend.rest import ApiException

class TestMatchResponse(unittest.TestCase):
    """MatchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MatchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchResponse`
        """
        model = dupr_backend.models.match_response.MatchResponse()  # noqa: E501
        if include_optional :
            return MatchResponse(
                bracket_id = 6806605627, 
                client_id = 45, 
                club_id = 7737603024, 
                confirmed = True, 
                created = '2020-03-04T17:21:16.000Z', 
                creator = dupr_backend.models.basic_user_info.BasicUserInfo(
                    email = '', 
                    id = 56, 
                    name = '', 
                    referral_code = '', ), 
                display_identity = 'IS20MDL2', 
                elo_calculated = False, 
                event_date = 'yyyy-MM-dd', 
                event_format = 'SINGLES', 
                event_name = 'event name', 
                id = 7737603024, 
                initialization = False, 
                league = 'Example League', 
                league_id = 7396161624, 
                league_match_id = 2090230022, 
                location = 'Newport Beach, CA', 
                match_id = 7737603024, 
                match_score_added = True, 
                match_source = 'DUPR/MANUAL/LEAGUE', 
                match_type = 'SIDE_OUT/RALLY', 
                modified = '', 
                no_of_games = 2, 
                score_format = dupr_backend.models.score_format_response.ScoreFormatResponse(
                    format = 'Best 2 out of 3 Games to 11', 
                    games = 1, 
                    id = 56, 
                    priority = 1, 
                    variant = 'Game 3 to 15 or until win by 2', 
                    winning_score = 11, ), 
                status = '2', 
                teams = [
                    dupr_backend.models.team_response.TeamResponse(
                        delta = '-0.682', 
                        game1 = 11, 
                        game2 = -1, 
                        game3 = -1, 
                        game4 = -1, 
                        game5 = -1, 
                        id = 56, 
                        player1 = dupr_backend.models.team_player_response.TeamPlayerResponse(
                            allow_substitution = True, 
                            dupr_id = 'https://dupr-dev.s3.amazonaws.com/profile/image.png', 
                            full_name = 'Brian Lara', 
                            id = 26518181881, 
                            image_url = '', 
                            post_match_rating = dupr_backend.models.post_match_rating.PostMatchRating(
                                doubles = 1.337, 
                                singles = 1.337, ), 
                            validated_match = True, ), 
                        player2 = dupr_backend.models.team_player_response.TeamPlayerResponse(
                            allow_substitution = True, 
                            dupr_id = 'https://dupr-dev.s3.amazonaws.com/profile/image.png', 
                            full_name = 'Brian Lara', 
                            id = 26518181881, 
                            image_url = '', 
                            validated_match = True, ), 
                        pre_match_rating_and_impact = dupr_backend.models.pre_match_rating_and_impact.PreMatchRatingAndImpact(
                            match_double_rating_impact_player1 = 1.337, 
                            match_double_rating_impact_player2 = 1.337, 
                            match_single_rating_impact_player1 = 1.337, 
                            match_single_rating_impact_player2 = 1.337, 
                            pre_match_double_rating_player1 = 1.337, 
                            pre_match_double_rating_player2 = 1.337, 
                            pre_match_single_rating_player1 = 1.337, 
                            pre_match_single_rating_player2 = 1.337, ), 
                        serial = 1, 
                        team_rating = '4.659', 
                        winner = True, )
                    ], 
                tournament = 'Newport Beach Doubles Shootout', 
                user_id = 231312312312, 
                validator = dupr_backend.models.basic_user_info.BasicUserInfo(
                    email = '', 
                    id = 56, 
                    name = '', 
                    referral_code = '', ), 
                venue = 'Dreamland Pickleball'
            )
        else :
            return MatchResponse(
                confirmed = True,
                display_identity = 'IS20MDL2',
                event_date = 'yyyy-MM-dd',
                event_format = 'SINGLES',
                location = 'Newport Beach, CA',
                match_score_added = True,
                teams = [
                    dupr_backend.models.team_response.TeamResponse(
                        delta = '-0.682', 
                        game1 = 11, 
                        game2 = -1, 
                        game3 = -1, 
                        game4 = -1, 
                        game5 = -1, 
                        id = 56, 
                        player1 = dupr_backend.models.team_player_response.TeamPlayerResponse(
                            allow_substitution = True, 
                            dupr_id = 'https://dupr-dev.s3.amazonaws.com/profile/image.png', 
                            full_name = 'Brian Lara', 
                            id = 26518181881, 
                            image_url = '', 
                            post_match_rating = dupr_backend.models.post_match_rating.PostMatchRating(
                                doubles = 1.337, 
                                singles = 1.337, ), 
                            validated_match = True, ), 
                        player2 = dupr_backend.models.team_player_response.TeamPlayerResponse(
                            allow_substitution = True, 
                            dupr_id = 'https://dupr-dev.s3.amazonaws.com/profile/image.png', 
                            full_name = 'Brian Lara', 
                            id = 26518181881, 
                            image_url = '', 
                            validated_match = True, ), 
                        pre_match_rating_and_impact = dupr_backend.models.pre_match_rating_and_impact.PreMatchRatingAndImpact(
                            match_double_rating_impact_player1 = 1.337, 
                            match_double_rating_impact_player2 = 1.337, 
                            match_single_rating_impact_player1 = 1.337, 
                            match_single_rating_impact_player2 = 1.337, 
                            pre_match_double_rating_player1 = 1.337, 
                            pre_match_double_rating_player2 = 1.337, 
                            pre_match_single_rating_player1 = 1.337, 
                            pre_match_single_rating_player2 = 1.337, ), 
                        serial = 1, 
                        team_rating = '4.659', 
                        winner = True, )
                    ],
                tournament = 'Newport Beach Doubles Shootout',
                user_id = 231312312312,
                venue = 'Dreamland Pickleball',
        )
        """

    def testMatchResponse(self):
        """Test MatchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
