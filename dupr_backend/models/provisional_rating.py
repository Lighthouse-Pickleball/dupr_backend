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

class ProvisionalRating(object):
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
        'doubles_rating': 'float',
        'singles_rating': 'float'
    }

    attribute_map = {
        'doubles_rating': 'doublesRating',
        'singles_rating': 'singlesRating'
    }

    def __init__(self, doubles_rating=None, singles_rating=None):  # noqa: E501
        """ProvisionalRating - a model defined in Swagger"""  # noqa: E501
        self._doubles_rating = None
        self._singles_rating = None
        self.discriminator = None
        if doubles_rating is not None:
            self.doubles_rating = doubles_rating
        if singles_rating is not None:
            self.singles_rating = singles_rating

    @property
    def doubles_rating(self):
        """Gets the doubles_rating of this ProvisionalRating.  # noqa: E501


        :return: The doubles_rating of this ProvisionalRating.  # noqa: E501
        :rtype: float
        """
        return self._doubles_rating

    @doubles_rating.setter
    def doubles_rating(self, doubles_rating):
        """Sets the doubles_rating of this ProvisionalRating.


        :param doubles_rating: The doubles_rating of this ProvisionalRating.  # noqa: E501
        :type: float
        """

        self._doubles_rating = doubles_rating

    @property
    def singles_rating(self):
        """Gets the singles_rating of this ProvisionalRating.  # noqa: E501


        :return: The singles_rating of this ProvisionalRating.  # noqa: E501
        :rtype: float
        """
        return self._singles_rating

    @singles_rating.setter
    def singles_rating(self, singles_rating):
        """Sets the singles_rating of this ProvisionalRating.


        :param singles_rating: The singles_rating of this ProvisionalRating.  # noqa: E501
        :type: float
        """

        self._singles_rating = singles_rating

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
        if issubclass(ProvisionalRating, dict):
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
        if not isinstance(other, ProvisionalRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
