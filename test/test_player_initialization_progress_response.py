# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import dupr_backend
from dupr_backend.models.player_initialization_progress_response import PlayerInitializationProgressResponse  # noqa: E501
from dupr_backend.rest import ApiException

class TestPlayerInitializationProgressResponse(unittest.TestCase):
    """PlayerInitializationProgressResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PlayerInitializationProgressResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerInitializationProgressResponse`
        """
        model = dupr_backend.models.player_initialization_progress_response.PlayerInitializationProgressResponse()  # noqa: E501
        if include_optional :
            return PlayerInitializationProgressResponse(
                data = dupr_backend.models.player_initialization_data_response.PlayerInitializationDataResponse(
                    days_left_for_initialization = 56, 
                    event_format = '', 
                    initialization_status = '', 
                    player_id = '', 
                    player_name = '', 
                    qualification_score = 1.337, ), 
                message = '', 
                status = 'FAILURE'
            )
        else :
            return PlayerInitializationProgressResponse(
                message = '',
                status = 'FAILURE',
        )
        """

    def testPlayerInitializationProgressResponse(self):
        """Test PlayerInitializationProgressResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
