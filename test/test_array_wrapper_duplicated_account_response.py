# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.array_wrapper_duplicated_account_response import ArrayWrapperDuplicatedAccountResponse

class TestArrayWrapperDuplicatedAccountResponse(unittest.TestCase):
    """ArrayWrapperDuplicatedAccountResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayWrapperDuplicatedAccountResponse:
        """Test ArrayWrapperDuplicatedAccountResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayWrapperDuplicatedAccountResponse`
        """
        model = ArrayWrapperDuplicatedAccountResponse()
        if include_optional:
            return ArrayWrapperDuplicatedAccountResponse(
                status = 'SUCCESS',
                message = 'Show this message to user.',
                results = [
                    dupr_backend.models.duplicated_account_response.DuplicatedAccountResponse(
                        player1 = dupr_backend.models.duplicated_player.DuplicatedPlayer(
                            id = 56, 
                            full_name = '', 
                            first_name = '', 
                            last_name = '', 
                            gender = 'MALE', 
                            hand = 'RIGHT', 
                            dupr_id = '', 
                            birthday = '', 
                            verified_email = True, 
                            email = '', 
                            status = 'ACTIVE', ), 
                        player2 = dupr_backend.models.duplicated_player.DuplicatedPlayer(
                            id = 56, 
                            full_name = '', 
                            first_name = '', 
                            last_name = '', 
                            gender = 'MALE', 
                            hand = 'RIGHT', 
                            dupr_id = '', 
                            birthday = '', 
                            verified_email = True, 
                            email = '', 
                            status = 'ACTIVE', ), 
                        probability = '', )
                    ]
            )
        else:
            return ArrayWrapperDuplicatedAccountResponse(
        )
        """

    def testArrayWrapperDuplicatedAccountResponse(self):
        """Test ArrayWrapperDuplicatedAccountResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
