# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.single_wrapper_of_page_of_mi_lp_event import SingleWrapperOfPageOfMiLPEvent

class TestSingleWrapperOfPageOfMiLPEvent(unittest.TestCase):
    """SingleWrapperOfPageOfMiLPEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleWrapperOfPageOfMiLPEvent:
        """Test SingleWrapperOfPageOfMiLPEvent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleWrapperOfPageOfMiLPEvent`
        """
        model = SingleWrapperOfPageOfMiLPEvent()
        if include_optional:
            return SingleWrapperOfPageOfMiLPEvent(
                message = 'Show this message to user.',
                result = dupr_backend.models.page_of_mi_lp_event.PageOfMiLPEvent(
                    empty = False, 
                    has_more = False, 
                    has_previous = True, 
                    hits = [
                        dupr_backend.models.mi_lp_event.MiLPEvent(
                            address_str = '', 
                            club_id = 56, 
                            club_name = '', 
                            creator_email = '', 
                            creator_id = 56, 
                            creator_name = '', 
                            default_entry_fee = 1.337, 
                            default_max_teams = 56, 
                            default_max_waitlist = 56, 
                            description = dupr_backend.models.description.Description(
                                content = '', 
                                content_type = '', 
                                footer = '', 
                                footer_type = '', 
                                header = '', 
                                header_type = '', ), 
                            divisions = [
                                dupr_backend.models.division.Division(
                                    day1_start = '', 
                                    day2_start = '', 
                                    division_code = '', 
                                    division_id = 56, 
                                    division_name = '', 
                                    division_type = 'DUPR12', 
                                    entry_fee = 1.337, 
                                    event_id = 56, 
                                    max_teams = 56, 
                                    max_waitlist = 56, 
                                    prize = 1.337, 
                                    registration_end = '', 
                                    registration_period = [
                                        ''
                                        ], 
                                    registration_start = '', 
                                    status = 'ACTIVE', )
                                ], 
                            duration = [
                                ''
                                ], 
                            event_id = 56, 
                            event_name = '', 
                            event_type = 'MARQUE', 
                            status = 'ACTIVE', )
                        ], 
                    limit = 10, 
                    offset = 90, 
                    total = 100, 
                    total_value_relation = 'GREATER_THAN_OR_EQUAL_TO', ),
                status = 'FAILURE'
            )
        else:
            return SingleWrapperOfPageOfMiLPEvent(
        )
        """

    def testSingleWrapperOfPageOfMiLPEvent(self):
        """Test SingleWrapperOfPageOfMiLPEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
