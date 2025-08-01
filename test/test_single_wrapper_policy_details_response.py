# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.single_wrapper_policy_details_response import SingleWrapperPolicyDetailsResponse

class TestSingleWrapperPolicyDetailsResponse(unittest.TestCase):
    """SingleWrapperPolicyDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperPolicyDetailsResponse:
        """Test SingleWrapperPolicyDetailsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperPolicyDetailsResponse`
        """
        model = SingleWrapperPolicyDetailsResponse()
        if include_optional:
            return SingleWrapperPolicyDetailsResponse(
                status = 'SUCCESS',
                message = 'Show this message to user.',
                result = dupr_backend.models.policy_details_response.PolicyDetailsResponse(
                    refund_policy = dupr_backend.models.league_content_response.LeagueContentResponse(
                        content_id = 45785789, 
                        header = '<h1>header</h1>', 
                        header_type = 'text/html', 
                        content = '<h1>content</h1>', 
                        content_type = 'text/html', 
                        footer = '<h1>footer</h1>', 
                        footer_type = 'text/html', ), 
                    safety_policy = dupr_backend.models.league_content_response.LeagueContentResponse(
                        content_id = 45785789, 
                        header = '<h1>header</h1>', 
                        header_type = 'text/html', 
                        content = '<h1>content</h1>', 
                        content_type = 'text/html', 
                        footer = '<h1>footer</h1>', 
                        footer_type = 'text/html', ), )
            )
        else:
            return SingleWrapperPolicyDetailsResponse(
        )
        """

    def testSingleWrapperPolicyDetailsResponse(self):
        """Test SingleWrapperPolicyDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
