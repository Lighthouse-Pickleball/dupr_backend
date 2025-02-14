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

class MatchRatings(object):
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
        'average_opponent_dupr': 'str',
        'average_partner_dupr': 'str',
        'average_points_won_percent': 'str',
        'half_life': 'str',
        'losses': 'int',
        'wins': 'int'
    }

    attribute_map = {
        'average_opponent_dupr': 'averageOpponentDupr',
        'average_partner_dupr': 'averagePartnerDupr',
        'average_points_won_percent': 'averagePointsWonPercent',
        'half_life': 'halfLife',
        'losses': 'losses',
        'wins': 'wins'
    }

    def __init__(self, average_opponent_dupr=None, average_partner_dupr=None, average_points_won_percent=None, half_life=None, losses=None, wins=None):  # noqa: E501
        """MatchRatings - a model defined in Swagger"""  # noqa: E501
        self._average_opponent_dupr = None
        self._average_partner_dupr = None
        self._average_points_won_percent = None
        self._half_life = None
        self._losses = None
        self._wins = None
        self.discriminator = None
        if average_opponent_dupr is not None:
            self.average_opponent_dupr = average_opponent_dupr
        if average_partner_dupr is not None:
            self.average_partner_dupr = average_partner_dupr
        if average_points_won_percent is not None:
            self.average_points_won_percent = average_points_won_percent
        if half_life is not None:
            self.half_life = half_life
        if losses is not None:
            self.losses = losses
        if wins is not None:
            self.wins = wins

    @property
    def average_opponent_dupr(self):
        """Gets the average_opponent_dupr of this MatchRatings.  # noqa: E501


        :return: The average_opponent_dupr of this MatchRatings.  # noqa: E501
        :rtype: str
        """
        return self._average_opponent_dupr

    @average_opponent_dupr.setter
    def average_opponent_dupr(self, average_opponent_dupr):
        """Sets the average_opponent_dupr of this MatchRatings.


        :param average_opponent_dupr: The average_opponent_dupr of this MatchRatings.  # noqa: E501
        :type: str
        """

        self._average_opponent_dupr = average_opponent_dupr

    @property
    def average_partner_dupr(self):
        """Gets the average_partner_dupr of this MatchRatings.  # noqa: E501


        :return: The average_partner_dupr of this MatchRatings.  # noqa: E501
        :rtype: str
        """
        return self._average_partner_dupr

    @average_partner_dupr.setter
    def average_partner_dupr(self, average_partner_dupr):
        """Sets the average_partner_dupr of this MatchRatings.


        :param average_partner_dupr: The average_partner_dupr of this MatchRatings.  # noqa: E501
        :type: str
        """

        self._average_partner_dupr = average_partner_dupr

    @property
    def average_points_won_percent(self):
        """Gets the average_points_won_percent of this MatchRatings.  # noqa: E501


        :return: The average_points_won_percent of this MatchRatings.  # noqa: E501
        :rtype: str
        """
        return self._average_points_won_percent

    @average_points_won_percent.setter
    def average_points_won_percent(self, average_points_won_percent):
        """Sets the average_points_won_percent of this MatchRatings.


        :param average_points_won_percent: The average_points_won_percent of this MatchRatings.  # noqa: E501
        :type: str
        """

        self._average_points_won_percent = average_points_won_percent

    @property
    def half_life(self):
        """Gets the half_life of this MatchRatings.  # noqa: E501


        :return: The half_life of this MatchRatings.  # noqa: E501
        :rtype: str
        """
        return self._half_life

    @half_life.setter
    def half_life(self, half_life):
        """Sets the half_life of this MatchRatings.


        :param half_life: The half_life of this MatchRatings.  # noqa: E501
        :type: str
        """

        self._half_life = half_life

    @property
    def losses(self):
        """Gets the losses of this MatchRatings.  # noqa: E501


        :return: The losses of this MatchRatings.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this MatchRatings.


        :param losses: The losses of this MatchRatings.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def wins(self):
        """Gets the wins of this MatchRatings.  # noqa: E501


        :return: The wins of this MatchRatings.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this MatchRatings.


        :param wins: The wins of this MatchRatings.  # noqa: E501
        :type: int
        """

        self._wins = wins

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
        if issubclass(MatchRatings, dict):
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
        if not isinstance(other, MatchRatings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
