# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.address_component import AddressComponent

class TestAddressComponent(unittest.TestCase):
    """AddressComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddressComponent:
        """Test AddressComponent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressComponent`
        """
        model = AddressComponent()
        if include_optional:
            return AddressComponent(
                long_name = '',
                short_name = '',
                types = [
                    'ADMINISTRATIVE_AREA_LEVEL_1'
                    ]
            )
        else:
            return AddressComponent(
        )
        """

    def testAddressComponent(self):
        """Test AddressComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
