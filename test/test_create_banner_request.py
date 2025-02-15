# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.create_banner_request import CreateBannerRequest

class TestCreateBannerRequest(unittest.TestCase):
    """CreateBannerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateBannerRequest:
        """Test CreateBannerRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateBannerRequest`
        """
        model = CreateBannerRequest()
        if include_optional:
            return CreateBannerRequest(
                banner_id = 2322,
                content_id = 1214,
                description = dupr_backend.models.banner_content.BannerContent(
                    content = '<h1>content</h1>', 
                    content_id = 45785789, 
                    content_type = 'text/html', 
                    footer = '<h1>footer</h1>', 
                    footer_type = 'text/html', 
                    header = '<h1>header</h1>', 
                    header_type = 'text/html', ),
                end_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'ACTIVE/INACTIVE',
                title = 'banner Title'
            )
        else:
            return CreateBannerRequest(
                banner_id = 2322,
                content_id = 1214,
                description = dupr_backend.models.banner_content.BannerContent(
                    content = '<h1>content</h1>', 
                    content_id = 45785789, 
                    content_type = 'text/html', 
                    footer = '<h1>footer</h1>', 
                    footer_type = 'text/html', 
                    header = '<h1>header</h1>', 
                    header_type = 'text/html', ),
                status = 'ACTIVE/INACTIVE',
                title = 'banner Title',
        )
        """

    def testCreateBannerRequest(self):
        """Test CreateBannerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
