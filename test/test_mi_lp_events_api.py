# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.api.mi_lp_events_api import MiLPEventsApi


class TestMiLPEventsApi(unittest.TestCase):
    """MiLPEventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MiLPEventsApi()

    def tearDown(self) -> None:
        pass

    def test_get_event_info_using_get(self) -> None:
        """Test case for get_event_info_using_get

        getEventInfo
        """
        pass

    def test_get_teams_using_get(self) -> None:
        """Test case for get_teams_using_get

        getTeams
        """
        pass

    def test_register_team_using_post(self) -> None:
        """Test case for register_team_using_post

        registerTeam
        """
        pass

    def test_save_using_post2(self) -> None:
        """Test case for save_using_post2

        save
        """
        pass

    def test_search_event_using_post(self) -> None:
        """Test case for search_event_using_post

        searchEvent
        """
        pass


if __name__ == '__main__':
    unittest.main()
