# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.club_match_filters import ClubMatchFilters

class TestClubMatchFilters(unittest.TestCase):
    """ClubMatchFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClubMatchFilters:
        """Test ClubMatchFilters
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClubMatchFilters`
        """
        model = ClubMatchFilters()
        if include_optional:
            return ClubMatchFilters(
                event_format = ['SINGLES','DOUBLES'],
                event_date = YYYY-MM-DD,
                event_name = 'Pickle ball',
                player_id = 215254148
            )
        else:
            return ClubMatchFilters(
        )
        """

    def testClubMatchFilters(self):
        """Test ClubMatchFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
