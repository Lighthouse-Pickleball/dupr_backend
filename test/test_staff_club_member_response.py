# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.staff_club_member_response import StaffClubMemberResponse

class TestStaffClubMemberResponse(unittest.TestCase):
    """StaffClubMemberResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StaffClubMemberResponse:
        """Test StaffClubMemberResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StaffClubMemberResponse`
        """
        model = StaffClubMemberResponse()
        if include_optional:
            return StaffClubMemberResponse(
                directors = [
                    dupr_backend.models.staff_club_member.StaffClubMember(
                        approval = 'APPROVED', 
                        club_id = 1231231, 
                        dupr_id = 'ALSJD1234', 
                        email = 'john@xyz.com', 
                        iso_alpha2_code = 'US', 
                        media_url = 'https://dupr-dev.s3.us-east-1.amazonaws.com/images/profile-e7718f70-d6a1-11eb-941a-09a499721974.png', 
                        name = 'John Doe', 
                        phone = '211564789', 
                        role_id = 1231231, 
                        user_id = 1231231, )
                    ],
                max_director_count = 56,
                max_organizer_count = 56,
                organizers = [
                    dupr_backend.models.staff_club_member.StaffClubMember(
                        approval = 'APPROVED', 
                        club_id = 1231231, 
                        dupr_id = 'ALSJD1234', 
                        email = 'john@xyz.com', 
                        iso_alpha2_code = 'US', 
                        media_url = 'https://dupr-dev.s3.us-east-1.amazonaws.com/images/profile-e7718f70-d6a1-11eb-941a-09a499721974.png', 
                        name = 'John Doe', 
                        phone = '211564789', 
                        role_id = 1231231, 
                        user_id = 1231231, )
                    ]
            )
        else:
            return StaffClubMemberResponse(
                directors = [
                    dupr_backend.models.staff_club_member.StaffClubMember(
                        approval = 'APPROVED', 
                        club_id = 1231231, 
                        dupr_id = 'ALSJD1234', 
                        email = 'john@xyz.com', 
                        iso_alpha2_code = 'US', 
                        media_url = 'https://dupr-dev.s3.us-east-1.amazonaws.com/images/profile-e7718f70-d6a1-11eb-941a-09a499721974.png', 
                        name = 'John Doe', 
                        phone = '211564789', 
                        role_id = 1231231, 
                        user_id = 1231231, )
                    ],
                max_director_count = 56,
                max_organizer_count = 56,
                organizers = [
                    dupr_backend.models.staff_club_member.StaffClubMember(
                        approval = 'APPROVED', 
                        club_id = 1231231, 
                        dupr_id = 'ALSJD1234', 
                        email = 'john@xyz.com', 
                        iso_alpha2_code = 'US', 
                        media_url = 'https://dupr-dev.s3.us-east-1.amazonaws.com/images/profile-e7718f70-d6a1-11eb-941a-09a499721974.png', 
                        name = 'John Doe', 
                        phone = '211564789', 
                        role_id = 1231231, 
                        user_id = 1231231, )
                    ],
        )
        """

    def testStaffClubMemberResponse(self):
        """Test StaffClubMemberResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
