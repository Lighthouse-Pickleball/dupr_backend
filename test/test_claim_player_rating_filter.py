# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.claim_player_rating_filter import ClaimPlayerRatingFilter

class TestClaimPlayerRatingFilter(unittest.TestCase):
    """ClaimPlayerRatingFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClaimPlayerRatingFilter:
        """Test ClaimPlayerRatingFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClaimPlayerRatingFilter`
        """
        model = ClaimPlayerRatingFilter()
        if include_optional:
            return ClaimPlayerRatingFilter(
                max_rating = 3.3,
                min_rating = 2.3,
                type = 'DOUBLES'
            )
        else:
            return ClaimPlayerRatingFilter(
        )
        """

    def testClaimPlayerRatingFilter(self):
        """Test ClaimPlayerRatingFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
