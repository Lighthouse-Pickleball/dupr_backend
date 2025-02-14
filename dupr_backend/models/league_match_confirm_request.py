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

class LeagueMatchConfirmRequest(object):
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
        'league_match_id': 'int',
        'match_id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'league_match_id': 'leagueMatchId',
        'match_id': 'matchId',
        'user_id': 'userId'
    }

    def __init__(self, league_match_id=None, match_id=None, user_id=None):  # noqa: E501
        """LeagueMatchConfirmRequest - a model defined in Swagger"""  # noqa: E501
        self._league_match_id = None
        self._match_id = None
        self._user_id = None
        self.discriminator = None
        if league_match_id is not None:
            self.league_match_id = league_match_id
        self.match_id = match_id
        self.user_id = user_id

    @property
    def league_match_id(self):
        """Gets the league_match_id of this LeagueMatchConfirmRequest.  # noqa: E501


        :return: The league_match_id of this LeagueMatchConfirmRequest.  # noqa: E501
        :rtype: int
        """
        return self._league_match_id

    @league_match_id.setter
    def league_match_id(self, league_match_id):
        """Sets the league_match_id of this LeagueMatchConfirmRequest.


        :param league_match_id: The league_match_id of this LeagueMatchConfirmRequest.  # noqa: E501
        :type: int
        """

        self._league_match_id = league_match_id

    @property
    def match_id(self):
        """Gets the match_id of this LeagueMatchConfirmRequest.  # noqa: E501


        :return: The match_id of this LeagueMatchConfirmRequest.  # noqa: E501
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """Sets the match_id of this LeagueMatchConfirmRequest.


        :param match_id: The match_id of this LeagueMatchConfirmRequest.  # noqa: E501
        :type: int
        """
        if match_id is None:
            raise ValueError("Invalid value for `match_id`, must not be `None`")  # noqa: E501

        self._match_id = match_id

    @property
    def user_id(self):
        """Gets the user_id of this LeagueMatchConfirmRequest.  # noqa: E501


        :return: The user_id of this LeagueMatchConfirmRequest.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this LeagueMatchConfirmRequest.


        :param user_id: The user_id of this LeagueMatchConfirmRequest.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if issubclass(LeagueMatchConfirmRequest, dict):
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
        if not isinstance(other, LeagueMatchConfirmRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
