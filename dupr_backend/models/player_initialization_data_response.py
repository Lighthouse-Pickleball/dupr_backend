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

class PlayerInitializationDataResponse(object):
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
        'days_left_for_initialization': 'int',
        'event_format': 'str',
        'initialization_status': 'str',
        'player_id': 'str',
        'player_name': 'str',
        'qualification_score': 'float'
    }

    attribute_map = {
        'days_left_for_initialization': 'daysLeftForInitialization',
        'event_format': 'eventFormat',
        'initialization_status': 'initializationStatus',
        'player_id': 'playerId',
        'player_name': 'playerName',
        'qualification_score': 'qualificationScore'
    }

    def __init__(self, days_left_for_initialization=None, event_format=None, initialization_status=None, player_id=None, player_name=None, qualification_score=None):  # noqa: E501
        """PlayerInitializationDataResponse - a model defined in Swagger"""  # noqa: E501
        self._days_left_for_initialization = None
        self._event_format = None
        self._initialization_status = None
        self._player_id = None
        self._player_name = None
        self._qualification_score = None
        self.discriminator = None
        if days_left_for_initialization is not None:
            self.days_left_for_initialization = days_left_for_initialization
        self.event_format = event_format
        self.initialization_status = initialization_status
        self.player_id = player_id
        self.player_name = player_name
        self.qualification_score = qualification_score

    @property
    def days_left_for_initialization(self):
        """Gets the days_left_for_initialization of this PlayerInitializationDataResponse.  # noqa: E501


        :return: The days_left_for_initialization of this PlayerInitializationDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._days_left_for_initialization

    @days_left_for_initialization.setter
    def days_left_for_initialization(self, days_left_for_initialization):
        """Sets the days_left_for_initialization of this PlayerInitializationDataResponse.


        :param days_left_for_initialization: The days_left_for_initialization of this PlayerInitializationDataResponse.  # noqa: E501
        :type: int
        """

        self._days_left_for_initialization = days_left_for_initialization

    @property
    def event_format(self):
        """Gets the event_format of this PlayerInitializationDataResponse.  # noqa: E501


        :return: The event_format of this PlayerInitializationDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._event_format

    @event_format.setter
    def event_format(self, event_format):
        """Sets the event_format of this PlayerInitializationDataResponse.


        :param event_format: The event_format of this PlayerInitializationDataResponse.  # noqa: E501
        :type: str
        """
        if event_format is None:
            raise ValueError("Invalid value for `event_format`, must not be `None`")  # noqa: E501

        self._event_format = event_format

    @property
    def initialization_status(self):
        """Gets the initialization_status of this PlayerInitializationDataResponse.  # noqa: E501


        :return: The initialization_status of this PlayerInitializationDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._initialization_status

    @initialization_status.setter
    def initialization_status(self, initialization_status):
        """Sets the initialization_status of this PlayerInitializationDataResponse.


        :param initialization_status: The initialization_status of this PlayerInitializationDataResponse.  # noqa: E501
        :type: str
        """
        if initialization_status is None:
            raise ValueError("Invalid value for `initialization_status`, must not be `None`")  # noqa: E501

        self._initialization_status = initialization_status

    @property
    def player_id(self):
        """Gets the player_id of this PlayerInitializationDataResponse.  # noqa: E501


        :return: The player_id of this PlayerInitializationDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        """Sets the player_id of this PlayerInitializationDataResponse.


        :param player_id: The player_id of this PlayerInitializationDataResponse.  # noqa: E501
        :type: str
        """
        if player_id is None:
            raise ValueError("Invalid value for `player_id`, must not be `None`")  # noqa: E501

        self._player_id = player_id

    @property
    def player_name(self):
        """Gets the player_name of this PlayerInitializationDataResponse.  # noqa: E501


        :return: The player_name of this PlayerInitializationDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._player_name

    @player_name.setter
    def player_name(self, player_name):
        """Sets the player_name of this PlayerInitializationDataResponse.


        :param player_name: The player_name of this PlayerInitializationDataResponse.  # noqa: E501
        :type: str
        """
        if player_name is None:
            raise ValueError("Invalid value for `player_name`, must not be `None`")  # noqa: E501

        self._player_name = player_name

    @property
    def qualification_score(self):
        """Gets the qualification_score of this PlayerInitializationDataResponse.  # noqa: E501


        :return: The qualification_score of this PlayerInitializationDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._qualification_score

    @qualification_score.setter
    def qualification_score(self, qualification_score):
        """Sets the qualification_score of this PlayerInitializationDataResponse.


        :param qualification_score: The qualification_score of this PlayerInitializationDataResponse.  # noqa: E501
        :type: float
        """
        if qualification_score is None:
            raise ValueError("Invalid value for `qualification_score`, must not be `None`")  # noqa: E501

        self._qualification_score = qualification_score

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
        if issubclass(PlayerInitializationDataResponse, dict):
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
        if not isinstance(other, PlayerInitializationDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
