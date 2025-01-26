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

class AgeFilter(object):
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
        'max_age': 'float',
        'min_age': 'float'
    }

    attribute_map = {
        'max_age': 'maxAge',
        'min_age': 'minAge'
    }

    def __init__(self, max_age=None, min_age=None):  # noqa: E501
        """AgeFilter - a model defined in Swagger"""  # noqa: E501
        self._max_age = None
        self._min_age = None
        self.discriminator = None
        if max_age is not None:
            self.max_age = max_age
        if min_age is not None:
            self.min_age = min_age

    @property
    def max_age(self):
        """Gets the max_age of this AgeFilter.  # noqa: E501


        :return: The max_age of this AgeFilter.  # noqa: E501
        :rtype: float
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """Sets the max_age of this AgeFilter.


        :param max_age: The max_age of this AgeFilter.  # noqa: E501
        :type: float
        """

        self._max_age = max_age

    @property
    def min_age(self):
        """Gets the min_age of this AgeFilter.  # noqa: E501


        :return: The min_age of this AgeFilter.  # noqa: E501
        :rtype: float
        """
        return self._min_age

    @min_age.setter
    def min_age(self, min_age):
        """Sets the min_age of this AgeFilter.


        :param min_age: The min_age of this AgeFilter.  # noqa: E501
        :type: float
        """

        self._min_age = min_age

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
        if issubclass(AgeFilter, dict):
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
        if not isinstance(other, AgeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
