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
from dupr_backend.api.media_api import MediaApi  # noqa: E501
from dupr_backend.rest import ApiException


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self):
        self.api = dupr_backend.api.media_api.MediaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_upload_document_using_put(self):
        """Test case for upload_document_using_put

        uploadDocument  # noqa: E501
        """
        pass

    def test_upload_using_put(self):
        """Test case for upload_using_put

        upload  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
