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

class CreateNewTeamRequest(object):
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
        'player1': 'int',
        'player2': 'int'
    }

    attribute_map = {
        'bracket_id': 'bracketId',
        'club_id': 'clubId',
        'player1': 'player1',
        'player2': 'player2'
    }

    def __init__(self, bracket_id=None, club_id=None, player1=None, player2=None):  # noqa: E501
        """CreateNewTeamRequest - a model defined in Swagger"""  # noqa: E501
        self._bracket_id = None
        self._club_id = None
        self._player1 = None
        self._player2 = None
        self.discriminator = None
        self.bracket_id = bracket_id
        self.club_id = club_id
        self.player1 = player1
        self.player2 = player2

    @property
    def bracket_id(self):
        """Gets the bracket_id of this CreateNewTeamRequest.  # noqa: E501


        :return: The bracket_id of this CreateNewTeamRequest.  # noqa: E501
        :rtype: int
        """
        return self._bracket_id

    @bracket_id.setter
    def bracket_id(self, bracket_id):
        """Sets the bracket_id of this CreateNewTeamRequest.


        :param bracket_id: The bracket_id of this CreateNewTeamRequest.  # noqa: E501
        :type: int
        """
        if bracket_id is None:
            raise ValueError("Invalid value for `bracket_id`, must not be `None`")  # noqa: E501

        self._bracket_id = bracket_id

    @property
    def club_id(self):
        """Gets the club_id of this CreateNewTeamRequest.  # noqa: E501


        :return: The club_id of this CreateNewTeamRequest.  # noqa: E501
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id):
        """Sets the club_id of this CreateNewTeamRequest.


        :param club_id: The club_id of this CreateNewTeamRequest.  # noqa: E501
        :type: int
        """
        if club_id is None:
            raise ValueError("Invalid value for `club_id`, must not be `None`")  # noqa: E501

        self._club_id = club_id

    @property
    def player1(self):
        """Gets the player1 of this CreateNewTeamRequest.  # noqa: E501


        :return: The player1 of this CreateNewTeamRequest.  # noqa: E501
        :rtype: int
        """
        return self._player1

    @player1.setter
    def player1(self, player1):
        """Sets the player1 of this CreateNewTeamRequest.


        :param player1: The player1 of this CreateNewTeamRequest.  # noqa: E501
        :type: int
        """
        if player1 is None:
            raise ValueError("Invalid value for `player1`, must not be `None`")  # noqa: E501

        self._player1 = player1

    @property
    def player2(self):
        """Gets the player2 of this CreateNewTeamRequest.  # noqa: E501


        :return: The player2 of this CreateNewTeamRequest.  # noqa: E501
        :rtype: int
        """
        return self._player2

    @player2.setter
    def player2(self, player2):
        """Sets the player2 of this CreateNewTeamRequest.


        :param player2: The player2 of this CreateNewTeamRequest.  # noqa: E501
        :type: int
        """
        if player2 is None:
            raise ValueError("Invalid value for `player2`, must not be `None`")  # noqa: E501

        self._player2 = player2

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
        if issubclass(CreateNewTeamRequest, dict):
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
        if not isinstance(other, CreateNewTeamRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
