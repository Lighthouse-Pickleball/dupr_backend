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

class MatchRoundReq(object):
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
        'end_date': 'date',
        'matches': 'list[SeedMatchReq]',
        'serial': 'int',
        'start_date': 'date',
        'team_ids': 'list[int]'
    }

    attribute_map = {
        'end_date': 'endDate',
        'matches': 'matches',
        'serial': 'serial',
        'start_date': 'startDate',
        'team_ids': 'teamIds'
    }

    def __init__(self, end_date=None, matches=None, serial=None, start_date=None, team_ids=None):  # noqa: E501
        """MatchRoundReq - a model defined in Swagger"""  # noqa: E501
        self._end_date = None
        self._matches = None
        self._serial = None
        self._start_date = None
        self._team_ids = None
        self.discriminator = None
        if end_date is not None:
            self.end_date = end_date
        self.matches = matches
        self.serial = serial
        self.start_date = start_date
        if team_ids is not None:
            self.team_ids = team_ids

    @property
    def end_date(self):
        """Gets the end_date of this MatchRoundReq.  # noqa: E501


        :return: The end_date of this MatchRoundReq.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this MatchRoundReq.


        :param end_date: The end_date of this MatchRoundReq.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def matches(self):
        """Gets the matches of this MatchRoundReq.  # noqa: E501


        :return: The matches of this MatchRoundReq.  # noqa: E501
        :rtype: list[SeedMatchReq]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this MatchRoundReq.


        :param matches: The matches of this MatchRoundReq.  # noqa: E501
        :type: list[SeedMatchReq]
        """
        if matches is None:
            raise ValueError("Invalid value for `matches`, must not be `None`")  # noqa: E501

        self._matches = matches

    @property
    def serial(self):
        """Gets the serial of this MatchRoundReq.  # noqa: E501


        :return: The serial of this MatchRoundReq.  # noqa: E501
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this MatchRoundReq.


        :param serial: The serial of this MatchRoundReq.  # noqa: E501
        :type: int
        """
        if serial is None:
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def start_date(self):
        """Gets the start_date of this MatchRoundReq.  # noqa: E501


        :return: The start_date of this MatchRoundReq.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this MatchRoundReq.


        :param start_date: The start_date of this MatchRoundReq.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def team_ids(self):
        """Gets the team_ids of this MatchRoundReq.  # noqa: E501


        :return: The team_ids of this MatchRoundReq.  # noqa: E501
        :rtype: list[int]
        """
        return self._team_ids

    @team_ids.setter
    def team_ids(self, team_ids):
        """Sets the team_ids of this MatchRoundReq.


        :param team_ids: The team_ids of this MatchRoundReq.  # noqa: E501
        :type: list[int]
        """

        self._team_ids = team_ids

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
        if issubclass(MatchRoundReq, dict):
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
        if not isinstance(other, MatchRoundReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
