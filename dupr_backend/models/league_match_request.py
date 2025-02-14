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

class LeagueMatchRequest(object):
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
        'event_name': 'str',
        'format': 'str',
        'league': 'str',
        'league_id': 'int',
        'league_match_id': 'int',
        'location': 'str',
        'match_date': 'date',
        'score_format_id': 'int',
        'team1': 'Team',
        'team2': 'Team',
        'tournament': 'str',
        'venue': 'str'
    }

    attribute_map = {
        'bracket_id': 'bracketId',
        'club_id': 'clubId',
        'event_name': 'eventName',
        'format': 'format',
        'league': 'league',
        'league_id': 'leagueId',
        'league_match_id': 'leagueMatchId',
        'location': 'location',
        'match_date': 'matchDate',
        'score_format_id': 'scoreFormatId',
        'team1': 'team1',
        'team2': 'team2',
        'tournament': 'tournament',
        'venue': 'venue'
    }

    def __init__(self, bracket_id=None, club_id=None, event_name=None, format=None, league=None, league_id=None, league_match_id=None, location=None, match_date=None, score_format_id=None, team1=None, team2=None, tournament=None, venue=None):  # noqa: E501
        """LeagueMatchRequest - a model defined in Swagger"""  # noqa: E501
        self._bracket_id = None
        self._club_id = None
        self._event_name = None
        self._format = None
        self._league = None
        self._league_id = None
        self._league_match_id = None
        self._location = None
        self._match_date = None
        self._score_format_id = None
        self._team1 = None
        self._team2 = None
        self._tournament = None
        self._venue = None
        self.discriminator = None
        self.bracket_id = bracket_id
        self.club_id = club_id
        if event_name is not None:
            self.event_name = event_name
        self.format = format
        if league is not None:
            self.league = league
        self.league_id = league_id
        self.league_match_id = league_match_id
        if location is not None:
            self.location = location
        self.match_date = match_date
        if score_format_id is not None:
            self.score_format_id = score_format_id
        self.team1 = team1
        self.team2 = team2
        if tournament is not None:
            self.tournament = tournament
        if venue is not None:
            self.venue = venue

    @property
    def bracket_id(self):
        """Gets the bracket_id of this LeagueMatchRequest.  # noqa: E501


        :return: The bracket_id of this LeagueMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._bracket_id

    @bracket_id.setter
    def bracket_id(self, bracket_id):
        """Sets the bracket_id of this LeagueMatchRequest.


        :param bracket_id: The bracket_id of this LeagueMatchRequest.  # noqa: E501
        :type: int
        """
        if bracket_id is None:
            raise ValueError("Invalid value for `bracket_id`, must not be `None`")  # noqa: E501

        self._bracket_id = bracket_id

    @property
    def club_id(self):
        """Gets the club_id of this LeagueMatchRequest.  # noqa: E501


        :return: The club_id of this LeagueMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id):
        """Sets the club_id of this LeagueMatchRequest.


        :param club_id: The club_id of this LeagueMatchRequest.  # noqa: E501
        :type: int
        """
        if club_id is None:
            raise ValueError("Invalid value for `club_id`, must not be `None`")  # noqa: E501

        self._club_id = club_id

    @property
    def event_name(self):
        """Gets the event_name of this LeagueMatchRequest.  # noqa: E501


        :return: The event_name of this LeagueMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this LeagueMatchRequest.


        :param event_name: The event_name of this LeagueMatchRequest.  # noqa: E501
        :type: str
        """

        self._event_name = event_name

    @property
    def format(self):
        """Gets the format of this LeagueMatchRequest.  # noqa: E501


        :return: The format of this LeagueMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this LeagueMatchRequest.


        :param format: The format of this LeagueMatchRequest.  # noqa: E501
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["DOUBLES", "SINGLES"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def league(self):
        """Gets the league of this LeagueMatchRequest.  # noqa: E501


        :return: The league of this LeagueMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this LeagueMatchRequest.


        :param league: The league of this LeagueMatchRequest.  # noqa: E501
        :type: str
        """

        self._league = league

    @property
    def league_id(self):
        """Gets the league_id of this LeagueMatchRequest.  # noqa: E501


        :return: The league_id of this LeagueMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this LeagueMatchRequest.


        :param league_id: The league_id of this LeagueMatchRequest.  # noqa: E501
        :type: int
        """
        if league_id is None:
            raise ValueError("Invalid value for `league_id`, must not be `None`")  # noqa: E501

        self._league_id = league_id

    @property
    def league_match_id(self):
        """Gets the league_match_id of this LeagueMatchRequest.  # noqa: E501


        :return: The league_match_id of this LeagueMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._league_match_id

    @league_match_id.setter
    def league_match_id(self, league_match_id):
        """Sets the league_match_id of this LeagueMatchRequest.


        :param league_match_id: The league_match_id of this LeagueMatchRequest.  # noqa: E501
        :type: int
        """
        if league_match_id is None:
            raise ValueError("Invalid value for `league_match_id`, must not be `None`")  # noqa: E501

        self._league_match_id = league_match_id

    @property
    def location(self):
        """Gets the location of this LeagueMatchRequest.  # noqa: E501


        :return: The location of this LeagueMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this LeagueMatchRequest.


        :param location: The location of this LeagueMatchRequest.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def match_date(self):
        """Gets the match_date of this LeagueMatchRequest.  # noqa: E501


        :return: The match_date of this LeagueMatchRequest.  # noqa: E501
        :rtype: date
        """
        return self._match_date

    @match_date.setter
    def match_date(self, match_date):
        """Sets the match_date of this LeagueMatchRequest.


        :param match_date: The match_date of this LeagueMatchRequest.  # noqa: E501
        :type: date
        """
        if match_date is None:
            raise ValueError("Invalid value for `match_date`, must not be `None`")  # noqa: E501

        self._match_date = match_date

    @property
    def score_format_id(self):
        """Gets the score_format_id of this LeagueMatchRequest.  # noqa: E501


        :return: The score_format_id of this LeagueMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._score_format_id

    @score_format_id.setter
    def score_format_id(self, score_format_id):
        """Sets the score_format_id of this LeagueMatchRequest.


        :param score_format_id: The score_format_id of this LeagueMatchRequest.  # noqa: E501
        :type: int
        """

        self._score_format_id = score_format_id

    @property
    def team1(self):
        """Gets the team1 of this LeagueMatchRequest.  # noqa: E501


        :return: The team1 of this LeagueMatchRequest.  # noqa: E501
        :rtype: Team
        """
        return self._team1

    @team1.setter
    def team1(self, team1):
        """Sets the team1 of this LeagueMatchRequest.


        :param team1: The team1 of this LeagueMatchRequest.  # noqa: E501
        :type: Team
        """
        if team1 is None:
            raise ValueError("Invalid value for `team1`, must not be `None`")  # noqa: E501

        self._team1 = team1

    @property
    def team2(self):
        """Gets the team2 of this LeagueMatchRequest.  # noqa: E501


        :return: The team2 of this LeagueMatchRequest.  # noqa: E501
        :rtype: Team
        """
        return self._team2

    @team2.setter
    def team2(self, team2):
        """Sets the team2 of this LeagueMatchRequest.


        :param team2: The team2 of this LeagueMatchRequest.  # noqa: E501
        :type: Team
        """
        if team2 is None:
            raise ValueError("Invalid value for `team2`, must not be `None`")  # noqa: E501

        self._team2 = team2

    @property
    def tournament(self):
        """Gets the tournament of this LeagueMatchRequest.  # noqa: E501


        :return: The tournament of this LeagueMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._tournament

    @tournament.setter
    def tournament(self, tournament):
        """Sets the tournament of this LeagueMatchRequest.


        :param tournament: The tournament of this LeagueMatchRequest.  # noqa: E501
        :type: str
        """

        self._tournament = tournament

    @property
    def venue(self):
        """Gets the venue of this LeagueMatchRequest.  # noqa: E501


        :return: The venue of this LeagueMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this LeagueMatchRequest.


        :param venue: The venue of this LeagueMatchRequest.  # noqa: E501
        :type: str
        """

        self._venue = venue

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
        if issubclass(LeagueMatchRequest, dict):
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
        if not isinstance(other, LeagueMatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
