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

class BracketUnmatchedPlayerSort(object):
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
        'order': 'str',
        'parameter': 'str'
    }

    attribute_map = {
        'order': 'order',
        'parameter': 'parameter'
    }

    def __init__(self, order=None, parameter=None):  # noqa: E501
        """BracketUnmatchedPlayerSort - a model defined in Swagger"""  # noqa: E501
        self._order = None
        self._parameter = None
        self.discriminator = None
        if order is not None:
            self.order = order
        if parameter is not None:
            self.parameter = parameter

    @property
    def order(self):
        """Gets the order of this BracketUnmatchedPlayerSort.  # noqa: E501


        :return: The order of this BracketUnmatchedPlayerSort.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this BracketUnmatchedPlayerSort.


        :param order: The order of this BracketUnmatchedPlayerSort.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"  # noqa: E501
                .format(order, allowed_values)
            )

        self._order = order

    @property
    def parameter(self):
        """Gets the parameter of this BracketUnmatchedPlayerSort.  # noqa: E501


        :return: The parameter of this BracketUnmatchedPlayerSort.  # noqa: E501
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this BracketUnmatchedPlayerSort.


        :param parameter: The parameter of this BracketUnmatchedPlayerSort.  # noqa: E501
        :type: str
        """
        allowed_values = ["RATINGS"]  # noqa: E501
        if parameter not in allowed_values:
            raise ValueError(
                "Invalid value for `parameter` ({0}), must be one of {1}"  # noqa: E501
                .format(parameter, allowed_values)
            )

        self._parameter = parameter

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
        if issubclass(BracketUnmatchedPlayerSort, dict):
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
        if not isinstance(other, BracketUnmatchedPlayerSort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
