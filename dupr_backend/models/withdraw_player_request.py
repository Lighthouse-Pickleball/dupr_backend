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

class WithdrawPlayerRequest(object):
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
        'bracket_id': 'int',
        'club_id': 'int',
        'player_id': 'int',
        'registration_id': 'int'
    }

    attribute_map = {
        'bracket_id': 'bracketId',
        'club_id': 'clubId',
        'player_id': 'playerId',
        'registration_id': 'registrationId'
    }

    def __init__(self, bracket_id=None, club_id=None, player_id=None, registration_id=None):  # noqa: E501
        """WithdrawPlayerRequest - a model defined in Swagger"""  # noqa: E501
        self._bracket_id = None
        self._club_id = None
        self._player_id = None
        self._registration_id = None
        self.discriminator = None
        self.bracket_id = bracket_id
        self.club_id = club_id
        self.player_id = player_id
        self.registration_id = registration_id

    @property
    def bracket_id(self):
        """Gets the bracket_id of this WithdrawPlayerRequest.  # noqa: E501


        :return: The bracket_id of this WithdrawPlayerRequest.  # noqa: E501
        :rtype: int
        """
        return self._bracket_id

    @bracket_id.setter
    def bracket_id(self, bracket_id):
        """Sets the bracket_id of this WithdrawPlayerRequest.


        :param bracket_id: The bracket_id of this WithdrawPlayerRequest.  # noqa: E501
        :type: int
        """
        if bracket_id is None:
            raise ValueError("Invalid value for `bracket_id`, must not be `None`")  # noqa: E501

        self._bracket_id = bracket_id

    @property
    def club_id(self):
        """Gets the club_id of this WithdrawPlayerRequest.  # noqa: E501


        :return: The club_id of this WithdrawPlayerRequest.  # noqa: E501
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id):
        """Sets the club_id of this WithdrawPlayerRequest.


        :param club_id: The club_id of this WithdrawPlayerRequest.  # noqa: E501
        :type: int
        """
        if club_id is None:
            raise ValueError("Invalid value for `club_id`, must not be `None`")  # noqa: E501

        self._club_id = club_id

    @property
    def player_id(self):
        """Gets the player_id of this WithdrawPlayerRequest.  # noqa: E501


        :return: The player_id of this WithdrawPlayerRequest.  # noqa: E501
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this WithdrawPlayerRequest.


        :param player_id: The player_id of this WithdrawPlayerRequest.  # noqa: E501
        :type: int
        """
        if player_id is None:
            raise ValueError("Invalid value for `player_id`, must not be `None`")  # noqa: E501

        self._player_id = player_id

    @property
    def registration_id(self):
        """Gets the registration_id of this WithdrawPlayerRequest.  # noqa: E501


        :return: The registration_id of this WithdrawPlayerRequest.  # noqa: E501
        :rtype: int
        """
        return self._registration_id

    @registration_id.setter
    def registration_id(self, registration_id):
        """Sets the registration_id of this WithdrawPlayerRequest.


        :param registration_id: The registration_id of this WithdrawPlayerRequest.  # noqa: E501
        :type: int
        """
        if registration_id is None:
            raise ValueError("Invalid value for `registration_id`, must not be `None`")  # noqa: E501

        self._registration_id = registration_id

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
        if issubclass(WithdrawPlayerRequest, dict):
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
        if not isinstance(other, WithdrawPlayerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
