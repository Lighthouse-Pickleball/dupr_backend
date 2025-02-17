# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.open_play_event_waitlist import OpenPlayEventWaitlist

class TestOpenPlayEventWaitlist(unittest.TestCase):
    """OpenPlayEventWaitlist unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenPlayEventWaitlist:
        """Test OpenPlayEventWaitlist
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenPlayEventWaitlist`
        """
        model = OpenPlayEventWaitlist()
        if include_optional:
            return OpenPlayEventWaitlist(
                event_id = 56,
                message = '',
                waitlist_position = 56
            )
        else:
            return OpenPlayEventWaitlist(
                event_id = 56,
                waitlist_position = 56,
        )
        """

    def testOpenPlayEventWaitlist(self):
        """Test OpenPlayEventWaitlist"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
