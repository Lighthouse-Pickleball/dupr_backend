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
from dupr_backend.models.single_wrapper_of_bracket_club_role_response import SingleWrapperOfBracketClubRoleResponse  # noqa: E501
from dupr_backend.rest import ApiException

class TestSingleWrapperOfBracketClubRoleResponse(unittest.TestCase):
    """SingleWrapperOfBracketClubRoleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SingleWrapperOfBracketClubRoleResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfBracketClubRoleResponse`
        """
        model = dupr_backend.models.single_wrapper_of_bracket_club_role_response.SingleWrapperOfBracketClubRoleResponse()  # noqa: E501
        if include_optional :
            return SingleWrapperOfBracketClubRoleResponse(
                message = 'Show this message to user.', 
                result = dupr_backend.models.bracket_club_role_response.BracketClubRoleResponse(
                    is_club_member = True, 
                    role_id = 45785789, 
                    role_name = 'ADMIN', ), 
                status = 'FAILURE'
            )
        else :
            return SingleWrapperOfBracketClubRoleResponse(
        )
        """

    def testSingleWrapperOfBracketClubRoleResponse(self):
        """Test SingleWrapperOfBracketClubRoleResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
