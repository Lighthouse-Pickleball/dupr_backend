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

class PlayerStatisticsUpdateRequest(object):
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
        'doubles': 'MatchRatings',
        'obfuscated_player_id': 'int',
        'singles': 'MatchRatings'
    }

    attribute_map = {
        'doubles': 'doubles',
        'obfuscated_player_id': 'obfuscatedPlayerId',
        'singles': 'singles'
    }

    def __init__(self, doubles=None, obfuscated_player_id=None, singles=None):  # noqa: E501
        """PlayerStatisticsUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._doubles = None
        self._obfuscated_player_id = None
        self._singles = None
        self.discriminator = None
        if doubles is not None:
            self.doubles = doubles
        self.obfuscated_player_id = obfuscated_player_id
        if singles is not None:
            self.singles = singles

    @property
    def doubles(self):
        """Gets the doubles of this PlayerStatisticsUpdateRequest.  # noqa: E501


        :return: The doubles of this PlayerStatisticsUpdateRequest.  # noqa: E501
        :rtype: MatchRatings
        """
        return self._doubles

    @doubles.setter
    def doubles(self, doubles):
        """Sets the doubles of this PlayerStatisticsUpdateRequest.


        :param doubles: The doubles of this PlayerStatisticsUpdateRequest.  # noqa: E501
        :type: MatchRatings
        """

        self._doubles = doubles

    @property
    def obfuscated_player_id(self):
        """Gets the obfuscated_player_id of this PlayerStatisticsUpdateRequest.  # noqa: E501


        :return: The obfuscated_player_id of this PlayerStatisticsUpdateRequest.  # noqa: E501
        :rtype: int
        """
        return self._obfuscated_player_id

    @obfuscated_player_id.setter
    def obfuscated_player_id(self, obfuscated_player_id):
        """Sets the obfuscated_player_id of this PlayerStatisticsUpdateRequest.


        :param obfuscated_player_id: The obfuscated_player_id of this PlayerStatisticsUpdateRequest.  # noqa: E501
        :type: int
        """
        if obfuscated_player_id is None:
            raise ValueError("Invalid value for `obfuscated_player_id`, must not be `None`")  # noqa: E501

        self._obfuscated_player_id = obfuscated_player_id

    @property
    def singles(self):
        """Gets the singles of this PlayerStatisticsUpdateRequest.  # noqa: E501


        :return: The singles of this PlayerStatisticsUpdateRequest.  # noqa: E501
        :rtype: MatchRatings
        """
        return self._singles

    @singles.setter
    def singles(self, singles):
        """Sets the singles of this PlayerStatisticsUpdateRequest.


        :param singles: The singles of this PlayerStatisticsUpdateRequest.  # noqa: E501
        :type: MatchRatings
        """

        self._singles = singles

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
        if issubclass(PlayerStatisticsUpdateRequest, dict):
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
        if not isinstance(other, PlayerStatisticsUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
