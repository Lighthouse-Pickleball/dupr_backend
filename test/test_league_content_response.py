# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.league_content_response import LeagueContentResponse

class TestLeagueContentResponse(unittest.TestCase):
    """LeagueContentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeagueContentResponse:
        """Test LeagueContentResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeagueContentResponse`
        """
        model = LeagueContentResponse()
        if include_optional:
            return LeagueContentResponse(
                content_id = 45785789,
                header = '<h1>header</h1>',
                header_type = 'text/html',
                content = '<h1>content</h1>',
                content_type = 'text/html',
                footer = '<h1>footer</h1>',
                footer_type = 'text/html'
            )
        else:
            return LeagueContentResponse(
                content_id = 45785789,
                content = '<h1>content</h1>',
                content_type = 'text/html',
        )
        """

    def testLeagueContentResponse(self):
        """Test LeagueContentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
