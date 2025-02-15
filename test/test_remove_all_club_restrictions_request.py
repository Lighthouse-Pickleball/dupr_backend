# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.remove_all_club_restrictions_request import RemoveAllClubRestrictionsRequest

class TestRemoveAllClubRestrictionsRequest(unittest.TestCase):
    """RemoveAllClubRestrictionsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemoveAllClubRestrictionsRequest:
        """Test RemoveAllClubRestrictionsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemoveAllClubRestrictionsRequest`
        """
        model = RemoveAllClubRestrictionsRequest()
        if include_optional:
            return RemoveAllClubRestrictionsRequest(
                club_id = 56
            )
        else:
            return RemoveAllClubRestrictionsRequest(
        )
        """

    def testRemoveAllClubRestrictionsRequest(self):
        """Test RemoveAllClubRestrictionsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
