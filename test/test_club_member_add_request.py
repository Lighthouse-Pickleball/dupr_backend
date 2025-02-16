# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.club_member_add_request import ClubMemberAddRequest

class TestClubMemberAddRequest(unittest.TestCase):
    """ClubMemberAddRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClubMemberAddRequest:
        """Test ClubMemberAddRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClubMemberAddRequest`
        """
        model = ClubMemberAddRequest()
        if include_optional:
            return ClubMemberAddRequest(
                add_members = [
                    dupr_backend.models.member_request.MemberRequest(
                        email = 'john@yopmail.com', 
                        full_name = 'John Doe', )
                    ]
            )
        else:
            return ClubMemberAddRequest(
                add_members = [
                    dupr_backend.models.member_request.MemberRequest(
                        email = 'john@yopmail.com', 
                        full_name = 'John Doe', )
                    ],
        )
        """

    def testClubMemberAddRequest(self):
        """Test ClubMemberAddRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
