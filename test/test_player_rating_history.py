# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.player_rating_history import PlayerRatingHistory

class TestPlayerRatingHistory(unittest.TestCase):
    """PlayerRatingHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerRatingHistory:
        """Test PlayerRatingHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerRatingHistory`
        """
        model = PlayerRatingHistory()
        if include_optional:
            return PlayerRatingHistory(
                changed_by_admin = True,
                created = '',
                doubles = 1.337,
                doubles_provisional = True,
                match_date = '',
                rating_history_id = 56,
                singles = 1.337,
                singles_provisional = True,
                status = '',
                user_email = '',
                user_id = 56,
                user_name = ''
            )
        else:
            return PlayerRatingHistory(
                changed_by_admin = True,
                created = '',
                doubles_provisional = True,
                rating_history_id = 56,
                singles_provisional = True,
                user_email = '',
                user_id = 56,
                user_name = '',
        )
        """

    def testPlayerRatingHistory(self):
        """Test PlayerRatingHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
