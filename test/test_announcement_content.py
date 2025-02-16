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
from dupr_backend.models.announcement_content import AnnouncementContent  # noqa: E501
from dupr_backend.rest import ApiException

class TestAnnouncementContent(unittest.TestCase):
    """AnnouncementContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnnouncementContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnnouncementContent`
        """
        model = dupr_backend.models.announcement_content.AnnouncementContent()  # noqa: E501
        if include_optional :
            return AnnouncementContent(
                content = '<h1>content</h1>', 
                content_id = 45785789, 
                content_type = 'text/html', 
                footer = '<h1>footer</h1>', 
                footer_type = 'text/html', 
                header = '<h1>header</h1>', 
                header_type = 'text/html'
            )
        else :
            return AnnouncementContent(
                content = '<h1>content</h1>',
                content_type = 'text/html',
        )
        """

    def testAnnouncementContent(self):
        """Test AnnouncementContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
