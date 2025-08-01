# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.payment_report_request import PaymentReportRequest

class TestPaymentReportRequest(unittest.TestCase):
    """PaymentReportRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentReportRequest:
        """Test PaymentReportRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentReportRequest`
        """
        model = PaymentReportRequest()
        if include_optional:
            return PaymentReportRequest(
                client_key = '',
                purchased_package = ''
            )
        else:
            return PaymentReportRequest(
                client_key = '',
                purchased_package = '',
        )
        """

    def testPaymentReportRequest(self):
        """Test PaymentReportRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
