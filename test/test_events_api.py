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
from dupr_backend.api.events_api import EventsApi  # noqa: E501
from dupr_backend.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_checkout_event_using_get(self):
        """Test case for checkout_event_using_get

        checkoutEvent  # noqa: E501
        """
        pass

    def test_delete_league_using_delete1(self):
        """Test case for delete_league_using_delete1

        deleteLeague  # noqa: E501
        """
        pass

    def test_delete_text_content_using_delete(self):
        """Test case for delete_text_content_using_delete

        deleteTextContent  # noqa: E501
        """
        pass

    def test_draft_using_post1(self):
        """Test case for draft_using_post1

        draft  # noqa: E501
        """
        pass

    def test_edit_league_using_put(self):
        """Test case for edit_league_using_put

        editLeague  # noqa: E501
        """
        pass

    def test_end_league_using_get1(self):
        """Test case for end_league_using_get1

        endLeague  # noqa: E501
        """
        pass

    def test_export_event_participants_using_get(self):
        """Test case for export_event_participants_using_get

        exportEventParticipants  # noqa: E501
        """
        pass

    def test_export_event_payments_using_post(self):
        """Test case for export_event_payments_using_post

        exportEventPayments  # noqa: E501
        """
        pass

    def test_get_all_event_players_using_post1(self):
        """Test case for get_all_event_players_using_post1

        getAllEventPlayers  # noqa: E501
        """
        pass

    def test_get_city_autocomplete_using_get(self):
        """Test case for get_city_autocomplete_using_get

        getCityAutocomplete  # noqa: E501
        """
        pass

    def test_get_club_leagues_using_get(self):
        """Test case for get_club_leagues_using_get

        getClubLeagues  # noqa: E501
        """
        pass

    def test_get_league_policy_using_get(self):
        """Test case for get_league_policy_using_get

        getLeaguePolicy  # noqa: E501
        """
        pass

    def test_get_league_using_get(self):
        """Test case for get_league_using_get

        getLeague  # noqa: E501
        """
        pass

    def test_get_leagues_by_user_id_using_post(self):
        """Test case for get_leagues_by_user_id_using_post

        getLeaguesByUserId  # noqa: E501
        """
        pass

    def test_get_my_leagues_using_post(self):
        """Test case for get_my_leagues_using_post

        getMyLeagues  # noqa: E501
        """
        pass

    def test_join_event_using_post(self):
        """Test case for join_event_using_post

        joinEvent  # noqa: E501
        """
        pass

    def test_register_event_using_post(self):
        """Test case for register_event_using_post

        registerEvent  # noqa: E501
        """
        pass

    def test_save_using_post1(self):
        """Test case for save_using_post1

        save  # noqa: E501
        """
        pass

    def test_search_leagues_using_post(self):
        """Test case for search_leagues_using_post

        searchLeagues  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
