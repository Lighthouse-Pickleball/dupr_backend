# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.array_wrapper_club_listing_response import ArrayWrapperClubListingResponse

class TestArrayWrapperClubListingResponse(unittest.TestCase):
    """ArrayWrapperClubListingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayWrapperClubListingResponse:
        """Test ArrayWrapperClubListingResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayWrapperClubListingResponse`
        """
        model = ArrayWrapperClubListingResponse()
        if include_optional:
            return ArrayWrapperClubListingResponse(
                status = 'SUCCESS',
                message = 'Show this message to user.',
                results = [
                    dupr_backend.models.club_listing_response.ClubListingResponse(
                        club_id = 1231231, 
                        club_name = 'Stillwater Pickleball', 
                        media_url = '4684651981', 
                        short_address = 'Miami-Dade County, FL, US', 
                        club_member_count = 12, 
                        created = '2020-03-04T17:21:16.000Z', 
                        role = dupr_backend.models.club_role_response.ClubRoleResponse(
                            role_id = 56, 
                            role = '', ), )
                    ]
            )
        else:
            return ArrayWrapperClubListingResponse(
        )
        """

    def testArrayWrapperClubListingResponse(self):
        """Test ArrayWrapperClubListingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
