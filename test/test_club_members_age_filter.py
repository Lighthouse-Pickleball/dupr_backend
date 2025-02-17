# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.club_members_age_filter import ClubMembersAgeFilter

class TestClubMembersAgeFilter(unittest.TestCase):
    """ClubMembersAgeFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClubMembersAgeFilter:
        """Test ClubMembersAgeFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClubMembersAgeFilter`
        """
        model = ClubMembersAgeFilter()
        if include_optional:
            return ClubMembersAgeFilter(
                max_age = 25.0,
                min_age = 18.0
            )
        else:
            return ClubMembersAgeFilter(
        )
        """

    def testClubMembersAgeFilter(self):
        """Test ClubMembersAgeFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
