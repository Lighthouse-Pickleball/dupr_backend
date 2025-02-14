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

class VerifiedMatchRequest(object):
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
        'event_date': 'str',
        'event_name': 'str',
        'location': 'str',
        'team_a_player1': 'str',
        'team_a_player1_id': 'str',
        'team_a_player2': 'str',
        'team_a_player2_id': 'str',
        'team_a_points_game1': 'int',
        'team_a_points_game2': 'int',
        'team_a_points_game3': 'int',
        'team_a_points_game4': 'int',
        'team_a_points_game5': 'int',
        'team_b_player1': 'str',
        'team_b_player1_id': 'str',
        'team_b_player2': 'str',
        'team_b_player2_id': 'str',
        'team_b_points_game1': 'int',
        'team_b_points_game2': 'int',
        'team_b_points_game3': 'int',
        'team_b_points_game4': 'int',
        'team_b_points_game5': 'int',
        'tournament_name': 'str',
        'venue': 'str',
        'winning_team': 'str'
    }

    attribute_map = {
        'club_id': 'clubId',
        'event_date': 'eventDate',
        'event_name': 'eventName',
        'location': 'location',
        'team_a_player1': 'teamAPlayer1',
        'team_a_player1_id': 'teamAPlayer1ID',
        'team_a_player2': 'teamAPlayer2',
        'team_a_player2_id': 'teamAPlayer2ID',
        'team_a_points_game1': 'teamAPointsGame1',
        'team_a_points_game2': 'teamAPointsGame2',
        'team_a_points_game3': 'teamAPointsGame3',
        'team_a_points_game4': 'teamAPointsGame4',
        'team_a_points_game5': 'teamAPointsGame5',
        'team_b_player1': 'teamBPlayer1',
        'team_b_player1_id': 'teamBPlayer1ID',
        'team_b_player2': 'teamBPlayer2',
        'team_b_player2_id': 'teamBPlayer2ID',
        'team_b_points_game1': 'teamBPointsGame1',
        'team_b_points_game2': 'teamBPointsGame2',
        'team_b_points_game3': 'teamBPointsGame3',
        'team_b_points_game4': 'teamBPointsGame4',
        'team_b_points_game5': 'teamBPointsGame5',
        'tournament_name': 'tournamentName',
        'venue': 'venue',
        'winning_team': 'winningTeam'
    }

    def __init__(self, club_id=None, event_date=None, event_name=None, location=None, team_a_player1=None, team_a_player1_id=None, team_a_player2=None, team_a_player2_id=None, team_a_points_game1=None, team_a_points_game2=None, team_a_points_game3=None, team_a_points_game4=None, team_a_points_game5=None, team_b_player1=None, team_b_player1_id=None, team_b_player2=None, team_b_player2_id=None, team_b_points_game1=None, team_b_points_game2=None, team_b_points_game3=None, team_b_points_game4=None, team_b_points_game5=None, tournament_name=None, venue=None, winning_team=None):  # noqa: E501
        """VerifiedMatchRequest - a model defined in Swagger"""  # noqa: E501
        self._club_id = None
        self._event_date = None
        self._event_name = None
        self._location = None
        self._team_a_player1 = None
        self._team_a_player1_id = None
        self._team_a_player2 = None
        self._team_a_player2_id = None
        self._team_a_points_game1 = None
        self._team_a_points_game2 = None
        self._team_a_points_game3 = None
        self._team_a_points_game4 = None
        self._team_a_points_game5 = None
        self._team_b_player1 = None
        self._team_b_player1_id = None
        self._team_b_player2 = None
        self._team_b_player2_id = None
        self._team_b_points_game1 = None
        self._team_b_points_game2 = None
        self._team_b_points_game3 = None
        self._team_b_points_game4 = None
        self._team_b_points_game5 = None
        self._tournament_name = None
        self._venue = None
        self._winning_team = None
        self.discriminator = None
        if club_id is not None:
            self.club_id = club_id
        if event_date is not None:
            self.event_date = event_date
        if event_name is not None:
            self.event_name = event_name
        if location is not None:
            self.location = location
        if team_a_player1 is not None:
            self.team_a_player1 = team_a_player1
        if team_a_player1_id is not None:
            self.team_a_player1_id = team_a_player1_id
        if team_a_player2 is not None:
            self.team_a_player2 = team_a_player2
        if team_a_player2_id is not None:
            self.team_a_player2_id = team_a_player2_id
        if team_a_points_game1 is not None:
            self.team_a_points_game1 = team_a_points_game1
        if team_a_points_game2 is not None:
            self.team_a_points_game2 = team_a_points_game2
        if team_a_points_game3 is not None:
            self.team_a_points_game3 = team_a_points_game3
        if team_a_points_game4 is not None:
            self.team_a_points_game4 = team_a_points_game4
        if team_a_points_game5 is not None:
            self.team_a_points_game5 = team_a_points_game5
        if team_b_player1 is not None:
            self.team_b_player1 = team_b_player1
        if team_b_player1_id is not None:
            self.team_b_player1_id = team_b_player1_id
        if team_b_player2 is not None:
            self.team_b_player2 = team_b_player2
        if team_b_player2_id is not None:
            self.team_b_player2_id = team_b_player2_id
        if team_b_points_game1 is not None:
            self.team_b_points_game1 = team_b_points_game1
        if team_b_points_game2 is not None:
            self.team_b_points_game2 = team_b_points_game2
        if team_b_points_game3 is not None:
            self.team_b_points_game3 = team_b_points_game3
        if team_b_points_game4 is not None:
            self.team_b_points_game4 = team_b_points_game4
        if team_b_points_game5 is not None:
            self.team_b_points_game5 = team_b_points_game5
        if tournament_name is not None:
            self.tournament_name = tournament_name
        if venue is not None:
            self.venue = venue
        if winning_team is not None:
            self.winning_team = winning_team

    @property
    def club_id(self):
        """Gets the club_id of this VerifiedMatchRequest.  # noqa: E501


        :return: The club_id of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id):
        """Sets the club_id of this VerifiedMatchRequest.


        :param club_id: The club_id of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._club_id = club_id

    @property
    def event_date(self):
        """Gets the event_date of this VerifiedMatchRequest.  # noqa: E501


        :return: The event_date of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this VerifiedMatchRequest.


        :param event_date: The event_date of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._event_date = event_date

    @property
    def event_name(self):
        """Gets the event_name of this VerifiedMatchRequest.  # noqa: E501


        :return: The event_name of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this VerifiedMatchRequest.


        :param event_name: The event_name of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._event_name = event_name

    @property
    def location(self):
        """Gets the location of this VerifiedMatchRequest.  # noqa: E501


        :return: The location of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this VerifiedMatchRequest.


        :param location: The location of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def team_a_player1(self):
        """Gets the team_a_player1 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_player1 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_a_player1

    @team_a_player1.setter
    def team_a_player1(self, team_a_player1):
        """Sets the team_a_player1 of this VerifiedMatchRequest.


        :param team_a_player1: The team_a_player1 of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._team_a_player1 = team_a_player1

    @property
    def team_a_player1_id(self):
        """Gets the team_a_player1_id of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_player1_id of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_a_player1_id

    @team_a_player1_id.setter
    def team_a_player1_id(self, team_a_player1_id):
        """Sets the team_a_player1_id of this VerifiedMatchRequest.


        :param team_a_player1_id: The team_a_player1_id of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._team_a_player1_id = team_a_player1_id

    @property
    def team_a_player2(self):
        """Gets the team_a_player2 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_player2 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_a_player2

    @team_a_player2.setter
    def team_a_player2(self, team_a_player2):
        """Sets the team_a_player2 of this VerifiedMatchRequest.


        :param team_a_player2: The team_a_player2 of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._team_a_player2 = team_a_player2

    @property
    def team_a_player2_id(self):
        """Gets the team_a_player2_id of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_player2_id of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_a_player2_id

    @team_a_player2_id.setter
    def team_a_player2_id(self, team_a_player2_id):
        """Sets the team_a_player2_id of this VerifiedMatchRequest.


        :param team_a_player2_id: The team_a_player2_id of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._team_a_player2_id = team_a_player2_id

    @property
    def team_a_points_game1(self):
        """Gets the team_a_points_game1 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_points_game1 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_a_points_game1

    @team_a_points_game1.setter
    def team_a_points_game1(self, team_a_points_game1):
        """Sets the team_a_points_game1 of this VerifiedMatchRequest.


        :param team_a_points_game1: The team_a_points_game1 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_a_points_game1 = team_a_points_game1

    @property
    def team_a_points_game2(self):
        """Gets the team_a_points_game2 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_points_game2 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_a_points_game2

    @team_a_points_game2.setter
    def team_a_points_game2(self, team_a_points_game2):
        """Sets the team_a_points_game2 of this VerifiedMatchRequest.


        :param team_a_points_game2: The team_a_points_game2 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_a_points_game2 = team_a_points_game2

    @property
    def team_a_points_game3(self):
        """Gets the team_a_points_game3 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_points_game3 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_a_points_game3

    @team_a_points_game3.setter
    def team_a_points_game3(self, team_a_points_game3):
        """Sets the team_a_points_game3 of this VerifiedMatchRequest.


        :param team_a_points_game3: The team_a_points_game3 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_a_points_game3 = team_a_points_game3

    @property
    def team_a_points_game4(self):
        """Gets the team_a_points_game4 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_points_game4 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_a_points_game4

    @team_a_points_game4.setter
    def team_a_points_game4(self, team_a_points_game4):
        """Sets the team_a_points_game4 of this VerifiedMatchRequest.


        :param team_a_points_game4: The team_a_points_game4 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_a_points_game4 = team_a_points_game4

    @property
    def team_a_points_game5(self):
        """Gets the team_a_points_game5 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_a_points_game5 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_a_points_game5

    @team_a_points_game5.setter
    def team_a_points_game5(self, team_a_points_game5):
        """Sets the team_a_points_game5 of this VerifiedMatchRequest.


        :param team_a_points_game5: The team_a_points_game5 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_a_points_game5 = team_a_points_game5

    @property
    def team_b_player1(self):
        """Gets the team_b_player1 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_player1 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_b_player1

    @team_b_player1.setter
    def team_b_player1(self, team_b_player1):
        """Sets the team_b_player1 of this VerifiedMatchRequest.


        :param team_b_player1: The team_b_player1 of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._team_b_player1 = team_b_player1

    @property
    def team_b_player1_id(self):
        """Gets the team_b_player1_id of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_player1_id of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_b_player1_id

    @team_b_player1_id.setter
    def team_b_player1_id(self, team_b_player1_id):
        """Sets the team_b_player1_id of this VerifiedMatchRequest.


        :param team_b_player1_id: The team_b_player1_id of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._team_b_player1_id = team_b_player1_id

    @property
    def team_b_player2(self):
        """Gets the team_b_player2 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_player2 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_b_player2

    @team_b_player2.setter
    def team_b_player2(self, team_b_player2):
        """Sets the team_b_player2 of this VerifiedMatchRequest.


        :param team_b_player2: The team_b_player2 of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._team_b_player2 = team_b_player2

    @property
    def team_b_player2_id(self):
        """Gets the team_b_player2_id of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_player2_id of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._team_b_player2_id

    @team_b_player2_id.setter
    def team_b_player2_id(self, team_b_player2_id):
        """Sets the team_b_player2_id of this VerifiedMatchRequest.


        :param team_b_player2_id: The team_b_player2_id of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._team_b_player2_id = team_b_player2_id

    @property
    def team_b_points_game1(self):
        """Gets the team_b_points_game1 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_points_game1 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_b_points_game1

    @team_b_points_game1.setter
    def team_b_points_game1(self, team_b_points_game1):
        """Sets the team_b_points_game1 of this VerifiedMatchRequest.


        :param team_b_points_game1: The team_b_points_game1 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_b_points_game1 = team_b_points_game1

    @property
    def team_b_points_game2(self):
        """Gets the team_b_points_game2 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_points_game2 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_b_points_game2

    @team_b_points_game2.setter
    def team_b_points_game2(self, team_b_points_game2):
        """Sets the team_b_points_game2 of this VerifiedMatchRequest.


        :param team_b_points_game2: The team_b_points_game2 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_b_points_game2 = team_b_points_game2

    @property
    def team_b_points_game3(self):
        """Gets the team_b_points_game3 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_points_game3 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_b_points_game3

    @team_b_points_game3.setter
    def team_b_points_game3(self, team_b_points_game3):
        """Sets the team_b_points_game3 of this VerifiedMatchRequest.


        :param team_b_points_game3: The team_b_points_game3 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_b_points_game3 = team_b_points_game3

    @property
    def team_b_points_game4(self):
        """Gets the team_b_points_game4 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_points_game4 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_b_points_game4

    @team_b_points_game4.setter
    def team_b_points_game4(self, team_b_points_game4):
        """Sets the team_b_points_game4 of this VerifiedMatchRequest.


        :param team_b_points_game4: The team_b_points_game4 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_b_points_game4 = team_b_points_game4

    @property
    def team_b_points_game5(self):
        """Gets the team_b_points_game5 of this VerifiedMatchRequest.  # noqa: E501


        :return: The team_b_points_game5 of this VerifiedMatchRequest.  # noqa: E501
        :rtype: int
        """
        return self._team_b_points_game5

    @team_b_points_game5.setter
    def team_b_points_game5(self, team_b_points_game5):
        """Sets the team_b_points_game5 of this VerifiedMatchRequest.


        :param team_b_points_game5: The team_b_points_game5 of this VerifiedMatchRequest.  # noqa: E501
        :type: int
        """

        self._team_b_points_game5 = team_b_points_game5

    @property
    def tournament_name(self):
        """Gets the tournament_name of this VerifiedMatchRequest.  # noqa: E501


        :return: The tournament_name of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._tournament_name

    @tournament_name.setter
    def tournament_name(self, tournament_name):
        """Sets the tournament_name of this VerifiedMatchRequest.


        :param tournament_name: The tournament_name of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._tournament_name = tournament_name

    @property
    def venue(self):
        """Gets the venue of this VerifiedMatchRequest.  # noqa: E501


        :return: The venue of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this VerifiedMatchRequest.


        :param venue: The venue of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._venue = venue

    @property
    def winning_team(self):
        """Gets the winning_team of this VerifiedMatchRequest.  # noqa: E501


        :return: The winning_team of this VerifiedMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._winning_team

    @winning_team.setter
    def winning_team(self, winning_team):
        """Sets the winning_team of this VerifiedMatchRequest.


        :param winning_team: The winning_team of this VerifiedMatchRequest.  # noqa: E501
        :type: str
        """

        self._winning_team = winning_team

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
        if issubclass(VerifiedMatchRequest, dict):
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
        if not isinstance(other, VerifiedMatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
