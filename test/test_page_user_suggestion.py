# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.page_user_suggestion import PageUserSuggestion

class TestPageUserSuggestion(unittest.TestCase):
    """PageUserSuggestion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageUserSuggestion:
        """Test PageUserSuggestion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageUserSuggestion`
        """
        model = PageUserSuggestion()
        if include_optional:
            return PageUserSuggestion(
                offset = 90,
                limit = 10,
                total = 100,
                hits = [
                    dupr_backend.models.user_suggestion.UserSuggestion(
                        user_id = 56, 
                        dupr_id = '', 
                        status = 'ACTIVE', 
                        name = '', 
                        image_url = '', 
                        address = '', 
                        brief_followers = [
                            dupr_backend.models.user_follow.UserFollow(
                                user_id = 56, 
                                name = '', )
                            ], 
                        follower_count = 56, )
                    ],
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO',
                has_previous = True,
                empty = False,
                has_more = False
            )
        else:
            return PageUserSuggestion(
                offset = 90,
                limit = 10,
                total = 100,
                total_value_relation = 'GREATER_THAN_OR_EQUAL_TO',
                has_previous = True,
                empty = False,
                has_more = False,
        )
        """

    def testPageUserSuggestion(self):
        """Test PageUserSuggestion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
