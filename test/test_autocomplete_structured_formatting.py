# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import dupr_backend
from dupr_backend.models.autocomplete_structured_formatting import AutocompleteStructuredFormatting  # noqa: E501
from dupr_backend.rest import ApiException

class TestAutocompleteStructuredFormatting(unittest.TestCase):
    """AutocompleteStructuredFormatting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AutocompleteStructuredFormatting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutocompleteStructuredFormatting`
        """
        model = dupr_backend.models.autocomplete_structured_formatting.AutocompleteStructuredFormatting()  # noqa: E501
        if include_optional :
            return AutocompleteStructuredFormatting(
                main_text = '', 
                main_text_matched_substrings = [
                    dupr_backend.models.matched_substring.MatchedSubstring(
                        length = 56, 
                        offset = 56, )
                    ], 
                secondary_text = ''
            )
        else :
            return AutocompleteStructuredFormatting(
        )
        """

    def testAutocompleteStructuredFormatting(self):
        """Test AutocompleteStructuredFormatting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
