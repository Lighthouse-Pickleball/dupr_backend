# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.event_refund_request import EventRefundRequest

class TestEventRefundRequest(unittest.TestCase):
    """EventRefundRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventRefundRequest:
        """Test EventRefundRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventRefundRequest`
        """
        model = EventRefundRequest()
        if include_optional:
            return EventRefundRequest(
                club_id = 45785789,
                event_id = 45785789,
                event_name = '45785789',
                process_refund = True,
                refund_amount = 45785789,
                player_id = 45785789,
                brackets = [
                    dupr_backend.models.bracket_refund_request.BracketRefundRequest(
                        bracket_id = 45785789, 
                        bracket_name = '45785789', 
                        registration_id = 45785789, 
                        process_refund = True, 
                        withdraw_player = True, 
                        refund_amount = 45785789, )
                    ]
            )
        else:
            return EventRefundRequest(
                club_id = 45785789,
                event_id = 45785789,
                event_name = '45785789',
                process_refund = True,
                refund_amount = 45785789,
                player_id = 45785789,
                brackets = [
                    dupr_backend.models.bracket_refund_request.BracketRefundRequest(
                        bracket_id = 45785789, 
                        bracket_name = '45785789', 
                        registration_id = 45785789, 
                        process_refund = True, 
                        withdraw_player = True, 
                        refund_amount = 45785789, )
                    ],
        )
        """

    def testEventRefundRequest(self):
        """Test EventRefundRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
