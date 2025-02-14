# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs  # noqa: E501

    OpenAPI spec version: v1.0 alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import dupr_backend
from dupr_backend.api.mi_lp_events_api import MiLPEventsApi  # noqa: E501
from dupr_backend.rest import ApiException


class TestMiLPEventsApi(unittest.TestCase):
    """MiLPEventsApi unit test stubs"""

    def setUp(self):
        self.api = MiLPEventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_event_info_using_get(self):
        """Test case for get_event_info_using_get

        getEventInfo  # noqa: E501
        """
        pass

    def test_get_teams_using_get(self):
        """Test case for get_teams_using_get

        getTeams  # noqa: E501
        """
        pass

    def test_register_team_using_post(self):
        """Test case for register_team_using_post

        registerTeam  # noqa: E501
        """
        pass

    def test_save_using_post2(self):
        """Test case for save_using_post2

        save  # noqa: E501
        """
        pass

    def test_search_event_using_post(self):
        """Test case for search_event_using_post

        searchEvent  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
