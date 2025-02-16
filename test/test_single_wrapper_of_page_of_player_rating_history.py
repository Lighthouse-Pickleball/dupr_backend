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
from dupr_backend.models.single_wrapper_of_page_of_player_rating_history import SingleWrapperOfPageOfPlayerRatingHistory  # noqa: E501
from dupr_backend.rest import ApiException

class TestSingleWrapperOfPageOfPlayerRatingHistory(unittest.TestCase):
    """SingleWrapperOfPageOfPlayerRatingHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SingleWrapperOfPageOfPlayerRatingHistory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfPageOfPlayerRatingHistory`
        """
        model = dupr_backend.models.single_wrapper_of_page_of_player_rating_history.SingleWrapperOfPageOfPlayerRatingHistory()  # noqa: E501
        if include_optional :
            return SingleWrapperOfPageOfPlayerRatingHistory(
                message = 'Show this message to user.', 
                result = dupr_backend.models.page_of_player_rating_history.PageOfPlayerRatingHistory(
                    empty = False, 
                    has_more = False, 
                    has_previous = True, 
                    hits = [
                        dupr_backend.models.player_rating_history.PlayerRatingHistory(
                            changed_by_admin = True, 
                            created = '', 
                            doubles = 1.337, 
                            doubles_provisional = True, 
                            match_date = '', 
                            rating_history_id = 56, 
                            singles = 1.337, 
                            singles_provisional = True, 
                            status = '', 
                            user_email = '', 
                            user_id = 56, 
                            user_name = '', )
                        ], 
                    limit = 10, 
                    offset = 90, 
                    total = 100, 
                    total_value_relation = 'GREATER_THAN_OR_EQUAL_TO', ), 
                status = 'FAILURE'
            )
        else :
            return SingleWrapperOfPageOfPlayerRatingHistory(
        )
        """

    def testSingleWrapperOfPageOfPlayerRatingHistory(self):
        """Test SingleWrapperOfPageOfPlayerRatingHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
