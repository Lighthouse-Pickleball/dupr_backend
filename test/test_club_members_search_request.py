# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.club_members_search_request import ClubMembersSearchRequest

class TestClubMembersSearchRequest(unittest.TestCase):
    """ClubMembersSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClubMembersSearchRequest:
        """Test ClubMembersSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClubMembersSearchRequest`
        """
        model = ClubMembersSearchRequest()
        if include_optional:
            return ClubMembersSearchRequest(
                exclude = [7828935307],
                filter = dupr_backend.models.club_members_search_filter.ClubMembersSearchFilter(
                    age = dupr_backend.models.club_members_age_filter.ClubMembersAgeFilter(
                        max_age = 25.0, 
                        min_age = 18.0, ), 
                    club_invitation_type = [INVITATION, REQUEST], 
                    gender = 'MALE', 
                    lat = 72.34654645455, 
                    lng = 19.55151584984, 
                    radius_in_meters = 16093.4, 
                    rating = dupr_backend.models.club_members_rating_filter.ClubMembersRatingFilter(
                        category = 'DUPR/PROVISIONAL', 
                        doubles = dupr_backend.models.club_members_rating_range.ClubMembersRatingRange(
                            max_rating = 3.3, 
                            min_rating = 2.3, ), 
                        singles = dupr_backend.models.club_members_rating_range.ClubMembersRatingRange(
                            max_rating = 3.3, 
                            min_rating = 2.3, ), ), 
                    status = 'ACTIVE', ),
                include_pending_players = True,
                include_staff = True,
                limit = 10,
                offset = 0,
                query = '*',
                sort = dupr_backend.models.club_members_search_sort.ClubMembersSearchSort(
                    order = 'ASC/DESC', 
                    parameter = 'fullNameSort/doubles/doublesVerified/singles/singlesVerified/created', )
            )
        else:
            return ClubMembersSearchRequest(
                limit = 10,
                offset = 0,
                query = '*',
        )
        """

    def testClubMembersSearchRequest(self):
        """Test ClubMembersSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
