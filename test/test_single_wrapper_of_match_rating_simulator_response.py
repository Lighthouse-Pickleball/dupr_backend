# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.single_wrapper_of_match_rating_simulator_response import SingleWrapperOfMatchRatingSimulatorResponse

class TestSingleWrapperOfMatchRatingSimulatorResponse(unittest.TestCase):
    """SingleWrapperOfMatchRatingSimulatorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperOfMatchRatingSimulatorResponse:
        """Test SingleWrapperOfMatchRatingSimulatorResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfMatchRatingSimulatorResponse`
        """
        model = SingleWrapperOfMatchRatingSimulatorResponse()
        if include_optional:
            return SingleWrapperOfMatchRatingSimulatorResponse(
                message = 'Show this message to user.',
                result = dupr_backend.models.match_rating_simulator_response.MatchRatingSimulatorResponse(
                    event_format = 'DOUBLES', 
                    match_source = 'CLUB', 
                    teams = [
                        dupr_backend.models.team_info0.TeamInfo0(
                            players = [
                                dupr_backend.models.player_info.PlayerInfo(
                                    id = 56, 
                                    initial_rating = 1.337, 
                                    player_no = 56, 
                                    rating_change = 1.337, 
                                    simulated_rating = 1.337, )
                                ], 
                            team_no = 56, )
                        ], ),
                status = 'FAILURE'
            )
        else:
            return SingleWrapperOfMatchRatingSimulatorResponse(
        )
        """

    def testSingleWrapperOfMatchRatingSimulatorResponse(self):
        """Test SingleWrapperOfMatchRatingSimulatorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
