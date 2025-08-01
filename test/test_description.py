# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.description import Description

class TestDescription(unittest.TestCase):
    """Description unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Description:
        """Test Description
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Description`
        """
        model = Description()
        if include_optional:
            return Description(
                header = '',
                header_type = '',
                content = '',
                content_type = '',
                footer = '',
                footer_type = ''
            )
        else:
            return Description(
        )
        """

    def testDescription(self):
        """Test Description"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
