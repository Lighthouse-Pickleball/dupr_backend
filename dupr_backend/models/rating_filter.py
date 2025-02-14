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

class RatingFilter(object):
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
        'category': 'str',
        'max_rating': 'float',
        'min_rating': 'float',
        'type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'max_rating': 'maxRating',
        'min_rating': 'minRating',
        'type': 'type'
    }

    def __init__(self, category=None, max_rating=None, min_rating=None, type=None):  # noqa: E501
        """RatingFilter - a model defined in Swagger"""  # noqa: E501
        self._category = None
        self._max_rating = None
        self._min_rating = None
        self._type = None
        self.discriminator = None
        if category is not None:
            self.category = category
        if max_rating is not None:
            self.max_rating = max_rating
        if min_rating is not None:
            self.min_rating = min_rating
        if type is not None:
            self.type = type

    @property
    def category(self):
        """Gets the category of this RatingFilter.  # noqa: E501


        :return: The category of this RatingFilter.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this RatingFilter.


        :param category: The category of this RatingFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["DUPR", "PROVISIONAL"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def max_rating(self):
        """Gets the max_rating of this RatingFilter.  # noqa: E501


        :return: The max_rating of this RatingFilter.  # noqa: E501
        :rtype: float
        """
        return self._max_rating

    @max_rating.setter
    def max_rating(self, max_rating):
        """Sets the max_rating of this RatingFilter.


        :param max_rating: The max_rating of this RatingFilter.  # noqa: E501
        :type: float
        """

        self._max_rating = max_rating

    @property
    def min_rating(self):
        """Gets the min_rating of this RatingFilter.  # noqa: E501


        :return: The min_rating of this RatingFilter.  # noqa: E501
        :rtype: float
        """
        return self._min_rating

    @min_rating.setter
    def min_rating(self, min_rating):
        """Sets the min_rating of this RatingFilter.


        :param min_rating: The min_rating of this RatingFilter.  # noqa: E501
        :type: float
        """

        self._min_rating = min_rating

    @property
    def type(self):
        """Gets the type of this RatingFilter.  # noqa: E501


        :return: The type of this RatingFilter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RatingFilter.


        :param type: The type of this RatingFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOUBLES", "SINGLES"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(RatingFilter, dict):
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
        if not isinstance(other, RatingFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
