# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.register_to_bracket_request import RegisterToBracketRequest

class TestRegisterToBracketRequest(unittest.TestCase):
    """RegisterToBracketRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RegisterToBracketRequest:
        """Test RegisterToBracketRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegisterToBracketRequest`
        """
        model = RegisterToBracketRequest()
        if include_optional:
            return RegisterToBracketRequest(
                bracket_id = 45785789,
                club_id = 45785789,
                users = [
                    dupr_backend.models.register_user_request.RegisterUserRequest(
                        is_club_member = True, 
                        user_id = 45785789, )
                    ]
            )
        else:
            return RegisterToBracketRequest(
                bracket_id = 45785789,
                club_id = 45785789,
        )
        """

    def testRegisterToBracketRequest(self):
        """Test RegisterToBracketRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
