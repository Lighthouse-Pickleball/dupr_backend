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
from dupr_backend.models.club_request import ClubRequest  # noqa: E501
from dupr_backend.rest import ApiException

class TestClubRequest(unittest.TestCase):
    """ClubRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClubRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClubRequest`
        """
        model = dupr_backend.models.club_request.ClubRequest()  # noqa: E501
        if include_optional :
            return ClubRequest(
                address_id = 5156151658, 
                attributes = {
                    'key' : dupr_backend.models.attribute.Attribute(
                        _children = {
                            'key' : dupr_backend.models.attribute.Attribute(
                                _comment = 'Contact person name, if provided.', 
                                value = 'String', )
                            }, 
                        _comment = 'Contact person name, if provided.', 
                        value = 'String', )
                    }, 
                club_id = 1231231, 
                club_name = 'Stillwater Pickleball', 
                club_type_id = 2, 
                currency_code = 'USD', 
                long_description = dupr_backend.models.content_request.ContentRequest(
                    content = '<h1>content</h1>', 
                    content_id = 13212313, 
                    content_type = 'text/html', 
                    footer = '<h1>footer</h1>', 
                    footer_type = 'text/html', 
                    header = '<h1>header</h1>', 
                    header_type = 'text/html', ), 
                manifest = dupr_backend.models.content_request.ContentRequest(
                    content = '<h1>content</h1>', 
                    content_id = 13212313, 
                    content_type = 'text/html', 
                    footer = '<h1>footer</h1>', 
                    footer_type = 'text/html', 
                    header = '<h1>header</h1>', 
                    header_type = 'text/html', ), 
                media_id = 4684651981, 
                model_type = 'ABSOLUTE/RELATIVE', 
                model_value = 33.5, 
                short_description = dupr_backend.models.content_request.ContentRequest(
                    content = '<h1>content</h1>', 
                    content_id = 13212313, 
                    content_type = 'text/html', 
                    footer = '<h1>footer</h1>', 
                    footer_type = 'text/html', 
                    header = '<h1>header</h1>', 
                    header_type = 'text/html', )
            )
        else :
            return ClubRequest(
                club_id = 1231231,
                club_name = 'Stillwater Pickleball',
                club_type_id = 2,
                currency_code = 'USD',
                model_type = 'ABSOLUTE/RELATIVE',
                model_value = 33.5,
        )
        """

    def testClubRequest(self):
        """Test ClubRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
