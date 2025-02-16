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
from dupr_backend.models.array_wrapper_of_post_response import ArrayWrapperOfPostResponse  # noqa: E501
from dupr_backend.rest import ApiException

class TestArrayWrapperOfPostResponse(unittest.TestCase):
    """ArrayWrapperOfPostResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ArrayWrapperOfPostResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayWrapperOfPostResponse`
        """
        model = dupr_backend.models.array_wrapper_of_post_response.ArrayWrapperOfPostResponse()  # noqa: E501
        if include_optional :
            return ArrayWrapperOfPostResponse(
                message = 'Show this message to user.', 
                results = [
                    dupr_backend.models.post_response.PostResponse(
                        activity_id = '', 
                        actor = dupr_backend.models.activity_user.ActivityUser(
                            id = 56, 
                            is_follow = True, 
                            name = '', 
                            profile_image = '', ), 
                        content = '', 
                        created_at = 56, 
                        hashtags = [
                            ''
                            ], 
                        id = '', 
                        images = [
                            ''
                            ], 
                        location = dupr_backend.models.location.location(), 
                        matches = [
                            dupr_backend.models.match.Match(
                                bracket_id = 56, 
                                client_id = 56, 
                                club_id = 56, 
                                confirmation_threshold = 56, 
                                confirmed = True, 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                creator = dupr_backend.models.basic_user_info.BasicUserInfo(
                                    email = '', 
                                    id = 56, 
                                    name = '', 
                                    referral_code = '', ), 
                                elo_calculated = True, 
                                elo_rated_match = True, 
                                event = '', 
                                event_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                event_format = 'DOUBLES', 
                                id = 56, 
                                league = '', 
                                league_id = 56, 
                                league_match_id = 56, 
                                location = '', 
                                match_score_added = True, 
                                match_source = 'CLUB', 
                                match_type = 'RALLY', 
                                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                player_ids = [
                                    56
                                    ], 
                                pre_elo_match = True, 
                                pro_match = True, 
                                score_format = dupr_backend.models.score_format.ScoreFormat(
                                    format = '', 
                                    games = 56, 
                                    id = 56, 
                                    priority = 56, 
                                    status = 'ACTIVE', 
                                    variant = '', 
                                    winning_score = 56, ), 
                                status = 'ACTIVE', 
                                teams = [
                                    dupr_backend.models.team.Team(
                                        delta = 1.337, 
                                        game1 = 56, 
                                        game2 = 56, 
                                        game3 = 56, 
                                        game4 = 56, 
                                        game5 = 56, 
                                        id = 56, 
                                        league_match_team_id = 56, 
                                        player1 = dupr_backend.models.player.Player(
                                            age = 56, 
                                            birthdate = '', 
                                            created = '', 
                                            default_rating = 'DOUBLES', 
                                            display_username = True, 
                                            distance = '', 
                                            distance_in_miles = 1.337, 
                                            doubles = 1.337, 
                                            doubles_provisional = True, 
                                            doubles_reliability = 1.337, 
                                            doubles_verified = 1.337, 
                                            email = '', 
                                            enable_privacy = True, 
                                            first_name = '', 
                                            formatted_address = '', 
                                            full_name = '', 
                                            gender = 'FEMALE', 
                                            hand = 'BOTH', 
                                            id = 56, 
                                            image_url = '', 
                                            iso_alpha2_code = '', 
                                            last_name = '', 
                                            latitude = 1.337, 
                                            location = '', 
                                            longitude = 1.337, 
                                            lucra_connected = True, 
                                            phone = '', 
                                            provisional_doubles_rating = 1.337, 
                                            provisional_singles_rating = 1.337, 
                                            referral_code = '', 
                                            registered = True, 
                                            registration_type = 'INVITATION', 
                                            reliability_score = 56, 
                                            short_address = '', 
                                            singles = 1.337, 
                                            singles_provisional = True, 
                                            singles_reliability = 1.337, 
                                            singles_verified = 1.337, 
                                            sponsor = dupr_backend.models.sponsor.Sponsor(
                                                button_text = '', 
                                                description = '', 
                                                id = 56, 
                                                image_url = '', 
                                                sponsor_popup_heading = '', 
                                                sponsor_redirect_url = '', ), 
                                            status = 'ACTIVE', 
                                            username = '', 
                                            verified_email = True, 
                                            verified_phone = True, ), 
                                        player1_doubles_rating = 1.337, 
                                        player1_singles_rating = 1.337, 
                                        player2 = dupr_backend.models.player.Player(
                                            age = 56, 
                                            birthdate = '', 
                                            created = '', 
                                            default_rating = 'DOUBLES', 
                                            display_username = True, 
                                            distance = '', 
                                            distance_in_miles = 1.337, 
                                            doubles = 1.337, 
                                            doubles_provisional = True, 
                                            doubles_reliability = 1.337, 
                                            doubles_verified = 1.337, 
                                            email = '', 
                                            enable_privacy = True, 
                                            first_name = '', 
                                            formatted_address = '', 
                                            full_name = '', 
                                            gender = 'FEMALE', 
                                            hand = 'BOTH', 
                                            id = 56, 
                                            image_url = '', 
                                            iso_alpha2_code = '', 
                                            last_name = '', 
                                            latitude = 1.337, 
                                            location = '', 
                                            longitude = 1.337, 
                                            lucra_connected = True, 
                                            phone = '', 
                                            provisional_doubles_rating = 1.337, 
                                            provisional_singles_rating = 1.337, 
                                            referral_code = '', 
                                            registered = True, 
                                            registration_type = 'INVITATION', 
                                            reliability_score = 56, 
                                            short_address = '', 
                                            singles = 1.337, 
                                            singles_provisional = True, 
                                            singles_reliability = 1.337, 
                                            singles_verified = 1.337, 
                                            status = 'ACTIVE', 
                                            username = '', 
                                            verified_email = True, 
                                            verified_phone = True, ), 
                                        player2_doubles_rating = 1.337, 
                                        player2_singles_rating = 1.337, 
                                        player_ids = [
                                            56
                                            ], 
                                        pre_match_rating_and_impact = dupr_backend.models.pre_match_rating_and_impact.PreMatchRatingAndImpact(
                                            match_double_rating_impact_player1 = 1.337, 
                                            match_double_rating_impact_player2 = 1.337, 
                                            match_single_rating_impact_player1 = 1.337, 
                                            match_single_rating_impact_player2 = 1.337, 
                                            pre_match_double_rating_player1 = 1.337, 
                                            pre_match_double_rating_player2 = 1.337, 
                                            pre_match_single_rating_player1 = 1.337, 
                                            pre_match_single_rating_player2 = 1.337, ), 
                                        priority = 56, 
                                        team_player1 = dupr_backend.models.team_player.TeamPlayer(
                                            allow_substitution = True, 
                                            email = '', 
                                            full_name = '', 
                                            id = 56, 
                                            image_url = '', 
                                            post_match_rating = dupr_backend.models.post_match_rating.PostMatchRating(
                                                doubles = 1.337, 
                                                singles = 1.337, ), 
                                            referral_code = '', 
                                            status = 'ACTIVE', 
                                            validated_match = True, 
                                            verified_email = True, ), 
                                        team_player2 = dupr_backend.models.team_player.TeamPlayer(
                                            allow_substitution = True, 
                                            email = '', 
                                            full_name = '', 
                                            id = 56, 
                                            image_url = '', 
                                            referral_code = '', 
                                            status = 'ACTIVE', 
                                            validated_match = True, 
                                            verified_email = True, ), 
                                        team_rating = 1.337, 
                                        winner = True, )
                                    ], 
                                tournament = '', 
                                used_in_initialization = True, 
                                user_id = 56, 
                                validator = dupr_backend.models.basic_user_info.BasicUserInfo(
                                    email = '', 
                                    id = 56, 
                                    name = '', 
                                    referral_code = '', ), 
                                venue = '', )
                            ], 
                        own_reactions = {
                            'key' : [
                                dupr_backend.models.post_reaction_response.PostReactionResponse(
                                    activity_id = '', 
                                    actor = dupr_backend.models.activity_user.ActivityUser(
                                        id = 56, 
                                        is_follow = True, 
                                        name = '', 
                                        profile_image = '', ), 
                                    children = {
                                        'key' : [
                                            dupr_backend.models.post_reaction_response.PostReactionResponse(
                                                activity_id = '', 
                                                actor = , 
                                                children = {
                                                    'key' : [
                                                        
                                                        ]
                                                    }, 
                                                comment = '', 
                                                created_at = 56, 
                                                getstream_id = '', 
                                                id = '', 
                                                images = [
                                                    ''
                                                    ], 
                                                matches = [
                                                    dupr_backend.models.match.Match(
                                                        bracket_id = 56, 
                                                        client_id = 56, 
                                                        club_id = 56, 
                                                        confirmation_threshold = 56, 
                                                        confirmed = True, 
                                                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        elo_calculated = True, 
                                                        elo_rated_match = True, 
                                                        event = '', 
                                                        event_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                                        event_format = 'DOUBLES', 
                                                        id = 56, 
                                                        league = '', 
                                                        league_id = 56, 
                                                        league_match_id = 56, 
                                                        location = '', 
                                                        match_score_added = True, 
                                                        match_source = 'CLUB', 
                                                        match_type = 'RALLY', 
                                                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        player_ids = , 
                                                        pre_elo_match = True, 
                                                        pro_match = True, 
                                                        status = 'ACTIVE', 
                                                        teams = [
                                                            dupr_backend.models.team.Team(
                                                                delta = 1.337, 
                                                                game1 = 56, 
                                                                game2 = 56, 
                                                                game3 = 56, 
                                                                game4 = 56, 
                                                                game5 = 56, 
                                                                id = 56, 
                                                                league_match_team_id = 56, 
                                                                player1_doubles_rating = 1.337, 
                                                                player1_singles_rating = 1.337, 
                                                                player2_doubles_rating = 1.337, 
                                                                player2_singles_rating = 1.337, 
                                                                player_ids = , 
                                                                priority = 56, 
                                                                team_rating = 1.337, 
                                                                winner = True, )
                                                            ], 
                                                        tournament = '', 
                                                        used_in_initialization = True, 
                                                        user_id = 56, 
                                                        venue = '', )
                                                    ], 
                                                parent_id = '', 
                                                post_id = '', 
                                                react = 'COMMENT', 
                                                reaction_counts = {
                                                    'key' : dupr_backend.models.number.Number()
                                                    }, 
                                                tags = [
                                                    
                                                    ], 
                                                updated_at = 56, )
                                            ]
                                        }, 
                                    comment = '', 
                                    created_at = 56, 
                                    getstream_id = '', 
                                    id = '', 
                                    images = , 
                                    matches = , 
                                    parent_id = '', 
                                    post_id = '', 
                                    react = 'COMMENT', 
                                    reaction_counts = {
                                        'key' : dupr_backend.models.number.Number()
                                        }, 
                                    tags = [
                                        
                                        ], 
                                    updated_at = 56, )
                                ]
                            }, 
                        reaction_counts = , 
                        tags = , 
                        updated_at = 56, 
                        verb = 'MATCH', )
                    ], 
                status = 'FAILURE'
            )
        else :
            return ArrayWrapperOfPostResponse(
        )
        """

    def testArrayWrapperOfPostResponse(self):
        """Test ArrayWrapperOfPostResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
