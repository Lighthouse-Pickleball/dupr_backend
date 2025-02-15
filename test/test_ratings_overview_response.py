# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.ratings_overview_response import RatingsOverviewResponse

class TestRatingsOverviewResponse(unittest.TestCase):
    """RatingsOverviewResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RatingsOverviewResponse:
        """Test RatingsOverviewResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RatingsOverviewResponse`
        """
        model = RatingsOverviewResponse()
        if include_optional:
            return RatingsOverviewResponse(
                losses = 56,
                pending = 56,
                wins = 56
            )
        else:
            return RatingsOverviewResponse(
                losses = 56,
                pending = 56,
                wins = 56,
        )
        """

    def testRatingsOverviewResponse(self):
        """Test RatingsOverviewResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
