# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.array_wrapper_of_activity_user import ArrayWrapperOfActivityUser

class TestArrayWrapperOfActivityUser(unittest.TestCase):
    """ArrayWrapperOfActivityUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayWrapperOfActivityUser:
        """Test ArrayWrapperOfActivityUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayWrapperOfActivityUser`
        """
        model = ArrayWrapperOfActivityUser()
        if include_optional:
            return ArrayWrapperOfActivityUser(
                message = 'Show this message to user.',
                results = [
                    dupr_backend.models.activity_user.ActivityUser(
                        id = 56, 
                        is_follow = True, 
                        name = '', 
                        profile_image = '', )
                    ],
                status = 'FAILURE'
            )
        else:
            return ArrayWrapperOfActivityUser(
        )
        """

    def testArrayWrapperOfActivityUser(self):
        """Test ArrayWrapperOfActivityUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
