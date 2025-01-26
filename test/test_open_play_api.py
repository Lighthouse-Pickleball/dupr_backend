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
from dupr_backend.api.open_play_api import OpenPlayApi  # noqa: E501
from dupr_backend.rest import ApiException


class TestOpenPlayApi(unittest.TestCase):
    """OpenPlayApi unit test stubs"""

    def setUp(self):
        self.api = OpenPlayApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_invitation_using_post(self):
        """Test case for accept_invitation_using_post

        acceptInvitation  # noqa: E501
        """
        pass

    def test_create_using_post(self):
        """Test case for create_using_post

        create  # noqa: E501
        """
        pass

    def test_get_event_detail_using_get(self):
        """Test case for get_event_detail_using_get

        getEventDetail  # noqa: E501
        """
        pass

    def test_get_events_members_using_get(self):
        """Test case for get_events_members_using_get

        getEventsMembers  # noqa: E501
        """
        pass

    def test_get_events_near_by_using_get(self):
        """Test case for get_events_near_by_using_get

        getEventsNearBy  # noqa: E501
        """
        pass

    def test_get_invitation_by_player_using_get(self):
        """Test case for get_invitation_by_player_using_get

        getInvitationByPlayer  # noqa: E501
        """
        pass

    def test_get_waitlist_by_player_using_get(self):
        """Test case for get_waitlist_by_player_using_get

        getWaitlistByPlayer  # noqa: E501
        """
        pass

    def test_join_waitlist_using_post(self):
        """Test case for join_waitlist_using_post

        joinWaitlist  # noqa: E501
        """
        pass

    def test_register_event_using_post1(self):
        """Test case for register_event_using_post1

        registerEvent  # noqa: E501
        """
        pass

    def test_reject_invitation_using_post(self):
        """Test case for reject_invitation_using_post

        rejectInvitation  # noqa: E501
        """
        pass

    def test_update_using_put(self):
        """Test case for update_using_put

        update  # noqa: E501
        """
        pass

    def test_withdraw_event_using_delete(self):
        """Test case for withdraw_event_using_delete

        withdrawEvent  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
