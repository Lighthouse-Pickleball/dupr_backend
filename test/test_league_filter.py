# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.league_filter import LeagueFilter

class TestLeagueFilter(unittest.TestCase):
    """LeagueFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeagueFilter:
        """Test LeagueFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeagueFilter`
        """
        model = LeagueFilter()
        if include_optional:
            return LeagueFilter(
                city = [San Francisco, Great Falls],
                duration_status = [COMPLETE, IN_PROGRESS, UPCOMING],
                elimination = [DOUBLE_PREVENTED, ROUND_ROBIN],
                event_format = [SINGLES, DOUBLES],
                player_group = [MEN, WOMEN, MIXED],
                registration_status = [OPEN, NOT_STARTED, CLOSED],
                skill_level = dupr_backend.models.skill_level_filter.SkillLevelFilter(
                    max_rating = 4.2, 
                    min_rating = 3.2, ),
                status = [ACTIVE, IN_ACTIVE]
            )
        else:
            return LeagueFilter(
        )
        """

    def testLeagueFilter(self):
        """Test LeagueFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
