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
from dupr_backend.models.merge_users_request import MergeUsersRequest  # noqa: E501
from dupr_backend.rest import ApiException

class TestMergeUsersRequest(unittest.TestCase):
    """MergeUsersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MergeUsersRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MergeUsersRequest`
        """
        model = dupr_backend.models.merge_users_request.MergeUsersRequest()  # noqa: E501
        if include_optional :
            return MergeUsersRequest(
                source = '26518181881', 
                source_type = 'DUPR_ID/USER_ID/OBFUSCATED_USER_ID/EMAIL', 
                target = 'A1C3Z', 
                target_type = 'DUPR_ID/USER_ID/OBFUSCATED_USER_ID/EMAIL'
            )
        else :
            return MergeUsersRequest(
                source = '26518181881',
                source_type = 'DUPR_ID/USER_ID/OBFUSCATED_USER_ID/EMAIL',
                target = 'A1C3Z',
                target_type = 'DUPR_ID/USER_ID/OBFUSCATED_USER_ID/EMAIL',
        )
        """

    def testMergeUsersRequest(self):
        """Test MergeUsersRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
