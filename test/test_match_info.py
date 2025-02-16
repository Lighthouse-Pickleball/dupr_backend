# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.match_info import MatchInfo

class TestMatchInfo(unittest.TestCase):
    """MatchInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatchInfo:
        """Test MatchInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchInfo`
        """
        model = MatchInfo()
        if include_optional:
            return MatchInfo(
                event_format = 'DOUBLES',
                event_name = '',
                match_source = 'CLUB'
            )
        else:
            return MatchInfo(
                event_format = 'DOUBLES',
                match_source = 'CLUB',
        )
        """

    def testMatchInfo(self):
        """Test MatchInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
