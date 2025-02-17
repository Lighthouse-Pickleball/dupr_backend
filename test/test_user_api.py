# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_delete_user_using_delete(self) -> None:
        """Test case for delete_user_using_delete

        deleteUser
        """
        pass

    def test_delete_using_delete(self) -> None:
        """Test case for delete_using_delete

        delete
        """
        pass

    def test_get_calculated_statistics_using_get(self) -> None:
        """Test case for get_calculated_statistics_using_get

        getCalculatedStatistics
        """
        pass

    def test_get_profile_using_get(self) -> None:
        """Test case for get_profile_using_get

        getProfile
        """
        pass

    def test_get_rating_using_get(self) -> None:
        """Test case for get_rating_using_get

        getRating
        """
        pass

    def test_get_settings_using_get(self) -> None:
        """Test case for get_settings_using_get

        getSettings
        """
        pass

    def test_get_sponsor_logo_using_get(self) -> None:
        """Test case for get_sponsor_logo_using_get

        getSponsorLogo
        """
        pass

    def test_get_statistics_using_get1(self) -> None:
        """Test case for get_statistics_using_get1

        getStatistics
        """
        pass

    def test_get_user_initialization_information_bulk_using_post(self) -> None:
        """Test case for get_user_initialization_information_bulk_using_post

        getUserInitializationInformationBulk
        """
        pass

    def test_get_user_initialization_information_using_get(self) -> None:
        """Test case for get_user_initialization_information_using_get

        getUserInitializationInformation
        """
        pass

    def test_get_verfied_statistics_using_get(self) -> None:
        """Test case for get_verfied_statistics_using_get

        getVerfiedStatistics
        """
        pass

    def test_history_using_get(self) -> None:
        """Test case for history_using_get

        history
        """
        pass

    def test_is_sole_director_using_get(self) -> None:
        """Test case for is_sole_director_using_get

        isSoleDirector
        """
        pass

    def test_logout_using_post(self) -> None:
        """Test case for logout_using_post

        logout
        """
        pass

    def test_reset_password_using_post(self) -> None:
        """Test case for reset_password_using_post

        resetPassword
        """
        pass

    def test_send_email_verification_link_using_post(self) -> None:
        """Test case for send_email_verification_link_using_post

        sendEmailVerificationLink
        """
        pass

    def test_send_phone_otp_using_post(self) -> None:
        """Test case for send_phone_otp_using_post

        sendPhoneOTP
        """
        pass

    def test_send_verification_email_using_post(self) -> None:
        """Test case for send_verification_email_using_post

        sendVerificationEmail
        """
        pass

    def test_update_lucra_connection_using_put1(self) -> None:
        """Test case for update_lucra_connection_using_put1

        updateLucraConnection
        """
        pass

    def test_update_preferences_using_put(self) -> None:
        """Test case for update_preferences_using_put

        updatePreferences
        """
        pass

    def test_update_profile_using_put(self) -> None:
        """Test case for update_profile_using_put

        updateProfile
        """
        pass

    def test_update_settings_using_put(self) -> None:
        """Test case for update_settings_using_put

        updateSettings
        """
        pass

    def test_verify_captcha_using_post(self) -> None:
        """Test case for verify_captcha_using_post

        verifyCaptcha
        """
        pass

    def test_verify_email_address_using_post(self) -> None:
        """Test case for verify_email_address_using_post

        verifyEmailAddress
        """
        pass

    def test_verify_phone_number_using_post(self) -> None:
        """Test case for verify_phone_number_using_post

        verifyPhoneNumber
        """
        pass


if __name__ == '__main__':
    unittest.main()
