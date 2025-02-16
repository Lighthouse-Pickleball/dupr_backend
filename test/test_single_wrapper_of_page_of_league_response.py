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
from dupr_backend.models.single_wrapper_of_page_of_league_response import SingleWrapperOfPageOfLeagueResponse  # noqa: E501
from dupr_backend.rest import ApiException

class TestSingleWrapperOfPageOfLeagueResponse(unittest.TestCase):
    """SingleWrapperOfPageOfLeagueResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SingleWrapperOfPageOfLeagueResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfPageOfLeagueResponse`
        """
        model = dupr_backend.models.single_wrapper_of_page_of_league_response.SingleWrapperOfPageOfLeagueResponse()  # noqa: E501
        if include_optional :
            return SingleWrapperOfPageOfLeagueResponse(
                message = 'Show this message to user.', 
                result = dupr_backend.models.page_of_league_response.PageOfLeagueResponse(
                    empty = False, 
                    has_more = False, 
                    has_previous = True, 
                    hits = [
                        dupr_backend.models.league_response.LeagueResponse(
                            additional_information = dupr_backend.models.league_content_response.LeagueContentResponse(
                                content = '<h1>content</h1>', 
                                content_id = 45785789, 
                                content_type = 'text/html', 
                                footer = '<h1>footer</h1>', 
                                footer_type = 'text/html', 
                                header = '<h1>header</h1>', 
                                header_type = 'text/html', ), 
                            address = dupr_backend.models.address_response.AddressResponse(
                                address_line = 'Apartment, Room, PO Box numbers (optional)', 
                                create = '', 
                                formatted_address = '5800 PA-378, Center Valley, PA 18034, United States', 
                                id = 12385789, 
                                latitude = 33.194791, 
                                longitude = -117.048582, 
                                place_id = '', 
                                precision = '', 
                                short_address = 'Center Valley, PA, US', 
                                status = '', 
                                types = '', ), 
                            age_string = '20 - 30', 
                            attributes = {"additionalProp1":{"children":{},"comment":"Contact person name, if provided.","value":"String"}}, 
                            brackets = [
                                dupr_backend.models.bracket_response.BracketResponse(
                                    age_bracket = [27, 35], 
                                    bracket_id = 4684651981, 
                                    can_show_standings = False, 
                                    club_id = 45785789, 
                                    club_name = 'Stillwater Pickleball', 
                                    contact_details = [
                                        dupr_backend.models.league_contact_detail_response.LeagueContactDetailResponse(
                                            email = 'hisenberg@yopmail.com', 
                                            name = 'Dreamland pickalball', 
                                            phone = '18022214966', 
                                            priority = 1, 
                                            type = 'person/club', )
                                        ], 
                                    courts = 5, 
                                    currency_details = dupr_backend.models.currency_details_response.CurrencyDetailsResponse(
                                        currency_code = 'USD', 
                                        currency_name = 'US Dollar', 
                                        currency_symbol = '$', 
                                        min_limit = 100.0, ), 
                                    custom_code = 'BRACKET123', 
                                    description = dupr_backend.models.league_content_response.LeagueContentResponse(
                                        content = '<h1>content</h1>', 
                                        content_id = 45785789, 
                                        content_type = 'text/html', 
                                        footer = '<h1>footer</h1>', 
                                        footer_type = 'text/html', 
                                        header = '<h1>header</h1>', 
                                        header_type = 'text/html', ), 
                                    display_status = 'Draft/Upcoming/Open/Ongoing', 
                                    draw_impacted = False, 
                                    duration = [yyyy-mm-dd, yyyy-mm-dd], 
                                    duration_date_time = [yyyy-mm-ddTHH:mm:ss, yyyy-mm-ddTHH:mm:ss], 
                                    duration_status = 'IN_PROGRESS/UPCOMING', 
                                    elimination = 'SINGLE/DOUBLE/DOUBLE_PREVENTED/ROUND_ROBIN', 
                                    format = 'SINGLES/DOUBLES', 
                                    has_confirm_match = False, 
                                    has_queue = False, 
                                    is_match_seeded = True, 
                                    is_player_eligible = False, 
                                    is_queue_complete = False, 
                                    is_registered = False, 
                                    is_wait_list_full = False, 
                                    league_address = dupr_backend.models.address_response.AddressResponse(
                                        address_line = 'Apartment, Room, PO Box numbers (optional)', 
                                        create = '', 
                                        formatted_address = '5800 PA-378, Center Valley, PA 18034, United States', 
                                        id = 12385789, 
                                        latitude = 33.194791, 
                                        longitude = -117.048582, 
                                        place_id = '', 
                                        precision = '', 
                                        short_address = 'Center Valley, PA, US', 
                                        status = '', 
                                        types = '', ), 
                                    league_id = 4684651981, 
                                    league_name = 'Stillwater Pickleball', 
                                    match_bonus_points = 8.0, 
                                    max_team = 500, 
                                    media_url = 'www.url.com/image.jpg', 
                                    member_fee = 500.0, 
                                    name = 'Stillwater Pickleball', 
                                    non_member_fee = 500.0, 
                                    payment_details = dupr_backend.models.payment_details_response.PaymentDetailsResponse(
                                        amount_paid = 100.0, 
                                        event_fee = 1.337, 
                                        is_club_member = True, 
                                        is_registered = True, 
                                        is_wait_listed = True, 
                                        payment_capture = True, 
                                        payment_status = 'ACTIVE', 
                                        player_status = 'ACTIVE', 
                                        refunded_amount = 10.0, ), 
                                    payment_status = 'ACTIVE', 
                                    player_group = 'MEN/WOMEN/MIXED/COED', 
                                    rating_bracket = [3.1, 4.5], 
                                    reg_user_id = 56, 
                                    registered_members = 56, 
                                    registration_date = [yyyy-mm-dd, yyyy-mm-dd], 
                                    registration_date_time = [yyyy-mm-ddTHH:mm:ss, yyyy-mm-ddTHH:mm:ss], 
                                    registration_details = dupr_backend.models.registration_response.RegistrationResponse(
                                        event_refunded_amount = 1.337, 
                                        is_participant1 = False, 
                                        is_wait_listed = False, 
                                        player1 = dupr_backend.models.participant.Participant(
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
                                    registration_status = 'OPEN/CLOSED', 
                                    score_format = '1', 
                                    score_format_id = 4684651981, 
                                    status = 'ACTIVE/IN_PROGRESS/COMPLETE/CANCELLED', 
                                    time_zone = 'IST', 
                                    total_rounds = 1, 
                                    wait_list = 500, 
                                    zone_name = 'IST', )
                                ], 
                            can_show_standings = False, 
                            club_id = 45785789, 
                            club_name = 'Stillwater Pickleball', 
                            contact_details = [
                                dupr_backend.models.league_contact_detail_response.LeagueContactDetailResponse(
                                    email = 'hisenberg@yopmail.com', 
                                    name = 'Dreamland pickalball', 
                                    phone = '18022214966', 
                                    priority = 1, 
                                    type = 'person/club', )
                                ], 
                            currency_details = dupr_backend.models.currency_details_response.CurrencyDetailsResponse(
                                currency_code = 'USD', 
                                currency_name = 'US Dollar', 
                                currency_symbol = '$', 
                                min_limit = 100.0, ), 
                            display_status = 'Draft/Upcoming/Open/Ongoing', 
                            distance = 'Nearby', 
                            distance_in_miles = 15.4, 
                            duration = [yyyy-mm-dd, yyyy-mm-dd], 
                            duration_date_time = [yyyy-mm-ddTHH:mm:ss, yyyy-mm-ddTHH:mm:ss], 
                            duration_date_time_utc = [yyyy-mm-ddTHH:mm:ss, yyyy-mm-ddTHH:mm:ss], 
                            duration_status = 'IN_PROGRESS/UPCOMING/COMPLETE', 
                            duration_string = '2021-11-07 - 2021-11-08', 
                            elimination_string = 'ROUND_ROBIN', 
                            end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            event_format_string = 'SINGLES,DOUBLES', 
                            is_registered = True, 
                            league_id = 45785789, 
                            league_name = 'Stillwater Pickleball', 
                            league_price = '$40 - $50', 
                            liability_waiver_id = 45785789, 
                            liability_waiver_url = 'www.url.com/doc.pdf', 
                            long_description = , 
                            media_id = 45785789, 
                            media_url = 'www.url.com/image.jpg', 
                            member_fee = 500.0, 
                            membership_permission = 'OPEN_TO_ALL/CLUB_MEMBERS', 
                            non_member_fee = 500.0, 
                            player_group = 'MEN,MIXED', 
                            refund_policy = , 
                            registered_members = 56, 
                            registration_date = [yyyy-mm-dd, yyyy-mm-dd], 
                            registration_date_time = [yyyy-mm-ddTHH:mm:ss, yyyy-mm-ddTHH:mm:ss], 
                            registration_date_time_utc = [yyyy-mm-ddTHH:mm:ss, yyyy-mm-ddTHH:mm:ss], 
                            registration_status = 'OPEN/CLOSED', 
                            registration_string = '2021-11-07 - 2021-11-08', 
                            registration_url = 'https://mydupr.com/register', 
                            safety_policy = , 
                            short_address = 'Miami-Dade County, FL, US', 
                            short_description = , 
                            skill_level = 'DUPR 3 - 4', 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            status = 'ACTIVE/IN_PROGRESS/COMPLETE/CANCELLED', 
                            type = 'FLEX', 
                            user_id = 45785789, )
                        ], 
                    limit = 10, 
                    offset = 90, 
                    total = 100, 
                    total_value_relation = 'GREATER_THAN_OR_EQUAL_TO', ), 
                status = 'FAILURE'
            )
        else :
            return SingleWrapperOfPageOfLeagueResponse(
        )
        """

    def testSingleWrapperOfPageOfLeagueResponse(self):
        """Test SingleWrapperOfPageOfLeagueResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
