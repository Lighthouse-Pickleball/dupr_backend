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

class FollowingInfo(object):
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
        'followers': 'int',
        'followings': 'int',
        'is_followed': 'bool'
    }

    attribute_map = {
        'followers': 'followers',
        'followings': 'followings',
        'is_followed': 'isFollowed'
    }

    def __init__(self, followers=None, followings=None, is_followed=None):  # noqa: E501
        """FollowingInfo - a model defined in Swagger"""  # noqa: E501
        self._followers = None
        self._followings = None
        self._is_followed = None
        self.discriminator = None
        if followers is not None:
            self.followers = followers
        if followings is not None:
            self.followings = followings
        if is_followed is not None:
            self.is_followed = is_followed

    @property
    def followers(self):
        """Gets the followers of this FollowingInfo.  # noqa: E501


        :return: The followers of this FollowingInfo.  # noqa: E501
        :rtype: int
        """
        return self._followers

    @followers.setter
    def followers(self, followers):
        """Sets the followers of this FollowingInfo.


        :param followers: The followers of this FollowingInfo.  # noqa: E501
        :type: int
        """

        self._followers = followers

    @property
    def followings(self):
        """Gets the followings of this FollowingInfo.  # noqa: E501


        :return: The followings of this FollowingInfo.  # noqa: E501
        :rtype: int
        """
        return self._followings

    @followings.setter
    def followings(self, followings):
        """Sets the followings of this FollowingInfo.


        :param followings: The followings of this FollowingInfo.  # noqa: E501
        :type: int
        """

        self._followings = followings

    @property
    def is_followed(self):
        """Gets the is_followed of this FollowingInfo.  # noqa: E501


        :return: The is_followed of this FollowingInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_followed

    @is_followed.setter
    def is_followed(self, is_followed):
        """Sets the is_followed of this FollowingInfo.


        :param is_followed: The is_followed of this FollowingInfo.  # noqa: E501
        :type: bool
        """

        self._is_followed = is_followed

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
        if issubclass(FollowingInfo, dict):
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
        if not isinstance(other, FollowingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
