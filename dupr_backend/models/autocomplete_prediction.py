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

class AutocompletePrediction(object):
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
        'description': 'str',
        'distance_meters': 'int',
        'matched_substrings': 'list[MatchedSubstring]',
        'place_id': 'str',
        'structured_formatting': 'AutocompleteStructuredFormatting',
        'terms': 'list[Term]',
        'types': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'distance_meters': 'distanceMeters',
        'matched_substrings': 'matchedSubstrings',
        'place_id': 'placeId',
        'structured_formatting': 'structuredFormatting',
        'terms': 'terms',
        'types': 'types'
    }

    def __init__(self, description=None, distance_meters=None, matched_substrings=None, place_id=None, structured_formatting=None, terms=None, types=None):  # noqa: E501
        """AutocompletePrediction - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._distance_meters = None
        self._matched_substrings = None
        self._place_id = None
        self._structured_formatting = None
        self._terms = None
        self._types = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if distance_meters is not None:
            self.distance_meters = distance_meters
        if matched_substrings is not None:
            self.matched_substrings = matched_substrings
        if place_id is not None:
            self.place_id = place_id
        if structured_formatting is not None:
            self.structured_formatting = structured_formatting
        if terms is not None:
            self.terms = terms
        if types is not None:
            self.types = types

    @property
    def description(self):
        """Gets the description of this AutocompletePrediction.  # noqa: E501


        :return: The description of this AutocompletePrediction.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AutocompletePrediction.


        :param description: The description of this AutocompletePrediction.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def distance_meters(self):
        """Gets the distance_meters of this AutocompletePrediction.  # noqa: E501


        :return: The distance_meters of this AutocompletePrediction.  # noqa: E501
        :rtype: int
        """
        return self._distance_meters

    @distance_meters.setter
    def distance_meters(self, distance_meters):
        """Sets the distance_meters of this AutocompletePrediction.


        :param distance_meters: The distance_meters of this AutocompletePrediction.  # noqa: E501
        :type: int
        """

        self._distance_meters = distance_meters

    @property
    def matched_substrings(self):
        """Gets the matched_substrings of this AutocompletePrediction.  # noqa: E501


        :return: The matched_substrings of this AutocompletePrediction.  # noqa: E501
        :rtype: list[MatchedSubstring]
        """
        return self._matched_substrings

    @matched_substrings.setter
    def matched_substrings(self, matched_substrings):
        """Sets the matched_substrings of this AutocompletePrediction.


        :param matched_substrings: The matched_substrings of this AutocompletePrediction.  # noqa: E501
        :type: list[MatchedSubstring]
        """

        self._matched_substrings = matched_substrings

    @property
    def place_id(self):
        """Gets the place_id of this AutocompletePrediction.  # noqa: E501


        :return: The place_id of this AutocompletePrediction.  # noqa: E501
        :rtype: str
        """
        return self._place_id

    @place_id.setter
    def place_id(self, place_id):
        """Sets the place_id of this AutocompletePrediction.


        :param place_id: The place_id of this AutocompletePrediction.  # noqa: E501
        :type: str
        """

        self._place_id = place_id

    @property
    def structured_formatting(self):
        """Gets the structured_formatting of this AutocompletePrediction.  # noqa: E501


        :return: The structured_formatting of this AutocompletePrediction.  # noqa: E501
        :rtype: AutocompleteStructuredFormatting
        """
        return self._structured_formatting

    @structured_formatting.setter
    def structured_formatting(self, structured_formatting):
        """Sets the structured_formatting of this AutocompletePrediction.


        :param structured_formatting: The structured_formatting of this AutocompletePrediction.  # noqa: E501
        :type: AutocompleteStructuredFormatting
        """

        self._structured_formatting = structured_formatting

    @property
    def terms(self):
        """Gets the terms of this AutocompletePrediction.  # noqa: E501


        :return: The terms of this AutocompletePrediction.  # noqa: E501
        :rtype: list[Term]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this AutocompletePrediction.


        :param terms: The terms of this AutocompletePrediction.  # noqa: E501
        :type: list[Term]
        """

        self._terms = terms

    @property
    def types(self):
        """Gets the types of this AutocompletePrediction.  # noqa: E501


        :return: The types of this AutocompletePrediction.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this AutocompletePrediction.


        :param types: The types of this AutocompletePrediction.  # noqa: E501
        :type: list[str]
        """

        self._types = types

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
        if issubclass(AutocompletePrediction, dict):
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
        if not isinstance(other, AutocompletePrediction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
