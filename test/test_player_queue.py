# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.player_queue import PlayerQueue

class TestPlayerQueue(unittest.TestCase):
    """PlayerQueue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerQueue:
        """Test PlayerQueue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerQueue`
        """
        model = PlayerQueue()
        if include_optional:
            return PlayerQueue(
                create_at = 'YYYY-MM-dd',
                event = dupr_backend.models.open_play_event.OpenPlayEvent(
                    creator = dupr_backend.models.creator.Creator(
                        email = '', 
                        id = 56, 
                        name = '', ), 
                    date = 'YYYY-MM-dd', 
                    description = '', 
                    id = 56, 
                    location = '', 
                    max_players = 56, 
                    name = '', 
                    rating = dupr_backend.models.rating_range_res.RatingRangeRes(
                        max = 1.337, 
                        min = 1.337, ), 
                    registered_players = 56, 
                    time = dupr_backend.models.time_range_res.TimeRangeRes(
                        end = 'HH:mm', 
                        start = 'HH:mm', ), )
            )
        else:
            return PlayerQueue(
        )
        """

    def testPlayerQueue(self):
        """Test PlayerQueue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
