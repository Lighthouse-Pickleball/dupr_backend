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
from dupr_backend.models.match_round_res import MatchRoundRes  # noqa: E501
from dupr_backend.rest import ApiException

class TestMatchRoundRes(unittest.TestCase):
    """MatchRoundRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MatchRoundRes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchRoundRes`
        """
        model = dupr_backend.models.match_round_res.MatchRoundRes()  # noqa: E501
        if include_optional :
            return MatchRoundRes(
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                matches = [
                    dupr_backend.models.seed_match_res.SeedMatchRes(
                        bye = True, 
                        match_serial = 1, 
                        serial = 1, 
                        team1 = dupr_backend.models.league_teams_res.LeagueTeamsRes(
                            partner_status = 'ACTIVE', 
                            payment_status = 'ACTIVE', 
                            player1 = dupr_backend.models.player_res.PlayerRes(
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
                                sponsor = dupr_backend.models.sponsor_res.SponsorRes(
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
                            player2 = dupr_backend.models.player_res.PlayerRes(
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
                        team2 = dupr_backend.models.league_teams_res.LeagueTeamsRes(
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
            return MatchRoundRes(
                matches = [
                    dupr_backend.models.seed_match_res.SeedMatchRes(
                        bye = True, 
                        match_serial = 1, 
                        serial = 1, 
                        team1 = dupr_backend.models.league_teams_res.LeagueTeamsRes(
                            partner_status = 'ACTIVE', 
                            payment_status = 'ACTIVE', 
                            player1 = dupr_backend.models.player_res.PlayerRes(
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
                                sponsor = dupr_backend.models.sponsor_res.SponsorRes(
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
                            player2 = dupr_backend.models.player_res.PlayerRes(
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
                        team2 = dupr_backend.models.league_teams_res.LeagueTeamsRes(
                            partner_status = 'ACTIVE', 
                            payment_status = 'ACTIVE', 
                            registration_id = 56, 
                            team_status = 'ACTIVE', ), )
                    ],
                serial = 1,
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testMatchRoundRes(self):
        """Test MatchRoundRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
