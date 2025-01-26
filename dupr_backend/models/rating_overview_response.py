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

class RatingOverviewResponse(object):
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
        'all': 'OverviewResponse',
        'doubles': 'OverviewResponse',
        'singles': 'OverviewResponse'
    }

    attribute_map = {
        'all': 'all',
        'doubles': 'doubles',
        'singles': 'singles'
    }

    def __init__(self, all=None, doubles=None, singles=None):  # noqa: E501
        """RatingOverviewResponse - a model defined in Swagger"""  # noqa: E501
        self._all = None
        self._doubles = None
        self._singles = None
        self.discriminator = None
        self.all = all
        self.doubles = doubles
        self.singles = singles

    @property
    def all(self):
        """Gets the all of this RatingOverviewResponse.  # noqa: E501


        :return: The all of this RatingOverviewResponse.  # noqa: E501
        :rtype: OverviewResponse
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this RatingOverviewResponse.


        :param all: The all of this RatingOverviewResponse.  # noqa: E501
        :type: OverviewResponse
        """
        if all is None:
            raise ValueError("Invalid value for `all`, must not be `None`")  # noqa: E501

        self._all = all

    @property
    def doubles(self):
        """Gets the doubles of this RatingOverviewResponse.  # noqa: E501


        :return: The doubles of this RatingOverviewResponse.  # noqa: E501
        :rtype: OverviewResponse
        """
        return self._doubles

    @doubles.setter
    def doubles(self, doubles):
        """Sets the doubles of this RatingOverviewResponse.


        :param doubles: The doubles of this RatingOverviewResponse.  # noqa: E501
        :type: OverviewResponse
        """
        if doubles is None:
            raise ValueError("Invalid value for `doubles`, must not be `None`")  # noqa: E501

        self._doubles = doubles

    @property
    def singles(self):
        """Gets the singles of this RatingOverviewResponse.  # noqa: E501


        :return: The singles of this RatingOverviewResponse.  # noqa: E501
        :rtype: OverviewResponse
        """
        return self._singles

    @singles.setter
    def singles(self, singles):
        """Sets the singles of this RatingOverviewResponse.


        :param singles: The singles of this RatingOverviewResponse.  # noqa: E501
        :type: OverviewResponse
        """
        if singles is None:
            raise ValueError("Invalid value for `singles`, must not be `None`")  # noqa: E501

        self._singles = singles

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
        if issubclass(RatingOverviewResponse, dict):
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
        if not isinstance(other, RatingOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
