# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import dupr_backend
from dupr_backend.models.bracket_team_sort import BracketTeamSort  # noqa: E501
from dupr_backend.rest import ApiException

class TestBracketTeamSort(unittest.TestCase):
    """BracketTeamSort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BracketTeamSort
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BracketTeamSort`
        """
        model = dupr_backend.models.bracket_team_sort.BracketTeamSort()  # noqa: E501
        if include_optional :
            return BracketTeamSort(
                order = 'ASC/DESC', 
                parameter = 'RATINGS'
            )
        else :
            return BracketTeamSort(
        )
        """

    def testBracketTeamSort(self):
        """Test BracketTeamSort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
