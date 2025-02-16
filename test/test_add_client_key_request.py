# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.add_client_key_request import AddClientKeyRequest

class TestAddClientKeyRequest(unittest.TestCase):
    """AddClientKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddClientKeyRequest:
        """Test AddClientKeyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddClientKeyRequest`
        """
        model = AddClientKeyRequest()
        if include_optional:
            return AddClientKeyRequest(
                client_id = 123456,
                permissions = [
                    dupr_backend.models.permission.Permission(
                        operations = [
                            'ADD'
                            ], 
                        resource = 'BRACKET', )
                    ]
            )
        else:
            return AddClientKeyRequest(
                client_id = 123456,
        )
        """

    def testAddClientKeyRequest(self):
        """Test AddClientKeyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
