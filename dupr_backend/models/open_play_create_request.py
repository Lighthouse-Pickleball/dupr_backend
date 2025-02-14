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

class OpenPlayCreateRequest(object):
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
        'address_id': 'int',
        'description': 'str',
        'event_date': 'date',
        'invited_players': 'list[str]',
        'max_players': 'int',
        'name': 'str',
        'rating': 'RatingRangeReq',
        'time': 'TimeRangeReq'
    }

    attribute_map = {
        'address_id': 'addressId',
        'description': 'description',
        'event_date': 'eventDate',
        'invited_players': 'invitedPlayers',
        'max_players': 'maxPlayers',
        'name': 'name',
        'rating': 'rating',
        'time': 'time'
    }

    def __init__(self, address_id=None, description=None, event_date=None, invited_players=None, max_players=None, name=None, rating=None, time=None):  # noqa: E501
        """OpenPlayCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._address_id = None
        self._description = None
        self._event_date = None
        self._invited_players = None
        self._max_players = None
        self._name = None
        self._rating = None
        self._time = None
        self.discriminator = None
        self.address_id = address_id
        if description is not None:
            self.description = description
        self.event_date = event_date
        if invited_players is not None:
            self.invited_players = invited_players
        self.max_players = max_players
        self.name = name
        self.rating = rating
        self.time = time

    @property
    def address_id(self):
        """Gets the address_id of this OpenPlayCreateRequest.  # noqa: E501


        :return: The address_id of this OpenPlayCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this OpenPlayCreateRequest.


        :param address_id: The address_id of this OpenPlayCreateRequest.  # noqa: E501
        :type: int
        """
        if address_id is None:
            raise ValueError("Invalid value for `address_id`, must not be `None`")  # noqa: E501

        self._address_id = address_id

    @property
    def description(self):
        """Gets the description of this OpenPlayCreateRequest.  # noqa: E501


        :return: The description of this OpenPlayCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenPlayCreateRequest.


        :param description: The description of this OpenPlayCreateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def event_date(self):
        """Gets the event_date of this OpenPlayCreateRequest.  # noqa: E501


        :return: The event_date of this OpenPlayCreateRequest.  # noqa: E501
        :rtype: date
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this OpenPlayCreateRequest.


        :param event_date: The event_date of this OpenPlayCreateRequest.  # noqa: E501
        :type: date
        """
        if event_date is None:
            raise ValueError("Invalid value for `event_date`, must not be `None`")  # noqa: E501

        self._event_date = event_date

    @property
    def invited_players(self):
        """Gets the invited_players of this OpenPlayCreateRequest.  # noqa: E501


        :return: The invited_players of this OpenPlayCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._invited_players

    @invited_players.setter
    def invited_players(self, invited_players):
        """Sets the invited_players of this OpenPlayCreateRequest.


        :param invited_players: The invited_players of this OpenPlayCreateRequest.  # noqa: E501
        :type: list[str]
        """

        self._invited_players = invited_players

    @property
    def max_players(self):
        """Gets the max_players of this OpenPlayCreateRequest.  # noqa: E501


        :return: The max_players of this OpenPlayCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_players

    @max_players.setter
    def max_players(self, max_players):
        """Sets the max_players of this OpenPlayCreateRequest.


        :param max_players: The max_players of this OpenPlayCreateRequest.  # noqa: E501
        :type: int
        """
        if max_players is None:
            raise ValueError("Invalid value for `max_players`, must not be `None`")  # noqa: E501

        self._max_players = max_players

    @property
    def name(self):
        """Gets the name of this OpenPlayCreateRequest.  # noqa: E501


        :return: The name of this OpenPlayCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenPlayCreateRequest.


        :param name: The name of this OpenPlayCreateRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def rating(self):
        """Gets the rating of this OpenPlayCreateRequest.  # noqa: E501


        :return: The rating of this OpenPlayCreateRequest.  # noqa: E501
        :rtype: RatingRangeReq
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this OpenPlayCreateRequest.


        :param rating: The rating of this OpenPlayCreateRequest.  # noqa: E501
        :type: RatingRangeReq
        """
        if rating is None:
            raise ValueError("Invalid value for `rating`, must not be `None`")  # noqa: E501

        self._rating = rating

    @property
    def time(self):
        """Gets the time of this OpenPlayCreateRequest.  # noqa: E501


        :return: The time of this OpenPlayCreateRequest.  # noqa: E501
        :rtype: TimeRangeReq
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OpenPlayCreateRequest.


        :param time: The time of this OpenPlayCreateRequest.  # noqa: E501
        :type: TimeRangeReq
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if issubclass(OpenPlayCreateRequest, dict):
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
        if not isinstance(other, OpenPlayCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
