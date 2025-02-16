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
from dupr_backend.models.bracket_request import BracketRequest  # noqa: E501
from dupr_backend.rest import ApiException

class TestBracketRequest(unittest.TestCase):
    """BracketRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BracketRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BracketRequest`
        """
        model = dupr_backend.models.bracket_request.BracketRequest()  # noqa: E501
        if include_optional :
            return BracketRequest(
                age_bracket = [27, 35], 
                bracket_id = 45785789, 
                courts = 5, 
                custom_code = 'BRACKET123', 
                description = dupr_backend.models.league_content_request.LeagueContentRequest(
                    content = '<h1>content</h1>', 
                    content_id = 45785789, 
                    content_type = 'text/html', 
                    footer = '<h1>footer</h1>', 
                    footer_type = 'text/html', 
                    header = '<h1>header</h1>', 
                    header_type = 'text/html', ), 
                duration = [yyyy-mm-dd, yyyy-mm-dd], 
                duration_date_time = [yyyy-mm-ddTHH:mm:ss, yyyy-mm-ddTHH:mm:ss], 
                elimination = 'SINGLE/DOUBLE/DOUBLE_PREVENTED/ROUND_ROBIN', 
                format = 'SINGLES/DOUBLES', 
                league_id = 4684651981, 
                match_bonus_points = 8.0, 
                max_team = 500, 
                member_fee = 500.0, 
                name = 'Stillwater Pickleball', 
                non_member_fee = 500.0, 
                player_group = 'MEN/WOMEN/MIXED/COED', 
                rating_bracket = [3.1, 4.5], 
                registration_date = [yyyy-mm-dd, yyyy-mm-dd], 
                registration_date_time = [yyyy-mm-ddTHH:mm:ss, yyyy-mm-ddTHH:mm:ss], 
                score_format = 1, 
                time_zone = 'IST', 
                wait_list = 500, 
                zone_name = 'IST'
            )
        else :
            return BracketRequest(
                bracket_id = 45785789,
                duration = [yyyy-mm-dd, yyyy-mm-dd],
                elimination = 'SINGLE/DOUBLE/DOUBLE_PREVENTED/ROUND_ROBIN',
                format = 'SINGLES/DOUBLES',
                player_group = 'MEN/WOMEN/MIXED/COED',
                score_format = 1,
                wait_list = 500,
        )
        """

    def testBracketRequest(self):
        """Test BracketRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
