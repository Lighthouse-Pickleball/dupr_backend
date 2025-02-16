# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import dupr_backend
from dupr_backend.models.single_wrapper_of_post_report import SingleWrapperOfPostReport  # noqa: E501
from dupr_backend.rest import ApiException

class TestSingleWrapperOfPostReport(unittest.TestCase):
    """SingleWrapperOfPostReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SingleWrapperOfPostReport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfPostReport`
        """
        model = dupr_backend.models.single_wrapper_of_post_report.SingleWrapperOfPostReport()  # noqa: E501
        if include_optional :
            return SingleWrapperOfPostReport(
                message = 'Show this message to user.', 
                result = dupr_backend.models.post_report.PostReport(
                    count_report = 56, 
                    created_at = 56, 
                    id = '', 
                    note = '', 
                    report_reason = '', 
                    report_type = 'COMMENT', 
                    reported_id = '', 
                    reporter_id = 56, 
                    status = 'APPROVED', 
                    updated_at = 56, ), 
                status = 'FAILURE'
            )
        else :
            return SingleWrapperOfPostReport(
        )
        """

    def testSingleWrapperOfPostReport(self):
        """Test SingleWrapperOfPostReport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
