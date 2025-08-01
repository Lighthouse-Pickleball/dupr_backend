# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.array_wrapper_league_teams_response import ArrayWrapperLeagueTeamsResponse

class TestArrayWrapperLeagueTeamsResponse(unittest.TestCase):
    """ArrayWrapperLeagueTeamsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayWrapperLeagueTeamsResponse:
        """Test ArrayWrapperLeagueTeamsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayWrapperLeagueTeamsResponse`
        """
        model = ArrayWrapperLeagueTeamsResponse()
        if include_optional:
            return ArrayWrapperLeagueTeamsResponse(
                status = 'SUCCESS',
                message = 'Show this message to user.',
                results = [
                    dupr_backend.models.league_teams_response.LeagueTeamsResponse(
                        registration_id = 56, 
                        player1 = dupr_backend.models.player_response.PlayerResponse(
                            id = 26518181881, 
                            full_name = 'John Doe', 
                            first_name = 'John', 
                            last_name = 'Doe', 
                            username = 'X AE A-XII', 
                            display_username = True, 
                            short_address = 'Los Angels, CA', 
                            formatted_address = '5800', 
                            latitude = 72.34654645455, 
                            longitude = 19.55151584984, 
                            gender = 'MALE', 
                            age = 55, 
                            hand = 'RIGHT', 
                            image_url = 'https://dupr-dev.s3.amazonaws.com/profile/image.png', 
                            ratings = dupr_backend.models.player_rating_response.PlayerRatingResponse(
                                singles = '4.125', 
                                singles_verified = '4.1', 
                                singles_provisional = True, 
                                singles_reliability_score = 10, 
                                doubles = '2.864', 
                                doubles_verified = '2.75', 
                                doubles_provisional = True, 
                                doubles_reliability_score = 10, 
                                default_rating = 'DOUBLES', 
                                provisional_ratings = dupr_backend.models.provisional_rating.ProvisionalRating(
                                    singles_rating = 3.5, 
                                    doubles_rating = 3.5, 
                                    coach = { id: 12345, metadata: { name: example }}, ), ), 
                            invited = True, 
                            distance = 'Nearby', 
                            enable_privacy = False, 
                            distance_in_miles = 15.4, 
                            is_logged_in_user = True, 
                            partner_status = 'INVITED/CONFIRMED/NOT_CONFIRMED/CANCELLED', 
                            team_status = 'ACTIVE/INACTIVE', 
                            is_player1 = True, 
                            registration_details = user@exmaple.com, 
                            phone = '+14445785789', 
                            email = 'user@exmaple.com', 
                            verified_email = True, 
                            registration_type = 'INVITATION/UNCLAIMED', 
                            registered = True, 
                            dupr_id = '8M2YEL', 
                            show_rating_banner = True, 
                            status = 'ACTIVE', 
                            sponsor = dupr_backend.models.sponsor_logo_response.SponsorLogoResponse(
                                image_url = '', 
                                sponsor_redirect_url = '', 
                                sponsor_popup_heading = '', 
                                description = '', 
                                button_text = '', ), 
                            substitution_details = [
                                dupr_backend.models.player_response.PlayerResponse(
                                    id = 26518181881, 
                                    full_name = 'John Doe', 
                                    first_name = 'John', 
                                    last_name = 'Doe', 
                                    username = 'X AE A-XII', 
                                    display_username = True, 
                                    short_address = 'Los Angels, CA', 
                                    formatted_address = '5800', 
                                    latitude = 72.34654645455, 
                                    longitude = 19.55151584984, 
                                    gender = 'MALE', 
                                    age = 55, 
                                    hand = 'RIGHT', 
                                    image_url = 'https://dupr-dev.s3.amazonaws.com/profile/image.png', 
                                    invited = True, 
                                    distance = 'Nearby', 
                                    enable_privacy = False, 
                                    distance_in_miles = 15.4, 
                                    is_logged_in_user = True, 
                                    partner_status = 'INVITED/CONFIRMED/NOT_CONFIRMED/CANCELLED', 
                                    team_status = 'ACTIVE/INACTIVE', 
                                    is_player1 = True, 
                                    registration_details = user@exmaple.com, 
                                    phone = '+14445785789', 
                                    email = 'user@exmaple.com', 
                                    verified_email = True, 
                                    registration_type = 'INVITATION/UNCLAIMED', 
                                    registered = True, 
                                    dupr_id = '8M2YEL', 
                                    show_rating_banner = True, 
                                    status = 'ACTIVE', 
                                    is_substitute = True, 
                                    lucra_connected = True, 
                                    substitute = True, )
                                ], 
                            is_substitute = True, 
                            lucra_connected = True, 
                            substitute = True, ), 
                        player2 = , 
                        team_status = 'ACTIVE', 
                        partner_status = 'ACTIVE', )
                    ]
            )
        else:
            return ArrayWrapperLeagueTeamsResponse(
        )
        """

    def testArrayWrapperLeagueTeamsResponse(self):
        """Test ArrayWrapperLeagueTeamsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
