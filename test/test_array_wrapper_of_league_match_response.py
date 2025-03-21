# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.array_wrapper_of_league_match_response import ArrayWrapperOfLeagueMatchResponse

class TestArrayWrapperOfLeagueMatchResponse(unittest.TestCase):
    """ArrayWrapperOfLeagueMatchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayWrapperOfLeagueMatchResponse:
        """Test ArrayWrapperOfLeagueMatchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayWrapperOfLeagueMatchResponse`
        """
        model = ArrayWrapperOfLeagueMatchResponse()
        if include_optional:
            return ArrayWrapperOfLeagueMatchResponse(
                message = 'Show this message to user.',
                results = [
                    dupr_backend.models.league_match_response.LeagueMatchResponse(
                        bracket_id = 4684651981, 
                        bracket_name = 'Dreamland Pickleball bracket', 
                        confirmed = True, 
                        display_identity = 'IS20MDL2', 
                        end_date = 'yyyy-mm-dd', 
                        event_format = 'SINGLES', 
                        impacted_draw = True, 
                        in_queue = True, 
                        is_bye_match = False, 
                        is_forfeited = True, 
                        is_next_round_confirmed = True, 
                        is_team_1_tbd = False, 
                        is_team_2_tbd = False, 
                        league_id = 4684651981, 
                        league_match_id = 4684651981, 
                        league_match_status = 'ACTIVE', 
                        league_name = 'Dreamland Pickleball', 
                        location = 'Newport Beach, CA', 
                        match_date = 'yyyy-MM-dd', 
                        match_id = 4684651981, 
                        match_score_added = False, 
                        match_slot = 1, 
                        no_of_games = 3, 
                        registration_id = 4684651981, 
                        round = 56, 
                        score_format = dupr_backend.models.score_format_response.ScoreFormatResponse(
                            format = 'Best 2 out of 3 Games to 11', 
                            games = 1, 
                            id = 56, 
                            priority = 1, 
                            variant = 'Game 3 to 15 or until win by 2', 
                            winning_score = 11, ), 
                        start_date = 'yyyy-mm-dd', 
                        status = 'ACTIVE', 
                        tag = 'EAST', 
                        tbd_1 = 4684651981, 
                        tbd_2 = 4684651981, 
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
                        user_id = 4684651981, 
                        venue = 'Dreamland Pickleball', )
                    ],
                status = 'FAILURE'
            )
        else:
            return ArrayWrapperOfLeagueMatchResponse(
        )
        """

    def testArrayWrapperOfLeagueMatchResponse(self):
        """Test ArrayWrapperOfLeagueMatchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
