# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import dupr_backend
from dupr_backend.models.sign_up_request import SignUpRequest  # noqa: E501
from dupr_backend.rest import ApiException

class TestSignUpRequest(unittest.TestCase):
    """SignUpRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SignUpRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignUpRequest`
        """
        model = dupr_backend.models.sign_up_request.SignUpRequest()  # noqa: E501
        if include_optional :
            return SignUpRequest(
                address = 'GhIJQWX8-4yLQkARem8MAcBEWcA', 
                birthdate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                doubles_rating = 4.3, 
                dupr_id = 'C8AX1', 
                email = 'john.doe@yopmail.com', 
                external_id = 'B1234', 
                gender = 'male', 
                phone_number = '+12481234701', 
                player_name = 'John Doe', 
                singles_rating = 2.6
            )
        else :
            return SignUpRequest(
                email = 'john.doe@yopmail.com',
                player_name = 'John Doe',
        )
        """

    def testSignUpRequest(self):
        """Test SignUpRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
