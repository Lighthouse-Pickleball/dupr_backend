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
from dupr_backend.models.single_wrapper_of_page_of_user_lookup_response import SingleWrapperOfPageOfUserLookupResponse  # noqa: E501
from dupr_backend.rest import ApiException

class TestSingleWrapperOfPageOfUserLookupResponse(unittest.TestCase):
    """SingleWrapperOfPageOfUserLookupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SingleWrapperOfPageOfUserLookupResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfPageOfUserLookupResponse`
        """
        model = dupr_backend.models.single_wrapper_of_page_of_user_lookup_response.SingleWrapperOfPageOfUserLookupResponse()  # noqa: E501
        if include_optional :
            return SingleWrapperOfPageOfUserLookupResponse(
                message = 'Show this message to user.', 
                result = dupr_backend.models.page_of_user_lookup_response.PageOfUserLookupResponse(
                    empty = False, 
                    has_more = False, 
                    has_previous = True, 
                    hits = [
                        dupr_backend.models.user_lookup_response.UserLookupResponse(
                            birthdate = 'Tue Jan 12 19:00:00 EST 2021', 
                            created = '2021-01-13 01:01:01', 
                            email = 'john@qwe.com', 
                            external_id = 'C12345', 
                            full_name = 'John Die', 
                            gender = 'MALE', 
                            hand = 'LEFT', 
                            id = 26518181881, 
                            image_url = 'https://s3.aws.com/image.png', 
                            is_valid_email = True, 
                            is_valid_phone = True, 
                            phone_number = '+18938271', 
                            referral_code = 'ACASC', 
                            registered = False, 
                            restricted = False, 
                            role = dupr_backend.models.role_response.RoleResponse(
                                id = 424255123, 
                                permissions = {"USER":["VIEW","MODIFY"],"TOURNAMENT":["OWN_VIEW","OWN_MODIFY","OWN_DELETE"]}, 
                                role = 'PLAYER', ), 
                            status = 'ACTIVE', )
                        ], 
                    limit = 10, 
                    offset = 90, 
                    total = 100, 
                    total_value_relation = 'GREATER_THAN_OR_EQUAL_TO', ), 
                status = 'FAILURE'
            )
        else :
            return SingleWrapperOfPageOfUserLookupResponse(
        )
        """

    def testSingleWrapperOfPageOfUserLookupResponse(self):
        """Test SingleWrapperOfPageOfUserLookupResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
