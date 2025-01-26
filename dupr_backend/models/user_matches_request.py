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

class UserMatchesRequest(object):
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
        'league_match_id': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'bracket_id': 'bracketId',
        'club_id': 'clubId',
        'league_match_id': 'leagueMatchId',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, bracket_id=None, club_id=None, league_match_id=None, limit=None, offset=None):  # noqa: E501
        """UserMatchesRequest - a model defined in Swagger"""  # noqa: E501
        self._bracket_id = None
        self._club_id = None
        self._league_match_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None
        self.bracket_id = bracket_id
        self.club_id = club_id
        self.league_match_id = league_match_id
        self.limit = limit
        self.offset = offset

    @property
    def bracket_id(self):
        """Gets the bracket_id of this UserMatchesRequest.  # noqa: E501


        :return: The bracket_id of this UserMatchesRequest.  # noqa: E501
        :rtype: int
        """
        return self._bracket_id

    @bracket_id.setter
    def bracket_id(self, bracket_id):
        """Sets the bracket_id of this UserMatchesRequest.


        :param bracket_id: The bracket_id of this UserMatchesRequest.  # noqa: E501
        :type: int
        """
        if bracket_id is None:
            raise ValueError("Invalid value for `bracket_id`, must not be `None`")  # noqa: E501

        self._bracket_id = bracket_id

    @property
    def club_id(self):
        """Gets the club_id of this UserMatchesRequest.  # noqa: E501


        :return: The club_id of this UserMatchesRequest.  # noqa: E501
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id):
        """Sets the club_id of this UserMatchesRequest.


        :param club_id: The club_id of this UserMatchesRequest.  # noqa: E501
        :type: int
        """
        if club_id is None:
            raise ValueError("Invalid value for `club_id`, must not be `None`")  # noqa: E501

        self._club_id = club_id

    @property
    def league_match_id(self):
        """Gets the league_match_id of this UserMatchesRequest.  # noqa: E501


        :return: The league_match_id of this UserMatchesRequest.  # noqa: E501
        :rtype: int
        """
        return self._league_match_id

    @league_match_id.setter
    def league_match_id(self, league_match_id):
        """Sets the league_match_id of this UserMatchesRequest.


        :param league_match_id: The league_match_id of this UserMatchesRequest.  # noqa: E501
        :type: int
        """
        if league_match_id is None:
            raise ValueError("Invalid value for `league_match_id`, must not be `None`")  # noqa: E501

        self._league_match_id = league_match_id

    @property
    def limit(self):
        """Gets the limit of this UserMatchesRequest.  # noqa: E501


        :return: The limit of this UserMatchesRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this UserMatchesRequest.


        :param limit: The limit of this UserMatchesRequest.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this UserMatchesRequest.  # noqa: E501


        :return: The offset of this UserMatchesRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this UserMatchesRequest.


        :param offset: The offset of this UserMatchesRequest.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

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
        if issubclass(UserMatchesRequest, dict):
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
        if not isinstance(other, UserMatchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
