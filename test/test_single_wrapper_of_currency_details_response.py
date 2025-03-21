# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.single_wrapper_of_currency_details_response import SingleWrapperOfCurrencyDetailsResponse

class TestSingleWrapperOfCurrencyDetailsResponse(unittest.TestCase):
    """SingleWrapperOfCurrencyDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperOfCurrencyDetailsResponse:
        """Test SingleWrapperOfCurrencyDetailsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfCurrencyDetailsResponse`
        """
        model = SingleWrapperOfCurrencyDetailsResponse()
        if include_optional:
            return SingleWrapperOfCurrencyDetailsResponse(
                message = 'Show this message to user.',
                result = dupr_backend.models.currency_details_response.CurrencyDetailsResponse(
                    currency_code = 'USD', 
                    currency_name = 'US Dollar', 
                    currency_symbol = '$', 
                    min_limit = 100.0, ),
                status = 'FAILURE'
            )
        else:
            return SingleWrapperOfCurrencyDetailsResponse(
        )
        """

    def testSingleWrapperOfCurrencyDetailsResponse(self):
        """Test SingleWrapperOfCurrencyDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
