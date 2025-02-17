# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.mi_lp_team import MiLPTeam

class TestMiLPTeam(unittest.TestCase):
    """MiLPTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MiLPTeam:
        """Test MiLPTeam
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MiLPTeam`
        """
        model = MiLPTeam()
        if include_optional:
            return MiLPTeam(
                created = '',
                status = 'ACTIVE',
                team_code = '',
                team_id = 56,
                team_members = [
                    dupr_backend.models.team_member.TeamMember(
                        created = '', 
                        first_name = '', 
                        full_name = '', 
                        image_url = '', 
                        last_name = '', 
                        role = '', 
                        status = 'ACTIVE', 
                        team_id = 56, 
                        user_id = 56, )
                    ],
                team_name = ''
            )
        else:
            return MiLPTeam(
                team_id = 56,
                team_members = [
                    dupr_backend.models.team_member.TeamMember(
                        created = '', 
                        first_name = '', 
                        full_name = '', 
                        image_url = '', 
                        last_name = '', 
                        role = '', 
                        status = 'ACTIVE', 
                        team_id = 56, 
                        user_id = 56, )
                    ],
                team_name = '',
        )
        """

    def testMiLPTeam(self):
        """Test MiLPTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
