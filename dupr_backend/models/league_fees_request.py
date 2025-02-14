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

class LeagueFeesRequest(object):
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
        'member_fee': 'float',
        'non_member_fee': 'float'
    }

    attribute_map = {
        'member_fee': 'memberFee',
        'non_member_fee': 'nonMemberFee'
    }

    def __init__(self, member_fee=None, non_member_fee=None):  # noqa: E501
        """LeagueFeesRequest - a model defined in Swagger"""  # noqa: E501
        self._member_fee = None
        self._non_member_fee = None
        self.discriminator = None
        self.member_fee = member_fee
        self.non_member_fee = non_member_fee

    @property
    def member_fee(self):
        """Gets the member_fee of this LeagueFeesRequest.  # noqa: E501


        :return: The member_fee of this LeagueFeesRequest.  # noqa: E501
        :rtype: float
        """
        return self._member_fee

    @member_fee.setter
    def member_fee(self, member_fee):
        """Sets the member_fee of this LeagueFeesRequest.


        :param member_fee: The member_fee of this LeagueFeesRequest.  # noqa: E501
        :type: float
        """
        if member_fee is None:
            raise ValueError("Invalid value for `member_fee`, must not be `None`")  # noqa: E501

        self._member_fee = member_fee

    @property
    def non_member_fee(self):
        """Gets the non_member_fee of this LeagueFeesRequest.  # noqa: E501


        :return: The non_member_fee of this LeagueFeesRequest.  # noqa: E501
        :rtype: float
        """
        return self._non_member_fee

    @non_member_fee.setter
    def non_member_fee(self, non_member_fee):
        """Sets the non_member_fee of this LeagueFeesRequest.


        :param non_member_fee: The non_member_fee of this LeagueFeesRequest.  # noqa: E501
        :type: float
        """
        if non_member_fee is None:
            raise ValueError("Invalid value for `non_member_fee`, must not be `None`")  # noqa: E501

        self._non_member_fee = non_member_fee

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
        if issubclass(LeagueFeesRequest, dict):
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
        if not isinstance(other, LeagueFeesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
