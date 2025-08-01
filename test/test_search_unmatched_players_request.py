# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.search_unmatched_players_request import SearchUnmatchedPlayersRequest

class TestSearchUnmatchedPlayersRequest(unittest.TestCase):
    """SearchUnmatchedPlayersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchUnmatchedPlayersRequest:
        """Test SearchUnmatchedPlayersRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchUnmatchedPlayersRequest`
        """
        model = SearchUnmatchedPlayersRequest()
        if include_optional:
            return SearchUnmatchedPlayersRequest(
                offset = 0,
                limit = 10,
                query = '*',
                bracket_id = 7828935307,
                sort = dupr_backend.models.bracket_team_sort.BracketTeamSort(
                    parameter = 'RATINGS', 
                    order = 'ASC/DESC', )
            )
        else:
            return SearchUnmatchedPlayersRequest(
                offset = 0,
                limit = 10,
                bracket_id = 7828935307,
        )
        """

    def testSearchUnmatchedPlayersRequest(self):
        """Test SearchUnmatchedPlayersRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
