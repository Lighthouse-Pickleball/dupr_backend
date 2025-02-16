# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import dupr_backend
from dupr_backend.api.post_report_api import PostReportApi  # noqa: E501
from dupr_backend.rest import ApiException


class TestPostReportApi(unittest.TestCase):
    """PostReportApi unit test stubs"""

    def setUp(self):
        self.api = dupr_backend.api.post_report_api.PostReportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_reports_using_get(self):
        """Test case for get_reports_using_get

        getReports  # noqa: E501
        """
        pass

    def test_report_activity_using_post(self):
        """Test case for report_activity_using_post

        reportActivity  # noqa: E501
        """
        pass

    def test_report_process_using_post(self):
        """Test case for report_process_using_post

        reportProcess  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
