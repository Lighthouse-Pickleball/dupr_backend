# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.history import History

class TestHistory(unittest.TestCase):
    """History unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> History:
        """Test History
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `History`
        """
        model = History()
        if include_optional:
            return History(
                changed_by_admin = True,
                var_date = 'yyyy-MM-dd',
                match_date = 'yyyy-MM-dd',
                rating = 1.337
            )
        else:
            return History(
                changed_by_admin = True,
                var_date = 'yyyy-MM-dd',
        )
        """

    def testHistory(self):
        """Test History"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
