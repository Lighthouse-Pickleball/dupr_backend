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
from dupr_backend.models.assign_role_request import AssignRoleRequest  # noqa: E501
from dupr_backend.rest import ApiException

class TestAssignRoleRequest(unittest.TestCase):
    """AssignRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AssignRoleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssignRoleRequest`
        """
        model = dupr_backend.models.assign_role_request.AssignRoleRequest()  # noqa: E501
        if include_optional :
            return AssignRoleRequest(
                role_id = 2131312, 
                user_id = 1231231
            )
        else :
            return AssignRoleRequest(
                role_id = 2131312,
                user_id = 1231231,
        )
        """

    def testAssignRoleRequest(self):
        """Test AssignRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
