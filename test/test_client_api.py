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
from dupr_backend.api.client_api import ClientApi  # noqa: E501
from dupr_backend.rest import ApiException


class TestClientApi(unittest.TestCase):
    """ClientApi unit test stubs"""

    def setUp(self):
        self.api = dupr_backend.api.client_api.ClientApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_client_name_by_key_using_get(self):
        """Test case for get_client_name_by_key_using_get

        getClientNameByKey  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
