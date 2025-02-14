# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs  # noqa: E501

    OpenAPI spec version: v1.0 alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AutocompleteStructuredFormatting(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'main_text': 'str',
        'main_text_matched_substrings': 'list[MatchedSubstring]',
        'secondary_text': 'str'
    }

    attribute_map = {
        'main_text': 'mainText',
        'main_text_matched_substrings': 'mainTextMatchedSubstrings',
        'secondary_text': 'secondaryText'
    }

    def __init__(self, main_text=None, main_text_matched_substrings=None, secondary_text=None):  # noqa: E501
        """AutocompleteStructuredFormatting - a model defined in Swagger"""  # noqa: E501
        self._main_text = None
        self._main_text_matched_substrings = None
        self._secondary_text = None
        self.discriminator = None
        if main_text is not None:
            self.main_text = main_text
        if main_text_matched_substrings is not None:
            self.main_text_matched_substrings = main_text_matched_substrings
        if secondary_text is not None:
            self.secondary_text = secondary_text

    @property
    def main_text(self):
        """Gets the main_text of this AutocompleteStructuredFormatting.  # noqa: E501


        :return: The main_text of this AutocompleteStructuredFormatting.  # noqa: E501
        :rtype: str
        """
        return self._main_text

    @main_text.setter
    def main_text(self, main_text):
        """Sets the main_text of this AutocompleteStructuredFormatting.


        :param main_text: The main_text of this AutocompleteStructuredFormatting.  # noqa: E501
        :type: str
        """

        self._main_text = main_text

    @property
    def main_text_matched_substrings(self):
        """Gets the main_text_matched_substrings of this AutocompleteStructuredFormatting.  # noqa: E501


        :return: The main_text_matched_substrings of this AutocompleteStructuredFormatting.  # noqa: E501
        :rtype: list[MatchedSubstring]
        """
        return self._main_text_matched_substrings

    @main_text_matched_substrings.setter
    def main_text_matched_substrings(self, main_text_matched_substrings):
        """Sets the main_text_matched_substrings of this AutocompleteStructuredFormatting.


        :param main_text_matched_substrings: The main_text_matched_substrings of this AutocompleteStructuredFormatting.  # noqa: E501
        :type: list[MatchedSubstring]
        """

        self._main_text_matched_substrings = main_text_matched_substrings

    @property
    def secondary_text(self):
        """Gets the secondary_text of this AutocompleteStructuredFormatting.  # noqa: E501


        :return: The secondary_text of this AutocompleteStructuredFormatting.  # noqa: E501
        :rtype: str
        """
        return self._secondary_text

    @secondary_text.setter
    def secondary_text(self, secondary_text):
        """Sets the secondary_text of this AutocompleteStructuredFormatting.


        :param secondary_text: The secondary_text of this AutocompleteStructuredFormatting.  # noqa: E501
        :type: str
        """

        self._secondary_text = secondary_text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AutocompleteStructuredFormatting, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutocompleteStructuredFormatting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
