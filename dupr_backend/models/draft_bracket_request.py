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

class DraftBracketRequest(object):
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
        'age_bracket': 'list[int]',
        'bracket_id': 'int',
        'courts': 'int',
        'custom_code': 'str',
        'description': 'LeagueContentRequest',
        'duration': 'list[ErrorModelNamenamespacejavaTimeNameLocalDate]',
        'duration_date_time': 'list[str]',
        'elimination': 'str',
        'format': 'str',
        'league_id': 'int',
        'match_bonus_points': 'float',
        'max_team': 'int',
        'member_fee': 'float',
        'name': 'str',
        'non_member_fee': 'float',
        'player_group': 'str',
        'rating_bracket': 'list[float]',
        'registration_date': 'list[ErrorModelNamenamespacejavaTimeNameLocalDate]',
        'registration_date_time': 'list[str]',
        'score_format': 'int',
        'time_zone': 'str',
        'wait_list': 'int',
        'zone_name': 'str'
    }

    attribute_map = {
        'age_bracket': 'ageBracket',
        'bracket_id': 'bracketId',
        'courts': 'courts',
        'custom_code': 'customCode',
        'description': 'description',
        'duration': 'duration',
        'duration_date_time': 'durationDateTime',
        'elimination': 'elimination',
        'format': 'format',
        'league_id': 'leagueId',
        'match_bonus_points': 'matchBonusPoints',
        'max_team': 'maxTeam',
        'member_fee': 'memberFee',
        'name': 'name',
        'non_member_fee': 'nonMemberFee',
        'player_group': 'playerGroup',
        'rating_bracket': 'ratingBracket',
        'registration_date': 'registrationDate',
        'registration_date_time': 'registrationDateTime',
        'score_format': 'scoreFormat',
        'time_zone': 'timeZone',
        'wait_list': 'waitList',
        'zone_name': 'zoneName'
    }

    def __init__(self, age_bracket=None, bracket_id=None, courts=None, custom_code=None, description=None, duration=None, duration_date_time=None, elimination=None, format=None, league_id=None, match_bonus_points=None, max_team=None, member_fee=None, name=None, non_member_fee=None, player_group=None, rating_bracket=None, registration_date=None, registration_date_time=None, score_format=None, time_zone=None, wait_list=None, zone_name=None):  # noqa: E501
        """DraftBracketRequest - a model defined in Swagger"""  # noqa: E501
        self._age_bracket = None
        self._bracket_id = None
        self._courts = None
        self._custom_code = None
        self._description = None
        self._duration = None
        self._duration_date_time = None
        self._elimination = None
        self._format = None
        self._league_id = None
        self._match_bonus_points = None
        self._max_team = None
        self._member_fee = None
        self._name = None
        self._non_member_fee = None
        self._player_group = None
        self._rating_bracket = None
        self._registration_date = None
        self._registration_date_time = None
        self._score_format = None
        self._time_zone = None
        self._wait_list = None
        self._zone_name = None
        self.discriminator = None
        if age_bracket is not None:
            self.age_bracket = age_bracket
        self.bracket_id = bracket_id
        if courts is not None:
            self.courts = courts
        if custom_code is not None:
            self.custom_code = custom_code
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if duration_date_time is not None:
            self.duration_date_time = duration_date_time
        if elimination is not None:
            self.elimination = elimination
        if format is not None:
            self.format = format
        if league_id is not None:
            self.league_id = league_id
        if match_bonus_points is not None:
            self.match_bonus_points = match_bonus_points
        if max_team is not None:
            self.max_team = max_team
        if member_fee is not None:
            self.member_fee = member_fee
        if name is not None:
            self.name = name
        if non_member_fee is not None:
            self.non_member_fee = non_member_fee
        if player_group is not None:
            self.player_group = player_group
        if rating_bracket is not None:
            self.rating_bracket = rating_bracket
        if registration_date is not None:
            self.registration_date = registration_date
        if registration_date_time is not None:
            self.registration_date_time = registration_date_time
        if score_format is not None:
            self.score_format = score_format
        if time_zone is not None:
            self.time_zone = time_zone
        if wait_list is not None:
            self.wait_list = wait_list
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def age_bracket(self):
        """Gets the age_bracket of this DraftBracketRequest.  # noqa: E501


        :return: The age_bracket of this DraftBracketRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._age_bracket

    @age_bracket.setter
    def age_bracket(self, age_bracket):
        """Sets the age_bracket of this DraftBracketRequest.


        :param age_bracket: The age_bracket of this DraftBracketRequest.  # noqa: E501
        :type: list[int]
        """

        self._age_bracket = age_bracket

    @property
    def bracket_id(self):
        """Gets the bracket_id of this DraftBracketRequest.  # noqa: E501


        :return: The bracket_id of this DraftBracketRequest.  # noqa: E501
        :rtype: int
        """
        return self._bracket_id

    @bracket_id.setter
    def bracket_id(self, bracket_id):
        """Sets the bracket_id of this DraftBracketRequest.


        :param bracket_id: The bracket_id of this DraftBracketRequest.  # noqa: E501
        :type: int
        """
        if bracket_id is None:
            raise ValueError("Invalid value for `bracket_id`, must not be `None`")  # noqa: E501

        self._bracket_id = bracket_id

    @property
    def courts(self):
        """Gets the courts of this DraftBracketRequest.  # noqa: E501


        :return: The courts of this DraftBracketRequest.  # noqa: E501
        :rtype: int
        """
        return self._courts

    @courts.setter
    def courts(self, courts):
        """Sets the courts of this DraftBracketRequest.


        :param courts: The courts of this DraftBracketRequest.  # noqa: E501
        :type: int
        """

        self._courts = courts

    @property
    def custom_code(self):
        """Gets the custom_code of this DraftBracketRequest.  # noqa: E501


        :return: The custom_code of this DraftBracketRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_code

    @custom_code.setter
    def custom_code(self, custom_code):
        """Sets the custom_code of this DraftBracketRequest.


        :param custom_code: The custom_code of this DraftBracketRequest.  # noqa: E501
        :type: str
        """

        self._custom_code = custom_code

    @property
    def description(self):
        """Gets the description of this DraftBracketRequest.  # noqa: E501


        :return: The description of this DraftBracketRequest.  # noqa: E501
        :rtype: LeagueContentRequest
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DraftBracketRequest.


        :param description: The description of this DraftBracketRequest.  # noqa: E501
        :type: LeagueContentRequest
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this DraftBracketRequest.  # noqa: E501


        :return: The duration of this DraftBracketRequest.  # noqa: E501
        :rtype: list[ErrorModelNamenamespacejavaTimeNameLocalDate]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DraftBracketRequest.


        :param duration: The duration of this DraftBracketRequest.  # noqa: E501
        :type: list[ErrorModelNamenamespacejavaTimeNameLocalDate]
        """

        self._duration = duration

    @property
    def duration_date_time(self):
        """Gets the duration_date_time of this DraftBracketRequest.  # noqa: E501


        :return: The duration_date_time of this DraftBracketRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._duration_date_time

    @duration_date_time.setter
    def duration_date_time(self, duration_date_time):
        """Sets the duration_date_time of this DraftBracketRequest.


        :param duration_date_time: The duration_date_time of this DraftBracketRequest.  # noqa: E501
        :type: list[str]
        """

        self._duration_date_time = duration_date_time

    @property
    def elimination(self):
        """Gets the elimination of this DraftBracketRequest.  # noqa: E501


        :return: The elimination of this DraftBracketRequest.  # noqa: E501
        :rtype: str
        """
        return self._elimination

    @elimination.setter
    def elimination(self, elimination):
        """Sets the elimination of this DraftBracketRequest.


        :param elimination: The elimination of this DraftBracketRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMPASS", "DOUBLE", "DOUBLE_PREVENTED", "FLEX", "ROUND_ROBIN", "SINGLE"]  # noqa: E501
        if elimination not in allowed_values:
            raise ValueError(
                "Invalid value for `elimination` ({0}), must be one of {1}"  # noqa: E501
                .format(elimination, allowed_values)
            )

        self._elimination = elimination

    @property
    def format(self):
        """Gets the format of this DraftBracketRequest.  # noqa: E501


        :return: The format of this DraftBracketRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this DraftBracketRequest.


        :param format: The format of this DraftBracketRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOUBLES", "SINGLES"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def league_id(self):
        """Gets the league_id of this DraftBracketRequest.  # noqa: E501


        :return: The league_id of this DraftBracketRequest.  # noqa: E501
        :rtype: int
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this DraftBracketRequest.


        :param league_id: The league_id of this DraftBracketRequest.  # noqa: E501
        :type: int
        """

        self._league_id = league_id

    @property
    def match_bonus_points(self):
        """Gets the match_bonus_points of this DraftBracketRequest.  # noqa: E501


        :return: The match_bonus_points of this DraftBracketRequest.  # noqa: E501
        :rtype: float
        """
        return self._match_bonus_points

    @match_bonus_points.setter
    def match_bonus_points(self, match_bonus_points):
        """Sets the match_bonus_points of this DraftBracketRequest.


        :param match_bonus_points: The match_bonus_points of this DraftBracketRequest.  # noqa: E501
        :type: float
        """

        self._match_bonus_points = match_bonus_points

    @property
    def max_team(self):
        """Gets the max_team of this DraftBracketRequest.  # noqa: E501


        :return: The max_team of this DraftBracketRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_team

    @max_team.setter
    def max_team(self, max_team):
        """Sets the max_team of this DraftBracketRequest.


        :param max_team: The max_team of this DraftBracketRequest.  # noqa: E501
        :type: int
        """

        self._max_team = max_team

    @property
    def member_fee(self):
        """Gets the member_fee of this DraftBracketRequest.  # noqa: E501


        :return: The member_fee of this DraftBracketRequest.  # noqa: E501
        :rtype: float
        """
        return self._member_fee

    @member_fee.setter
    def member_fee(self, member_fee):
        """Sets the member_fee of this DraftBracketRequest.


        :param member_fee: The member_fee of this DraftBracketRequest.  # noqa: E501
        :type: float
        """

        self._member_fee = member_fee

    @property
    def name(self):
        """Gets the name of this DraftBracketRequest.  # noqa: E501


        :return: The name of this DraftBracketRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DraftBracketRequest.


        :param name: The name of this DraftBracketRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def non_member_fee(self):
        """Gets the non_member_fee of this DraftBracketRequest.  # noqa: E501


        :return: The non_member_fee of this DraftBracketRequest.  # noqa: E501
        :rtype: float
        """
        return self._non_member_fee

    @non_member_fee.setter
    def non_member_fee(self, non_member_fee):
        """Sets the non_member_fee of this DraftBracketRequest.


        :param non_member_fee: The non_member_fee of this DraftBracketRequest.  # noqa: E501
        :type: float
        """

        self._non_member_fee = non_member_fee

    @property
    def player_group(self):
        """Gets the player_group of this DraftBracketRequest.  # noqa: E501


        :return: The player_group of this DraftBracketRequest.  # noqa: E501
        :rtype: str
        """
        return self._player_group

    @player_group.setter
    def player_group(self, player_group):
        """Sets the player_group of this DraftBracketRequest.


        :param player_group: The player_group of this DraftBracketRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["COED", "MEN", "MIXED", "OPEN", "WOMEN"]  # noqa: E501
        if player_group not in allowed_values:
            raise ValueError(
                "Invalid value for `player_group` ({0}), must be one of {1}"  # noqa: E501
                .format(player_group, allowed_values)
            )

        self._player_group = player_group

    @property
    def rating_bracket(self):
        """Gets the rating_bracket of this DraftBracketRequest.  # noqa: E501


        :return: The rating_bracket of this DraftBracketRequest.  # noqa: E501
        :rtype: list[float]
        """
        return self._rating_bracket

    @rating_bracket.setter
    def rating_bracket(self, rating_bracket):
        """Sets the rating_bracket of this DraftBracketRequest.


        :param rating_bracket: The rating_bracket of this DraftBracketRequest.  # noqa: E501
        :type: list[float]
        """

        self._rating_bracket = rating_bracket

    @property
    def registration_date(self):
        """Gets the registration_date of this DraftBracketRequest.  # noqa: E501


        :return: The registration_date of this DraftBracketRequest.  # noqa: E501
        :rtype: list[ErrorModelNamenamespacejavaTimeNameLocalDate]
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this DraftBracketRequest.


        :param registration_date: The registration_date of this DraftBracketRequest.  # noqa: E501
        :type: list[ErrorModelNamenamespacejavaTimeNameLocalDate]
        """

        self._registration_date = registration_date

    @property
    def registration_date_time(self):
        """Gets the registration_date_time of this DraftBracketRequest.  # noqa: E501


        :return: The registration_date_time of this DraftBracketRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._registration_date_time

    @registration_date_time.setter
    def registration_date_time(self, registration_date_time):
        """Sets the registration_date_time of this DraftBracketRequest.


        :param registration_date_time: The registration_date_time of this DraftBracketRequest.  # noqa: E501
        :type: list[str]
        """

        self._registration_date_time = registration_date_time

    @property
    def score_format(self):
        """Gets the score_format of this DraftBracketRequest.  # noqa: E501


        :return: The score_format of this DraftBracketRequest.  # noqa: E501
        :rtype: int
        """
        return self._score_format

    @score_format.setter
    def score_format(self, score_format):
        """Sets the score_format of this DraftBracketRequest.


        :param score_format: The score_format of this DraftBracketRequest.  # noqa: E501
        :type: int
        """

        self._score_format = score_format

    @property
    def time_zone(self):
        """Gets the time_zone of this DraftBracketRequest.  # noqa: E501


        :return: The time_zone of this DraftBracketRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this DraftBracketRequest.


        :param time_zone: The time_zone of this DraftBracketRequest.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def wait_list(self):
        """Gets the wait_list of this DraftBracketRequest.  # noqa: E501


        :return: The wait_list of this DraftBracketRequest.  # noqa: E501
        :rtype: int
        """
        return self._wait_list

    @wait_list.setter
    def wait_list(self, wait_list):
        """Sets the wait_list of this DraftBracketRequest.


        :param wait_list: The wait_list of this DraftBracketRequest.  # noqa: E501
        :type: int
        """

        self._wait_list = wait_list

    @property
    def zone_name(self):
        """Gets the zone_name of this DraftBracketRequest.  # noqa: E501


        :return: The zone_name of this DraftBracketRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this DraftBracketRequest.


        :param zone_name: The zone_name of this DraftBracketRequest.  # noqa: E501
        :type: str
        """

        self._zone_name = zone_name

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
        if issubclass(DraftBracketRequest, dict):
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
        if not isinstance(other, DraftBracketRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
