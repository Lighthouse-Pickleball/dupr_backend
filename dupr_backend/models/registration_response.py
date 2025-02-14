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

class RegistrationResponse(object):
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
        'event_refunded_amount': 'float',
        'is_participant1': 'bool',
        'is_wait_listed': 'bool',
        'player1': 'Participant',
        'player2': 'Participant',
        'registration_id': 'int'
    }

    attribute_map = {
        'event_refunded_amount': 'eventRefundedAmount',
        'is_participant1': 'isParticipant1',
        'is_wait_listed': 'isWaitListed',
        'player1': 'player1',
        'player2': 'player2',
        'registration_id': 'registrationId'
    }

    def __init__(self, event_refunded_amount=None, is_participant1=None, is_wait_listed=None, player1=None, player2=None, registration_id=None):  # noqa: E501
        """RegistrationResponse - a model defined in Swagger"""  # noqa: E501
        self._event_refunded_amount = None
        self._is_participant1 = None
        self._is_wait_listed = None
        self._player1 = None
        self._player2 = None
        self._registration_id = None
        self.discriminator = None
        self.event_refunded_amount = event_refunded_amount
        self.is_participant1 = is_participant1
        self.is_wait_listed = is_wait_listed
        if player1 is not None:
            self.player1 = player1
        if player2 is not None:
            self.player2 = player2
        self.registration_id = registration_id

    @property
    def event_refunded_amount(self):
        """Gets the event_refunded_amount of this RegistrationResponse.  # noqa: E501


        :return: The event_refunded_amount of this RegistrationResponse.  # noqa: E501
        :rtype: float
        """
        return self._event_refunded_amount

    @event_refunded_amount.setter
    def event_refunded_amount(self, event_refunded_amount):
        """Sets the event_refunded_amount of this RegistrationResponse.


        :param event_refunded_amount: The event_refunded_amount of this RegistrationResponse.  # noqa: E501
        :type: float
        """
        if event_refunded_amount is None:
            raise ValueError("Invalid value for `event_refunded_amount`, must not be `None`")  # noqa: E501

        self._event_refunded_amount = event_refunded_amount

    @property
    def is_participant1(self):
        """Gets the is_participant1 of this RegistrationResponse.  # noqa: E501


        :return: The is_participant1 of this RegistrationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_participant1

    @is_participant1.setter
    def is_participant1(self, is_participant1):
        """Sets the is_participant1 of this RegistrationResponse.


        :param is_participant1: The is_participant1 of this RegistrationResponse.  # noqa: E501
        :type: bool
        """
        if is_participant1 is None:
            raise ValueError("Invalid value for `is_participant1`, must not be `None`")  # noqa: E501

        self._is_participant1 = is_participant1

    @property
    def is_wait_listed(self):
        """Gets the is_wait_listed of this RegistrationResponse.  # noqa: E501


        :return: The is_wait_listed of this RegistrationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_wait_listed

    @is_wait_listed.setter
    def is_wait_listed(self, is_wait_listed):
        """Sets the is_wait_listed of this RegistrationResponse.


        :param is_wait_listed: The is_wait_listed of this RegistrationResponse.  # noqa: E501
        :type: bool
        """
        if is_wait_listed is None:
            raise ValueError("Invalid value for `is_wait_listed`, must not be `None`")  # noqa: E501

        self._is_wait_listed = is_wait_listed

    @property
    def player1(self):
        """Gets the player1 of this RegistrationResponse.  # noqa: E501


        :return: The player1 of this RegistrationResponse.  # noqa: E501
        :rtype: Participant
        """
        return self._player1

    @player1.setter
    def player1(self, player1):
        """Sets the player1 of this RegistrationResponse.


        :param player1: The player1 of this RegistrationResponse.  # noqa: E501
        :type: Participant
        """

        self._player1 = player1

    @property
    def player2(self):
        """Gets the player2 of this RegistrationResponse.  # noqa: E501


        :return: The player2 of this RegistrationResponse.  # noqa: E501
        :rtype: Participant
        """
        return self._player2

    @player2.setter
    def player2(self, player2):
        """Sets the player2 of this RegistrationResponse.


        :param player2: The player2 of this RegistrationResponse.  # noqa: E501
        :type: Participant
        """

        self._player2 = player2

    @property
    def registration_id(self):
        """Gets the registration_id of this RegistrationResponse.  # noqa: E501


        :return: The registration_id of this RegistrationResponse.  # noqa: E501
        :rtype: int
        """
        return self._registration_id

    @registration_id.setter
    def registration_id(self, registration_id):
        """Sets the registration_id of this RegistrationResponse.


        :param registration_id: The registration_id of this RegistrationResponse.  # noqa: E501
        :type: int
        """
        if registration_id is None:
            raise ValueError("Invalid value for `registration_id`, must not be `None`")  # noqa: E501

        self._registration_id = registration_id

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
        if issubclass(RegistrationResponse, dict):
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
        if not isinstance(other, RegistrationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
