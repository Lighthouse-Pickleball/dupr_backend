# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.single_wrapper_of_page_of_event_announcements_response import SingleWrapperOfPageOfEventAnnouncementsResponse

class TestSingleWrapperOfPageOfEventAnnouncementsResponse(unittest.TestCase):
    """SingleWrapperOfPageOfEventAnnouncementsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperOfPageOfEventAnnouncementsResponse:
        """Test SingleWrapperOfPageOfEventAnnouncementsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfPageOfEventAnnouncementsResponse`
        """
        model = SingleWrapperOfPageOfEventAnnouncementsResponse()
        if include_optional:
            return SingleWrapperOfPageOfEventAnnouncementsResponse(
                message = 'Show this message to user.',
                result = dupr_backend.models.page_of_event_announcements_response.PageOfEventAnnouncementsResponse(
                    empty = False, 
                    has_more = False, 
                    has_previous = True, 
                    hits = [
                        dupr_backend.models.event_announcements_response.EventAnnouncementsResponse(
                            announcement_id = 45785789, 
                            bracket_id = 45785789, 
                            created = '2022-04-27T21:59:57.711772', 
                            description = dupr_backend.models.content_response.ContentResponse(
                                content = '<h1>content</h1>', 
                                content_id = 45785789, 
                                content_type = 'text/html', 
                                footer = '<h1>footer</h1>', 
                                footer_type = 'text/html', 
                                header = '<h1>header</h1>', 
                                header_type = 'text/html', ), 
                            email_failed = 10, 
                            email_sent = 10, 
                            league_id = 45785789, 
                            notification_count = 10, 
                            push_failed = 10, 
                            push_sent = 10, 
                            registered_members = 10, 
                            sms_failed = 10, 
                            sms_sent = 10, 
                            status = 'ACTIVE/IN_ACTIVE/COMPLETE', 
                            title = 'announcement', )
                        ], 
                    limit = 10, 
                    offset = 90, 
                    total = 100, 
                    total_value_relation = 'GREATER_THAN_OR_EQUAL_TO', ),
                status = 'FAILURE'
            )
        else:
            return SingleWrapperOfPageOfEventAnnouncementsResponse(
        )
        """

    def testSingleWrapperOfPageOfEventAnnouncementsResponse(self):
        """Test SingleWrapperOfPageOfEventAnnouncementsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
