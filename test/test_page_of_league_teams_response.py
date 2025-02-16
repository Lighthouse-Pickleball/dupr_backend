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
from dupr_backend.models.page_of_league_teams_response import PageOfLeagueTeamsResponse  # noqa: E501
from dupr_backend.rest import ApiException

class TestPageOfLeagueTeamsResponse(unittest.TestCase):
    """PageOfLeagueTeamsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageOfLeagueTeamsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageOfLeagueTeamsResponse`
        """
        model = dupr_backend.models.page_of_league_teams_response.PageOfLeagueTeamsResponse()  # noqa: E501
        if include_optional :
            return PageOfLeagueTeamsResponse(
                empty = False, 
                has_more = False, 
                has_previous = True, 
                hits = [
                    dupr_backend.models.league_teams_response.LeagueTeamsResponse(
                        partner_status = 'ACTIVE', 
                        player1 = dupr_backend.models.player_response.PlayerResponse(
                            age = 55, 
                            display_username = True, 
                            distance = 'Nearby', 
                            distance_in_miles = 15.4, 
                            dupr_id = '8M2YEL', 
                            email = 'user@exmaple.com', 
                            enable_privacy = False, 
                            first_name = 'John', 
                            formatted_address = '5800 PA-378, Center Valley, PA 18034, United States', 
                            full_name = 'John Doe', 
                            gender = 'MALE', 
                            hand = 'RIGHT', 
                            id = 26518181881, 
                            image_url = 'https://dupr-dev.s3.amazonaws.com/profile/image.png', 
                            invited = True, 
                            is_logged_in_user = False, 
                            is_player1 = False, 
                            is_substitute = True, 
                            last_name = 'Doe', 
                            latitude = 72.34654645455, 
                            longitude = 19.55151584984, 
                            lucra_connected = True, 
                            partner_status = 'INVITED/CONFIRMED/NOT_CONFIRMED/CANCELLED', 
                            phone = '+14445785789', 
                            ratings = dupr_backend.models.player_rating_response.PlayerRatingResponse(
                                default_rating = 'DOUBLES', 
                                doubles = '2.864', 
                                doubles_provisional = True, 
                                doubles_reliability_score = 10.0, 
                                doubles_verified = '2.75', 
                                provisional_ratings = dupr_backend.models.provisional_rating.ProvisionalRating(
                                    doubles_rating = 3.5, 
                                    singles_rating = 3.5, ), 
                                singles = '4.125', 
                                singles_provisional = True, 
                                singles_reliability_score = 10.0, 
                                singles_verified = '4.1', ), 
                            registered = True, 
                            registration_details = dupr_backend.models.registration_response.RegistrationResponse(
                                event_refunded_amount = 1.337, 
                                is_participant1 = False, 
                                is_wait_listed = False, 
                                player2 = dupr_backend.models.participant.Participant(
                                    club_member = True, 
                                    display_username = True, 
                                    full_name = 'Brian Lara', 
                                    id = 26518181881, 
                                    is_registered = False, 
                                    is_substitute = False, 
                                    is_wait_listed = False, 
                                    partner_status = 'NOT_ADDED/CONFIRMED/NOT_CONFIRMED/PAYMENT_DUE', 
                                    payment_due = '2021-12-01', 
                                    payment_refunded = False, 
                                    payment_status = 'PENDING/COMPLETE', 
                                    refund_amount = 1.337, 
                                    status = 'NOT_ADDED/CONFIRMED/NOT_CONFIRMED/PAYMENT_DUE', 
                                    username = 'X AE A-XII', ), 
                                registration_id = 4684651981, ), 
                            registration_type = 'INVITATION/UNCLAIMED', 
                            short_address = 'Los Angels, CA', 
                            show_rating_banner = False, 
                            sponsor = dupr_backend.models.sponsor_logo_response.SponsorLogoResponse(
                                button_text = '', 
                                description = '', 
                                image_url = '', 
                                sponsor_popup_heading = '', 
                                sponsor_redirect_url = '', ), 
                            status = 'ACTIVE', 
                            substitution_details = [
                                dupr_backend.models.player_response.PlayerResponse(
                                    age = 55, 
                                    display_username = True, 
                                    distance = 'Nearby', 
                                    distance_in_miles = 15.4, 
                                    dupr_id = '8M2YEL', 
                                    email = 'user@exmaple.com', 
                                    enable_privacy = False, 
                                    first_name = 'John', 
                                    formatted_address = '5800 PA-378, Center Valley, PA 18034, United States', 
                                    full_name = 'John Doe', 
                                    gender = 'MALE', 
                                    hand = 'RIGHT', 
                                    id = 26518181881, 
                                    image_url = 'https://dupr-dev.s3.amazonaws.com/profile/image.png', 
                                    invited = True, 
                                    is_logged_in_user = False, 
                                    is_player1 = False, 
                                    is_substitute = True, 
                                    last_name = 'Doe', 
                                    latitude = 72.34654645455, 
                                    longitude = 19.55151584984, 
                                    lucra_connected = True, 
                                    partner_status = 'INVITED/CONFIRMED/NOT_CONFIRMED/CANCELLED', 
                                    phone = '+14445785789', 
                                    registered = True, 
                                    registration_details = dupr_backend.models.registration_response.RegistrationResponse(
                                        event_refunded_amount = 1.337, 
                                        is_participant1 = False, 
                                        is_wait_listed = False, 
                                        registration_id = 4684651981, ), 
                                    registration_type = 'INVITATION/UNCLAIMED', 
                                    short_address = 'Los Angels, CA', 
                                    show_rating_banner = False, 
                                    status = 'ACTIVE', 
                                    team_status = 'ACTIVE/INACTIVE', 
                                    username = 'X AE A-XII', 
                                    verified_email = False, )
                                ], 
                            team_status = 'ACTIVE/INACTIVE', 
                            username = 'X AE A-XII', 
                            verified_email = False, ), 
                        player2 = , 
                        registration_id = 56, 
                        team_status = 'ACTIVE', )
                    ], 
                limit = 10, 
                offset = 90, 
                total = 100, 
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO'
            )
        else :
            return PageOfLeagueTeamsResponse(
                empty = False,
                has_more = False,
                has_previous = True,
                limit = 10,
                offset = 90,
                total = 100,
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO',
        )
        """

    def testPageOfLeagueTeamsResponse(self):
        """Test PageOfLeagueTeamsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
