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

class LeagueStandingResponse(object):
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
        'game_lost': 'int',
        'game_won': 'int',
        'match_lost': 'int',
        'match_won': 'int',
        'player1': 'PlayerResponse',
        'player2': 'PlayerResponse',
        'point_diff_percentage': 'float',
        'point_difference': 'int',
        'points_conceded': 'int',
        'points_scored': 'int',
        'rank': 'int',
        'registration_id': 'int',
        'round': 'int'
    }

    attribute_map = {
        'bracket_id': 'bracketId',
        'game_lost': 'gameLost',
        'game_won': 'gameWon',
        'match_lost': 'matchLost',
        'match_won': 'matchWon',
        'player1': 'player1',
        'player2': 'player2',
        'point_diff_percentage': 'pointDiffPercentage',
        'point_difference': 'pointDifference',
        'points_conceded': 'pointsConceded',
        'points_scored': 'pointsScored',
        'rank': 'rank',
        'registration_id': 'registrationId',
        'round': 'round'
    }

    def __init__(self, bracket_id=None, game_lost=None, game_won=None, match_lost=None, match_won=None, player1=None, player2=None, point_diff_percentage=None, point_difference=None, points_conceded=None, points_scored=None, rank=None, registration_id=None, round=None):  # noqa: E501
        """LeagueStandingResponse - a model defined in Swagger"""  # noqa: E501
        self._bracket_id = None
        self._game_lost = None
        self._game_won = None
        self._match_lost = None
        self._match_won = None
        self._player1 = None
        self._player2 = None
        self._point_diff_percentage = None
        self._point_difference = None
        self._points_conceded = None
        self._points_scored = None
        self._rank = None
        self._registration_id = None
        self._round = None
        self.discriminator = None
        self.bracket_id = bracket_id
        if game_lost is not None:
            self.game_lost = game_lost
        if game_won is not None:
            self.game_won = game_won
        if match_lost is not None:
            self.match_lost = match_lost
        if match_won is not None:
            self.match_won = match_won
        if player1 is not None:
            self.player1 = player1
        if player2 is not None:
            self.player2 = player2
        if point_diff_percentage is not None:
            self.point_diff_percentage = point_diff_percentage
        if point_difference is not None:
            self.point_difference = point_difference
        if points_conceded is not None:
            self.points_conceded = points_conceded
        if points_scored is not None:
            self.points_scored = points_scored
        if rank is not None:
            self.rank = rank
        self.registration_id = registration_id
        self.round = round

    @property
    def bracket_id(self):
        """Gets the bracket_id of this LeagueStandingResponse.  # noqa: E501


        :return: The bracket_id of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._bracket_id

    @bracket_id.setter
    def bracket_id(self, bracket_id):
        """Sets the bracket_id of this LeagueStandingResponse.


        :param bracket_id: The bracket_id of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """
        if bracket_id is None:
            raise ValueError("Invalid value for `bracket_id`, must not be `None`")  # noqa: E501

        self._bracket_id = bracket_id

    @property
    def game_lost(self):
        """Gets the game_lost of this LeagueStandingResponse.  # noqa: E501


        :return: The game_lost of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._game_lost

    @game_lost.setter
    def game_lost(self, game_lost):
        """Sets the game_lost of this LeagueStandingResponse.


        :param game_lost: The game_lost of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """

        self._game_lost = game_lost

    @property
    def game_won(self):
        """Gets the game_won of this LeagueStandingResponse.  # noqa: E501


        :return: The game_won of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._game_won

    @game_won.setter
    def game_won(self, game_won):
        """Sets the game_won of this LeagueStandingResponse.


        :param game_won: The game_won of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """

        self._game_won = game_won

    @property
    def match_lost(self):
        """Gets the match_lost of this LeagueStandingResponse.  # noqa: E501


        :return: The match_lost of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._match_lost

    @match_lost.setter
    def match_lost(self, match_lost):
        """Sets the match_lost of this LeagueStandingResponse.


        :param match_lost: The match_lost of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """

        self._match_lost = match_lost

    @property
    def match_won(self):
        """Gets the match_won of this LeagueStandingResponse.  # noqa: E501


        :return: The match_won of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._match_won

    @match_won.setter
    def match_won(self, match_won):
        """Sets the match_won of this LeagueStandingResponse.


        :param match_won: The match_won of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """

        self._match_won = match_won

    @property
    def player1(self):
        """Gets the player1 of this LeagueStandingResponse.  # noqa: E501


        :return: The player1 of this LeagueStandingResponse.  # noqa: E501
        :rtype: PlayerResponse
        """
        return self._player1

    @player1.setter
    def player1(self, player1):
        """Sets the player1 of this LeagueStandingResponse.


        :param player1: The player1 of this LeagueStandingResponse.  # noqa: E501
        :type: PlayerResponse
        """

        self._player1 = player1

    @property
    def player2(self):
        """Gets the player2 of this LeagueStandingResponse.  # noqa: E501


        :return: The player2 of this LeagueStandingResponse.  # noqa: E501
        :rtype: PlayerResponse
        """
        return self._player2

    @player2.setter
    def player2(self, player2):
        """Sets the player2 of this LeagueStandingResponse.


        :param player2: The player2 of this LeagueStandingResponse.  # noqa: E501
        :type: PlayerResponse
        """

        self._player2 = player2

    @property
    def point_diff_percentage(self):
        """Gets the point_diff_percentage of this LeagueStandingResponse.  # noqa: E501


        :return: The point_diff_percentage of this LeagueStandingResponse.  # noqa: E501
        :rtype: float
        """
        return self._point_diff_percentage

    @point_diff_percentage.setter
    def point_diff_percentage(self, point_diff_percentage):
        """Sets the point_diff_percentage of this LeagueStandingResponse.


        :param point_diff_percentage: The point_diff_percentage of this LeagueStandingResponse.  # noqa: E501
        :type: float
        """

        self._point_diff_percentage = point_diff_percentage

    @property
    def point_difference(self):
        """Gets the point_difference of this LeagueStandingResponse.  # noqa: E501


        :return: The point_difference of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._point_difference

    @point_difference.setter
    def point_difference(self, point_difference):
        """Sets the point_difference of this LeagueStandingResponse.


        :param point_difference: The point_difference of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """

        self._point_difference = point_difference

    @property
    def points_conceded(self):
        """Gets the points_conceded of this LeagueStandingResponse.  # noqa: E501


        :return: The points_conceded of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._points_conceded

    @points_conceded.setter
    def points_conceded(self, points_conceded):
        """Sets the points_conceded of this LeagueStandingResponse.


        :param points_conceded: The points_conceded of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """

        self._points_conceded = points_conceded

    @property
    def points_scored(self):
        """Gets the points_scored of this LeagueStandingResponse.  # noqa: E501


        :return: The points_scored of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._points_scored

    @points_scored.setter
    def points_scored(self, points_scored):
        """Sets the points_scored of this LeagueStandingResponse.


        :param points_scored: The points_scored of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """

        self._points_scored = points_scored

    @property
    def rank(self):
        """Gets the rank of this LeagueStandingResponse.  # noqa: E501


        :return: The rank of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this LeagueStandingResponse.


        :param rank: The rank of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def registration_id(self):
        """Gets the registration_id of this LeagueStandingResponse.  # noqa: E501


        :return: The registration_id of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._registration_id

    @registration_id.setter
    def registration_id(self, registration_id):
        """Sets the registration_id of this LeagueStandingResponse.


        :param registration_id: The registration_id of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """
        if registration_id is None:
            raise ValueError("Invalid value for `registration_id`, must not be `None`")  # noqa: E501

        self._registration_id = registration_id

    @property
    def round(self):
        """Gets the round of this LeagueStandingResponse.  # noqa: E501


        :return: The round of this LeagueStandingResponse.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this LeagueStandingResponse.


        :param round: The round of this LeagueStandingResponse.  # noqa: E501
        :type: int
        """
        if round is None:
            raise ValueError("Invalid value for `round`, must not be `None`")  # noqa: E501

        self._round = round

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
        if issubclass(LeagueStandingResponse, dict):
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
        if not isinstance(other, LeagueStandingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
