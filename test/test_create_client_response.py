# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.create_client_response import CreateClientResponse

class TestCreateClientResponse(unittest.TestCase):
    """CreateClientResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateClientResponse:
        """Test CreateClientResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateClientResponse`
        """
        model = CreateClientResponse()
        if include_optional:
            return CreateClientResponse(
                client_id = 56,
                client_key = '',
                client_secret = ''
            )
        else:
            return CreateClientResponse(
                client_id = 56,
        )
        """

    def testCreateClientResponse(self):
        """Test CreateClientResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
