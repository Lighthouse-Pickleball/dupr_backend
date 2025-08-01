# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.user_suggestion_request import UserSuggestionRequest

class TestUserSuggestionRequest(unittest.TestCase):
    """UserSuggestionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSuggestionRequest:
        """Test UserSuggestionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSuggestionRequest`
        """
        model = UserSuggestionRequest()
        if include_optional:
            return UserSuggestionRequest(
                dupr_ids = [
                    ''
                    ]
            )
        else:
            return UserSuggestionRequest(
                dupr_ids = [
                    ''
                    ],
        )
        """

    def testUserSuggestionRequest(self):
        """Test UserSuggestionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
