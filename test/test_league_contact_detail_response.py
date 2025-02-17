# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.league_contact_detail_response import LeagueContactDetailResponse

class TestLeagueContactDetailResponse(unittest.TestCase):
    """LeagueContactDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeagueContactDetailResponse:
        """Test LeagueContactDetailResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeagueContactDetailResponse`
        """
        model = LeagueContactDetailResponse()
        if include_optional:
            return LeagueContactDetailResponse(
                address = 'PA 18034, United States',
                email = 'hisenberg@yopmail.com',
                name = 'Dreamland pickalball',
                phone = '18022214966',
                priority = 1,
                type = 'person/club'
            )
        else:
            return LeagueContactDetailResponse(
        )
        """

    def testLeagueContactDetailResponse(self):
        """Test LeagueContactDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
