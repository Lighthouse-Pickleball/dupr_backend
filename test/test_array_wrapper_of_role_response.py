# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.array_wrapper_of_role_response import ArrayWrapperOfRoleResponse

class TestArrayWrapperOfRoleResponse(unittest.TestCase):
    """ArrayWrapperOfRoleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayWrapperOfRoleResponse:
        """Test ArrayWrapperOfRoleResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayWrapperOfRoleResponse`
        """
        model = ArrayWrapperOfRoleResponse()
        if include_optional:
            return ArrayWrapperOfRoleResponse(
                message = 'Show this message to user.',
                results = [
                    dupr_backend.models.role_response.RoleResponse(
                        id = 424255123, 
                        permissions = {"USER":["VIEW","MODIFY"],"TOURNAMENT":["OWN_VIEW","OWN_MODIFY","OWN_DELETE"]}, 
                        role = 'PLAYER', )
                    ],
                status = 'FAILURE'
            )
        else:
            return ArrayWrapperOfRoleResponse(
        )
        """

    def testArrayWrapperOfRoleResponse(self):
        """Test ArrayWrapperOfRoleResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
