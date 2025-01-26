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

class RatingsOverviewResponse(object):
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
        'losses': 'int',
        'pending': 'int',
        'wins': 'int'
    }

    attribute_map = {
        'losses': 'losses',
        'pending': 'pending',
        'wins': 'wins'
    }

    def __init__(self, losses=None, pending=None, wins=None):  # noqa: E501
        """RatingsOverviewResponse - a model defined in Swagger"""  # noqa: E501
        self._losses = None
        self._pending = None
        self._wins = None
        self.discriminator = None
        self.losses = losses
        self.pending = pending
        self.wins = wins

    @property
    def losses(self):
        """Gets the losses of this RatingsOverviewResponse.  # noqa: E501


        :return: The losses of this RatingsOverviewResponse.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this RatingsOverviewResponse.


        :param losses: The losses of this RatingsOverviewResponse.  # noqa: E501
        :type: int
        """
        if losses is None:
            raise ValueError("Invalid value for `losses`, must not be `None`")  # noqa: E501

        self._losses = losses

    @property
    def pending(self):
        """Gets the pending of this RatingsOverviewResponse.  # noqa: E501


        :return: The pending of this RatingsOverviewResponse.  # noqa: E501
        :rtype: int
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this RatingsOverviewResponse.


        :param pending: The pending of this RatingsOverviewResponse.  # noqa: E501
        :type: int
        """
        if pending is None:
            raise ValueError("Invalid value for `pending`, must not be `None`")  # noqa: E501

        self._pending = pending

    @property
    def wins(self):
        """Gets the wins of this RatingsOverviewResponse.  # noqa: E501


        :return: The wins of this RatingsOverviewResponse.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this RatingsOverviewResponse.


        :param wins: The wins of this RatingsOverviewResponse.  # noqa: E501
        :type: int
        """
        if wins is None:
            raise ValueError("Invalid value for `wins`, must not be `None`")  # noqa: E501

        self._wins = wins

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
        if issubclass(RatingsOverviewResponse, dict):
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
        if not isinstance(other, RatingsOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
