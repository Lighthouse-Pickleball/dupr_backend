# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.player_statistics_update_request import PlayerStatisticsUpdateRequest

class TestPlayerStatisticsUpdateRequest(unittest.TestCase):
    """PlayerStatisticsUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerStatisticsUpdateRequest:
        """Test PlayerStatisticsUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerStatisticsUpdateRequest`
        """
        model = PlayerStatisticsUpdateRequest()
        if include_optional:
            return PlayerStatisticsUpdateRequest(
                obfuscated_player_id = 1234,
                singles = dupr_backend.models.match_ratings.MatchRatings(
                    average_partner_dupr = 6.391, 
                    average_opponent_dupr = 3.254, 
                    average_points_won_percent = 0.67, 
                    half_life = 3.0, ),
                doubles = dupr_backend.models.match_ratings.MatchRatings(
                    average_partner_dupr = 6.391, 
                    average_opponent_dupr = 3.254, 
                    average_points_won_percent = 0.67, 
                    half_life = 3.0, )
            )
        else:
            return PlayerStatisticsUpdateRequest(
                obfuscated_player_id = 1234,
        )
        """

    def testPlayerStatisticsUpdateRequest(self):
        """Test PlayerStatisticsUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
