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
from dupr_backend.models.user_list_request import UserListRequest  # noqa: E501
from dupr_backend.rest import ApiException

class TestUserListRequest(unittest.TestCase):
    """UserListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserListRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserListRequest`
        """
        model = dupr_backend.models.user_list_request.UserListRequest()  # noqa: E501
        if include_optional :
            return UserListRequest(
                user_ids = [1231231, 9999999]
            )
        else :
            return UserListRequest(
                user_ids = [1231231, 9999999],
        )
        """

    def testUserListRequest(self):
        """Test UserListRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
