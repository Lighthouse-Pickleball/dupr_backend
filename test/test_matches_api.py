# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.api.matches_api import MatchesApi


class TestMatchesApi(unittest.TestCase):
    """MatchesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MatchesApi()

    def tearDown(self) -> None:
        pass

    def test_confirm_match_using_post1(self) -> None:
        """Test case for confirm_match_using_post1

        confirmMatch
        """
        pass

    def test_delete_match_using_delete(self) -> None:
        """Test case for delete_match_using_delete

        deleteMatch
        """
        pass

    def test_get_dupr_performance_data_user_using_get(self) -> None:
        """Test case for get_dupr_performance_data_user_using_get

        getDuprPerformanceDataUser
        """
        pass

    def test_get_dupr_performance_data_using_get(self) -> None:
        """Test case for get_dupr_performance_data_using_get

        getDuprPerformanceData
        """
        pass

    def test_get_match_rating_simulator_using_post(self) -> None:
        """Test case for get_match_rating_simulator_using_post

        getMatchRatingSimulator
        """
        pass

    def test_get_user_match_history_using_get(self) -> None:
        """Test case for get_user_match_history_using_get

        getUserMatchHistory
        """
        pass

    def test_match_details_using_get(self) -> None:
        """Test case for match_details_using_get

        matchDetails
        """
        pass

    def test_pending_match_details_using_get(self) -> None:
        """Test case for pending_match_details_using_get

        pendingMatchDetails
        """
        pass

    def test_save_match_using_put(self) -> None:
        """Test case for save_match_using_put

        saveMatch
        """
        pass

    def test_save_verified_match_cvs_using_put(self) -> None:
        """Test case for save_verified_match_cvs_using_put

        saveVerifiedMatchCVS
        """
        pass

    def test_save_verified_match_using_put1(self) -> None:
        """Test case for save_verified_match_using_put1

        saveVerifiedMatch
        """
        pass

    def test_score_formats_using_get(self) -> None:
        """Test case for score_formats_using_get

        scoreFormats
        """
        pass

    def test_share_match_using_post(self) -> None:
        """Test case for share_match_using_post

        shareMatch
        """
        pass

    def test_user_match_history_by_filters_using_post(self) -> None:
        """Test case for user_match_history_by_filters_using_post

        userMatchHistoryByFilters
        """
        pass

    def test_user_match_history_using_get(self) -> None:
        """Test case for user_match_history_using_get

        userMatchHistory
        """
        pass


if __name__ == '__main__':
    unittest.main()
