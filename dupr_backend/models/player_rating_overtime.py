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

class PlayerRatingOvertime(object):
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
        'player_id': 'int',
        'rating_history': 'list[History]',
        'type': 'str'
    }

    attribute_map = {
        'player_id': 'playerId',
        'rating_history': 'ratingHistory',
        'type': 'type'
    }

    def __init__(self, player_id=None, rating_history=None, type=None):  # noqa: E501
        """PlayerRatingOvertime - a model defined in Swagger"""  # noqa: E501
        self._player_id = None
        self._rating_history = None
        self._type = None
        self.discriminator = None
        self.player_id = player_id
        self.rating_history = rating_history
        self.type = type

    @property
    def player_id(self):
        """Gets the player_id of this PlayerRatingOvertime.  # noqa: E501


        :return: The player_id of this PlayerRatingOvertime.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this PlayerRatingOvertime.


        :param player_id: The player_id of this PlayerRatingOvertime.  # noqa: E501
        :type: int
        """
        if player_id is None:
            raise ValueError("Invalid value for `player_id`, must not be `None`")  # noqa: E501

        self._player_id = player_id

    @property
    def rating_history(self):
        """Gets the rating_history of this PlayerRatingOvertime.  # noqa: E501


        :return: The rating_history of this PlayerRatingOvertime.  # noqa: E501
        :rtype: list[History]
        """
        return self._rating_history

    @rating_history.setter
    def rating_history(self, rating_history):
        """Sets the rating_history of this PlayerRatingOvertime.


        :param rating_history: The rating_history of this PlayerRatingOvertime.  # noqa: E501
        :type: list[History]
        """
        if rating_history is None:
            raise ValueError("Invalid value for `rating_history`, must not be `None`")  # noqa: E501

        self._rating_history = rating_history

    @property
    def type(self):
        """Gets the type of this PlayerRatingOvertime.  # noqa: E501


        :return: The type of this PlayerRatingOvertime.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlayerRatingOvertime.


        :param type: The type of this PlayerRatingOvertime.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
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
        if issubclass(PlayerRatingOvertime, dict):
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
        if not isinstance(other, PlayerRatingOvertime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
