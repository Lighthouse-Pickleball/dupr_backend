# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.single_wrapper_of_page_of_user_suggestion import SingleWrapperOfPageOfUserSuggestion

class TestSingleWrapperOfPageOfUserSuggestion(unittest.TestCase):
    """SingleWrapperOfPageOfUserSuggestion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperOfPageOfUserSuggestion:
        """Test SingleWrapperOfPageOfUserSuggestion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfPageOfUserSuggestion`
        """
        model = SingleWrapperOfPageOfUserSuggestion()
        if include_optional:
            return SingleWrapperOfPageOfUserSuggestion(
                message = 'Show this message to user.',
                result = dupr_backend.models.page_of_user_suggestion.PageOfUserSuggestion(
                    empty = False, 
                    has_more = False, 
                    has_previous = True, 
                    hits = [
                        dupr_backend.models.user_suggestion.UserSuggestion(
                            address = '', 
                            brief_followers = [
                                dupr_backend.models.user_follow.UserFollow(
                                    name = '', 
                                    user_id = 56, )
                                ], 
                            dupr_id = '', 
                            follower_count = 56, 
                            image_url = '', 
                            name = '', 
                            status = 'ACTIVE', 
                            user_id = 56, )
                        ], 
                    limit = 10, 
                    offset = 90, 
                    total = 100, 
                    total_value_relation = 'GREATER_THAN_OR_EQUAL_TO', ),
                status = 'FAILURE'
            )
        else:
            return SingleWrapperOfPageOfUserSuggestion(
        )
        """

    def testSingleWrapperOfPageOfUserSuggestion(self):
        """Test SingleWrapperOfPageOfUserSuggestion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
