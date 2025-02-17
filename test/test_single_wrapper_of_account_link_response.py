# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.single_wrapper_of_account_link_response import SingleWrapperOfAccountLinkResponse

class TestSingleWrapperOfAccountLinkResponse(unittest.TestCase):
    """SingleWrapperOfAccountLinkResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperOfAccountLinkResponse:
        """Test SingleWrapperOfAccountLinkResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfAccountLinkResponse`
        """
        model = SingleWrapperOfAccountLinkResponse()
        if include_optional:
            return SingleWrapperOfAccountLinkResponse(
                message = 'Show this message to user.',
                result = dupr_backend.models.account_link_response.AccountLinkResponse(
                    created = 1645628420, 
                    expires_at = 1645628720, 
                    url = 'https://stripe.com/express/Ln7FfnNpUcCU', ),
                status = 'FAILURE'
            )
        else:
            return SingleWrapperOfAccountLinkResponse(
        )
        """

    def testSingleWrapperOfAccountLinkResponse(self):
        """Test SingleWrapperOfAccountLinkResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
