# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.verify_otp_request import VerifyOtpRequest

class TestVerifyOtpRequest(unittest.TestCase):
    """VerifyOtpRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VerifyOtpRequest:
        """Test VerifyOtpRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VerifyOtpRequest`
        """
        model = VerifyOtpRequest()
        if include_optional:
            return VerifyOtpRequest(
                iso_code = 'US',
                otp = '012345',
                phone_number = '+918087XXXXXX'
            )
        else:
            return VerifyOtpRequest(
                iso_code = 'US',
                otp = '012345',
                phone_number = '+918087XXXXXX',
        )
        """

    def testVerifyOtpRequest(self):
        """Test VerifyOtpRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
