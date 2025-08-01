# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.match_search_request import MatchSearchRequest

class TestMatchSearchRequest(unittest.TestCase):
    """MatchSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatchSearchRequest:
        """Test MatchSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchSearchRequest`
        """
        model = MatchSearchRequest()
        if include_optional:
            return MatchSearchRequest(
                offset = 0,
                limit = 3,
                filters = dupr_backend.models.match_filters.MatchFilters(
                    event_format = ['SINGLES','DOUBLES'], 
                    match_status = ['COMPLETE','PENDING'], 
                    event_date = yyyy-MM-dd, 
                    event_name = 'Pickle ball', 
                    player_id = 215254148, ),
                sort = dupr_backend.models.match_sort.MatchSort(
                    parameter = 'MATCH_DATE/CREATED_DATE/MODIFIED_DATE', 
                    order = 'ASC/DESC', )
            )
        else:
            return MatchSearchRequest(
                offset = 0,
                limit = 3,
        )
        """

    def testMatchSearchRequest(self):
        """Test MatchSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
