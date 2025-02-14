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

class MatchRequest(object):
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
        'club_id': 'int',
        'event': 'str',
        'event_date': 'date',
        'format': 'str',
        'league': 'str',
        'location': 'str',
        'match_type': 'str',
        'notify': 'bool',
        'score_format_id': 'int',
        'scores': 'list[PairOfintAndint]',
        'team1': 'Team',
        'team2': 'Team',
        'tournament': 'str',
        'venue': 'str'
    }

    attribute_map = {
        'club_id': 'clubId',
        'event': 'event',
        'event_date': 'eventDate',
        'format': 'format',
        'league': 'league',
        'location': 'location',
        'match_type': 'matchType',
        'notify': 'notify',
        'score_format_id': 'scoreFormatId',
        'scores': 'scores',
        'team1': 'team1',
        'team2': 'team2',
        'tournament': 'tournament',
        'venue': 'venue'
    }

    def __init__(self, club_id=None, event=None, event_date=None, format=None, league=None, location=None, match_type=None, notify=None, score_format_id=None, scores=None, team1=None, team2=None, tournament=None, venue=None):  # noqa: E501
        """MatchRequest - a model defined in Swagger"""  # noqa: E501
        self._club_id = None
        self._event = None
        self._event_date = None
        self._format = None
        self._league = None
        self._location = None
        self._match_type = None
        self._notify = None
        self._score_format_id = None
        self._scores = None
        self._team1 = None
        self._team2 = None
        self._tournament = None
        self._venue = None
        self.discriminator = None
        if club_id is not None:
            self.club_id = club_id
        if event is not None:
            self.event = event
        self.event_date = event_date
        self.format = format
        if league is not None:
            self.league = league
        if location is not None:
            self.location = location
        if match_type is not None:
            self.match_type = match_type
        if notify is not None:
            self.notify = notify
        if score_format_id is not None:
            self.score_format_id = score_format_id
        self.scores = scores
        self.team1 = team1
        self.team2 = team2
        if tournament is not None:
            self.tournament = tournament
        if venue is not None:
            self.venue = venue

    @property
    def club_id(self):
        """Gets the club_id of this MatchRequest.  # noqa: E501


        :return: The club_id of this MatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id):
        """Sets the club_id of this MatchRequest.


        :param club_id: The club_id of this MatchRequest.  # noqa: E501
        :type: int
        """

        self._club_id = club_id

    @property
    def event(self):
        """Gets the event of this MatchRequest.  # noqa: E501


        :return: The event of this MatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this MatchRequest.


        :param event: The event of this MatchRequest.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def event_date(self):
        """Gets the event_date of this MatchRequest.  # noqa: E501


        :return: The event_date of this MatchRequest.  # noqa: E501
        :rtype: date
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this MatchRequest.


        :param event_date: The event_date of this MatchRequest.  # noqa: E501
        :type: date
        """
        if event_date is None:
            raise ValueError("Invalid value for `event_date`, must not be `None`")  # noqa: E501

        self._event_date = event_date

    @property
    def format(self):
        """Gets the format of this MatchRequest.  # noqa: E501


        :return: The format of this MatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this MatchRequest.


        :param format: The format of this MatchRequest.  # noqa: E501
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
        """Gets the league of this MatchRequest.  # noqa: E501


        :return: The league of this MatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this MatchRequest.


        :param league: The league of this MatchRequest.  # noqa: E501
        :type: str
        """

        self._league = league

    @property
    def location(self):
        """Gets the location of this MatchRequest.  # noqa: E501


        :return: The location of this MatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this MatchRequest.


        :param location: The location of this MatchRequest.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def match_type(self):
        """Gets the match_type of this MatchRequest.  # noqa: E501


        :return: The match_type of this MatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this MatchRequest.


        :param match_type: The match_type of this MatchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["RALLY", "SIDE_ONLY"]  # noqa: E501
        if match_type not in allowed_values:
            raise ValueError(
                "Invalid value for `match_type` ({0}), must be one of {1}"  # noqa: E501
                .format(match_type, allowed_values)
            )

        self._match_type = match_type

    @property
    def notify(self):
        """Gets the notify of this MatchRequest.  # noqa: E501


        :return: The notify of this MatchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this MatchRequest.


        :param notify: The notify of this MatchRequest.  # noqa: E501
        :type: bool
        """

        self._notify = notify

    @property
    def score_format_id(self):
        """Gets the score_format_id of this MatchRequest.  # noqa: E501


        :return: The score_format_id of this MatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._score_format_id

    @score_format_id.setter
    def score_format_id(self, score_format_id):
        """Sets the score_format_id of this MatchRequest.


        :param score_format_id: The score_format_id of this MatchRequest.  # noqa: E501
        :type: int
        """

        self._score_format_id = score_format_id

    @property
    def scores(self):
        """Gets the scores of this MatchRequest.  # noqa: E501


        :return: The scores of this MatchRequest.  # noqa: E501
        :rtype: list[PairOfintAndint]
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """Sets the scores of this MatchRequest.


        :param scores: The scores of this MatchRequest.  # noqa: E501
        :type: list[PairOfintAndint]
        """
        if scores is None:
            raise ValueError("Invalid value for `scores`, must not be `None`")  # noqa: E501

        self._scores = scores

    @property
    def team1(self):
        """Gets the team1 of this MatchRequest.  # noqa: E501


        :return: The team1 of this MatchRequest.  # noqa: E501
        :rtype: Team
        """
        return self._team1

    @team1.setter
    def team1(self, team1):
        """Sets the team1 of this MatchRequest.


        :param team1: The team1 of this MatchRequest.  # noqa: E501
        :type: Team
        """
        if team1 is None:
            raise ValueError("Invalid value for `team1`, must not be `None`")  # noqa: E501

        self._team1 = team1

    @property
    def team2(self):
        """Gets the team2 of this MatchRequest.  # noqa: E501


        :return: The team2 of this MatchRequest.  # noqa: E501
        :rtype: Team
        """
        return self._team2

    @team2.setter
    def team2(self, team2):
        """Sets the team2 of this MatchRequest.


        :param team2: The team2 of this MatchRequest.  # noqa: E501
        :type: Team
        """
        if team2 is None:
            raise ValueError("Invalid value for `team2`, must not be `None`")  # noqa: E501

        self._team2 = team2

    @property
    def tournament(self):
        """Gets the tournament of this MatchRequest.  # noqa: E501


        :return: The tournament of this MatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._tournament

    @tournament.setter
    def tournament(self, tournament):
        """Sets the tournament of this MatchRequest.


        :param tournament: The tournament of this MatchRequest.  # noqa: E501
        :type: str
        """

        self._tournament = tournament

    @property
    def venue(self):
        """Gets the venue of this MatchRequest.  # noqa: E501


        :return: The venue of this MatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this MatchRequest.


        :param venue: The venue of this MatchRequest.  # noqa: E501
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
        if issubclass(MatchRequest, dict):
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
        if not isinstance(other, MatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
