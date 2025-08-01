# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.user_actor_response import UserActorResponse

class TestUserActorResponse(unittest.TestCase):
    """UserActorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserActorResponse:
        """Test UserActorResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserActorResponse`
        """
        model = UserActorResponse()
        if include_optional:
            return UserActorResponse(
                user_v1 = dupr_backend.models.user_v1.UserV1(
                    urn = dupr_backend.models.club_v1_urn.ClubV1Urn(
                        path = '', 
                        type = '', 
                        version = '', 
                        id = '', 
                        nid = '', ), 
                    user = dupr_backend.models.user.User(
                        id = 56, 
                        full_name = '', 
                        first_name = '', 
                        last_name = '', 
                        email = '', 
                        is_valid_email = True, 
                        secret = '', 
                        iso_code = '', 
                        phone_number = '', 
                        is_valid_phone = True, 
                        nickname = '', 
                        display_username = True, 
                        media_id = 56, 
                        image_url = '', 
                        referral_code = '', 
                        gender = 'MALE', 
                        birthdate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        hand = 'RIGHT', 
                        role = dupr_backend.models.role.Role(
                            id = 56, 
                            name = '', 
                            description = '', 
                            status = 'ACTIVE', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            permissions = [
                                dupr_backend.models.permission.Permission(
                                    resource = 'NONE', 
                                    operations = [
                                        'NONE'
                                        ], )
                                ], ), 
                        customer_key = '', 
                        status = 'ACTIVE', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        external_id = '', 
                        restricted = True, 
                        reliability_score = 56, 
                        lucra_connected = True, 
                        is_enabled = True, 
                        password = '', 
                        is_admin = True, 
                        valid_email = True, 
                        valid_phone = True, 
                        is_account_non_expired = True, 
                        is_account_non_locked = True, 
                        is_credentials_non_expired = True, 
                        username = '', 
                        authorities = [
                            dupr_backend.models.granted_authority.GrantedAuthority(
                                authority = '', )
                            ], ), )
            )
        else:
            return UserActorResponse(
                user_v1 = dupr_backend.models.user_v1.UserV1(
                    urn = dupr_backend.models.club_v1_urn.ClubV1Urn(
                        path = '', 
                        type = '', 
                        version = '', 
                        id = '', 
                        nid = '', ), 
                    user = dupr_backend.models.user.User(
                        id = 56, 
                        full_name = '', 
                        first_name = '', 
                        last_name = '', 
                        email = '', 
                        is_valid_email = True, 
                        secret = '', 
                        iso_code = '', 
                        phone_number = '', 
                        is_valid_phone = True, 
                        nickname = '', 
                        display_username = True, 
                        media_id = 56, 
                        image_url = '', 
                        referral_code = '', 
                        gender = 'MALE', 
                        birthdate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        hand = 'RIGHT', 
                        role = dupr_backend.models.role.Role(
                            id = 56, 
                            name = '', 
                            description = '', 
                            status = 'ACTIVE', 
                            created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            permissions = [
                                dupr_backend.models.permission.Permission(
                                    resource = 'NONE', 
                                    operations = [
                                        'NONE'
                                        ], )
                                ], ), 
                        customer_key = '', 
                        status = 'ACTIVE', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        external_id = '', 
                        restricted = True, 
                        reliability_score = 56, 
                        lucra_connected = True, 
                        is_enabled = True, 
                        password = '', 
                        is_admin = True, 
                        valid_email = True, 
                        valid_phone = True, 
                        is_account_non_expired = True, 
                        is_account_non_locked = True, 
                        is_credentials_non_expired = True, 
                        username = '', 
                        authorities = [
                            dupr_backend.models.granted_authority.GrantedAuthority(
                                authority = '', )
                            ], ), ),
        )
        """

    def testUserActorResponse(self):
        """Test UserActorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
