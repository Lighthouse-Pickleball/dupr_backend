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
from dupr_backend.models.match_round_req import MatchRoundReq  # noqa: E501
from dupr_backend.rest import ApiException

class TestMatchRoundReq(unittest.TestCase):
    """MatchRoundReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MatchRoundReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchRoundReq`
        """
        model = dupr_backend.models.match_round_req.MatchRoundReq()  # noqa: E501
        if include_optional :
            return MatchRoundReq(
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                matches = [
                    dupr_backend.models.seed_match_req.SeedMatchReq(
                        bye = True, 
                        match_serial = 1, 
                        serial = 1, 
                        team1 = dupr_backend.models.league_teams_req.LeagueTeamsReq(
                            partner_status = 'ACTIVE', 
                            payment_status = 'ACTIVE', 
                            player1 = dupr_backend.models.player_req.PlayerReq(
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
                                sponsor = dupr_backend.models.sponsor_req.SponsorReq(
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
                            player2 = dupr_backend.models.player_req.PlayerReq(
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
                            registration_id = 56, 
                            team_status = 'ACTIVE', ), 
                        team2 = dupr_backend.models.league_teams_req.LeagueTeamsReq(
                            partner_status = 'ACTIVE', 
                            payment_status = 'ACTIVE', 
                            registration_id = 56, 
                            team_status = 'ACTIVE', ), )
                    ], 
                serial = 1, 
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                team_ids = [9989596696]
            )
        else :
            return MatchRoundReq(
                matches = [
                    dupr_backend.models.seed_match_req.SeedMatchReq(
                        bye = True, 
                        match_serial = 1, 
                        serial = 1, 
                        team1 = dupr_backend.models.league_teams_req.LeagueTeamsReq(
                            partner_status = 'ACTIVE', 
                            payment_status = 'ACTIVE', 
                            player1 = dupr_backend.models.player_req.PlayerReq(
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
                                sponsor = dupr_backend.models.sponsor_req.SponsorReq(
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
                            player2 = dupr_backend.models.player_req.PlayerReq(
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
                            registration_id = 56, 
                            team_status = 'ACTIVE', ), 
                        team2 = dupr_backend.models.league_teams_req.LeagueTeamsReq(
                            partner_status = 'ACTIVE', 
                            payment_status = 'ACTIVE', 
                            registration_id = 56, 
                            team_status = 'ACTIVE', ), )
                    ],
                serial = 1,
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testMatchRoundReq(self):
        """Test MatchRoundReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
