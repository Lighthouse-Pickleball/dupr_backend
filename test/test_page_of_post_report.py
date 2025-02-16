# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.page_of_post_report import PageOfPostReport

class TestPageOfPostReport(unittest.TestCase):
    """PageOfPostReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageOfPostReport:
        """Test PageOfPostReport
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageOfPostReport`
        """
        model = PageOfPostReport()
        if include_optional:
            return PageOfPostReport(
                empty = False,
                has_more = False,
                has_previous = True,
                hits = [
                    dupr_backend.models.post_report.PostReport(
                        count_report = 56, 
                        created_at = 56, 
                        id = '', 
                        note = '', 
                        report_reason = '', 
                        report_type = 'COMMENT', 
                        reported_id = '', 
                        reporter_id = 56, 
                        status = 'APPROVED', 
                        updated_at = 56, )
                    ],
                limit = 10,
                offset = 90,
                total = 100,
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO'
            )
        else:
            return PageOfPostReport(
                empty = False,
                has_more = False,
                has_previous = True,
                limit = 10,
                offset = 90,
                total = 100,
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO',
        )
        """

    def testPageOfPostReport(self):
        """Test PageOfPostReport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
