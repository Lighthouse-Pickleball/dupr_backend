# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.page_player_queue import PagePlayerQueue

class TestPagePlayerQueue(unittest.TestCase):
    """PagePlayerQueue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PagePlayerQueue:
        """Test PagePlayerQueue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PagePlayerQueue`
        """
        model = PagePlayerQueue()
        if include_optional:
            return PagePlayerQueue(
                offset = 90,
                limit = 10,
                total = 100,
                hits = [
                    dupr_backend.models.player_queue.PlayerQueue(
                        event = dupr_backend.models.open_play_event.OpenPlayEvent(
                            id = 56, 
                            name = '', 
                            date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            time = dupr_backend.models.time_range.TimeRange(
                                start = '14:30:00', 
                                end = '14:30:00', ), 
                            location = '', 
                            max_players = 56, 
                            rating = dupr_backend.models.rating_range.RatingRange(
                                min = 1.337, 
                                max = 1.337, ), 
                            description = '', 
                            registered_players = 56, 
                            creator = dupr_backend.models.creator.Creator(
                                id = 56, 
                                name = '', 
                                email = '', ), ), 
                        create_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                    ],
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO',
                has_previous = True,
                empty = False,
                has_more = False
            )
        else:
            return PagePlayerQueue(
                offset = 90,
                limit = 10,
                total = 100,
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO',
                has_previous = True,
                empty = False,
                has_more = False,
        )
        """

    def testPagePlayerQueue(self):
        """Test PagePlayerQueue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
