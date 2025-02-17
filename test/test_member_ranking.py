# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.member_ranking import MemberRanking

class TestMemberRanking(unittest.TestCase):
    """MemberRanking unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberRanking:
        """Test MemberRanking
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberRanking`
        """
        model = MemberRanking()
        if include_optional:
            return MemberRanking(
                full_name = '',
                id = 56,
                image_url = '',
                ranking = 56,
                rating = '',
                reliability = 56
            )
        else:
            return MemberRanking(
                full_name = '',
                id = 56,
                ranking = 56,
                reliability = 56,
        )
        """

    def testMemberRanking(self):
        """Test MemberRanking"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
