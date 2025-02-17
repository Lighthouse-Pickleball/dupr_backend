# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.match_ratings import MatchRatings

class TestMatchRatings(unittest.TestCase):
    """MatchRatings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatchRatings:
        """Test MatchRatings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchRatings`
        """
        model = MatchRatings()
        if include_optional:
            return MatchRatings(
                average_opponent_dupr = '3.254',
                average_partner_dupr = '6.391',
                average_points_won_percent = '67%',
                half_life = '3.0',
                losses = 12,
                wins = 4
            )
        else:
            return MatchRatings(
        )
        """

    def testMatchRatings(self):
        """Test MatchRatings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
