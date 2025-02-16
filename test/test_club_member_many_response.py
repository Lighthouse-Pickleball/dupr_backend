# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.club_member_many_response import ClubMemberManyResponse

class TestClubMemberManyResponse(unittest.TestCase):
    """ClubMemberManyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClubMemberManyResponse:
        """Test ClubMemberManyResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClubMemberManyResponse`
        """
        model = ClubMemberManyResponse()
        if include_optional:
            return ClubMemberManyResponse(
                add_members_action_s3_url = 'https://dupr-dev.s3.amazonaws.com/clubs-members-excel/312312-2021-09-11',
                in_valid_email = [dupr@gmail.com],
                invalid_email = 56,
                players_added = 56,
                players_invited = 56,
                valid_email = [dupr@gmail.com]
            )
        else:
            return ClubMemberManyResponse(
                invalid_email = 56,
                players_added = 56,
                players_invited = 56,
        )
        """

    def testClubMemberManyResponse(self):
        """Test ClubMemberManyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
