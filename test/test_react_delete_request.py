# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.react_delete_request import ReactDeleteRequest

class TestReactDeleteRequest(unittest.TestCase):
    """ReactDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReactDeleteRequest:
        """Test ReactDeleteRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReactDeleteRequest`
        """
        model = ReactDeleteRequest()
        if include_optional:
            return ReactDeleteRequest(
                id = 'React Id from Getstream: db0f3ce2-99ab-4ec0-b006-333de4a3d47b',
                react = 'COMMENT|LIKE'
            )
        else:
            return ReactDeleteRequest(
                id = 'React Id from Getstream: db0f3ce2-99ab-4ec0-b006-333de4a3d47b',
                react = 'COMMENT|LIKE',
        )
        """

    def testReactDeleteRequest(self):
        """Test ReactDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
