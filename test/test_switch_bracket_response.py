# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.switch_bracket_response import SwitchBracketResponse

class TestSwitchBracketResponse(unittest.TestCase):
    """SwitchBracketResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwitchBracketResponse:
        """Test SwitchBracketResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwitchBracketResponse`
        """
        model = SwitchBracketResponse()
        if include_optional:
            return SwitchBracketResponse(
                failed_reason = '',
                is_source_re_seeded = True,
                is_success = False,
                is_target_re_seeded = True,
                registration_id = 56,
                user_id = 56
            )
        else:
            return SwitchBracketResponse(
        )
        """

    def testSwitchBracketResponse(self):
        """Test SwitchBracketResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
