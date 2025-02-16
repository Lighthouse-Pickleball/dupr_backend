# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.registration_response import RegistrationResponse

class TestRegistrationResponse(unittest.TestCase):
    """RegistrationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RegistrationResponse:
        """Test RegistrationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegistrationResponse`
        """
        model = RegistrationResponse()
        if include_optional:
            return RegistrationResponse(
                event_refunded_amount = 1.337,
                is_participant1 = False,
                is_wait_listed = False,
                player1 = dupr_backend.models.participant.Participant(
                    club_member = True, 
                    display_username = True, 
                    full_name = 'Brian Lara', 
                    id = 26518181881, 
                    is_registered = False, 
                    is_substitute = False, 
                    is_wait_listed = False, 
                    partner_status = 'NOT_ADDED/CONFIRMED/NOT_CONFIRMED/PAYMENT_DUE', 
                    payment_due = '2021-12-01', 
                    payment_refunded = False, 
                    payment_status = 'PENDING/COMPLETE', 
                    refund_amount = 1.337, 
                    status = 'NOT_ADDED/CONFIRMED/NOT_CONFIRMED/PAYMENT_DUE', 
                    username = 'X AE A-XII', ),
                player2 = dupr_backend.models.participant.Participant(
                    club_member = True, 
                    display_username = True, 
                    full_name = 'Brian Lara', 
                    id = 26518181881, 
                    is_registered = False, 
                    is_substitute = False, 
                    is_wait_listed = False, 
                    partner_status = 'NOT_ADDED/CONFIRMED/NOT_CONFIRMED/PAYMENT_DUE', 
                    payment_due = '2021-12-01', 
                    payment_refunded = False, 
                    payment_status = 'PENDING/COMPLETE', 
                    refund_amount = 1.337, 
                    status = 'NOT_ADDED/CONFIRMED/NOT_CONFIRMED/PAYMENT_DUE', 
                    username = 'X AE A-XII', ),
                registration_id = 4684651981
            )
        else:
            return RegistrationResponse(
                event_refunded_amount = 1.337,
                is_participant1 = False,
                is_wait_listed = False,
                registration_id = 4684651981,
        )
        """

    def testRegistrationResponse(self):
        """Test RegistrationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
