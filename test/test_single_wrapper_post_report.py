# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.single_wrapper_post_report import SingleWrapperPostReport

class TestSingleWrapperPostReport(unittest.TestCase):
    """SingleWrapperPostReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperPostReport:
        """Test SingleWrapperPostReport
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperPostReport`
        """
        model = SingleWrapperPostReport()
        if include_optional:
            return SingleWrapperPostReport(
                status = 'SUCCESS',
                message = 'Show this message to user.',
                result = dupr_backend.models.post_report.PostReport(
                    id = '', 
                    reporter_id = 56, 
                    reported_id = '', 
                    report_type = 'COMMENT', 
                    report_reason = '', 
                    note = '', 
                    status = 'PENDING', 
                    created_at = 56, 
                    updated_at = 56, 
                    count_report = 56, )
            )
        else:
            return SingleWrapperPostReport(
        )
        """

    def testSingleWrapperPostReport(self):
        """Test SingleWrapperPostReport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
