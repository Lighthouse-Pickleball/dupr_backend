# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.activity_user import ActivityUser

class TestActivityUser(unittest.TestCase):
    """ActivityUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityUser:
        """Test ActivityUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityUser`
        """
        model = ActivityUser()
        if include_optional:
            return ActivityUser(
                id = 56,
                name = '',
                profile_image = '',
                is_follow = True
            )
        else:
            return ActivityUser(
                id = 56,
                name = '',
                profile_image = '',
                is_follow = True,
        )
        """

    def testActivityUser(self):
        """Test ActivityUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
