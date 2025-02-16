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
from dupr_backend.models.page_of_club_response import PageOfClubResponse  # noqa: E501
from dupr_backend.rest import ApiException

class TestPageOfClubResponse(unittest.TestCase):
    """PageOfClubResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageOfClubResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageOfClubResponse`
        """
        model = dupr_backend.models.page_of_club_response.PageOfClubResponse()  # noqa: E501
        if include_optional :
            return PageOfClubResponse(
                empty = False, 
                has_more = False, 
                has_previous = True, 
                hits = [
                    dupr_backend.models.club_response.ClubResponse(
                        account_status = dupr_backend.models.account_status_response.AccountStatusResponse(
                            account_id = 6549864065, 
                            details_submitted = False, 
                            errors = [{code=invalid_street_address, reason=The provided street address cannot be found. Please verify the street name and number are correct in "111 Boulevard Street", requirement=individual.address.line1}], 
                            pending_requirement = False, ), 
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
                        attributes = dupr_backend.models.json_node.JsonNode(), 
                        club_id = 1231231, 
                        club_join_type = 'INVITATION', 
                        club_member_count = 12, 
                        club_name = 'Stillwater Pickleball', 
                        club_type = dupr_backend.models.club_type_response.ClubTypeResponse(
                            club_type = '<h1>header</h1>', 
                            club_type_id = 1231231, ), 
                        created = '', 
                        currency_details = dupr_backend.models.currency_details_response.CurrencyDetailsResponse(
                            currency_code = 'USD', 
                            currency_name = 'US Dollar', 
                            currency_symbol = '$', 
                            min_limit = 100.0, ), 
                        distance_in_miles = 254.0, 
                        is_payment_setup = True, 
                        long_description = dupr_backend.models.content_response.ContentResponse(
                            content = '<h1>content</h1>', 
                            content_id = 45785789, 
                            content_type = 'text/html', 
                            footer = '<h1>footer</h1>', 
                            footer_type = 'text/html', 
                            header = '<h1>header</h1>', 
                            header_type = 'text/html', ), 
                        manifest = dupr_backend.models.content_response.ContentResponse(
                            content = '<h1>content</h1>', 
                            content_id = 45785789, 
                            content_type = 'text/html', 
                            footer = '<h1>footer</h1>', 
                            footer_type = 'text/html', 
                            header = '<h1>header</h1>', 
                            header_type = 'text/html', ), 
                        media_url = '4684651981', 
                        model_type = 'ABSOLUTE', 
                        model_value = 1.337, 
                        pending_request_list = [1231231, 1231232, 1231233], 
                        requested_by = 56, 
                        role = dupr_backend.models.club_role_response.ClubRoleResponse(
                            role_id = 56, ), 
                        short_address = 'Miami-Dade County, FL, US', 
                        short_description = , )
                    ], 
                limit = 10, 
                offset = 90, 
                total = 100, 
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO'
            )
        else :
            return PageOfClubResponse(
                empty = False,
                has_more = False,
                has_previous = True,
                limit = 10,
                offset = 90,
                total = 100,
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO',
        )
        """

    def testPageOfClubResponse(self):
        """Test PageOfClubResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
