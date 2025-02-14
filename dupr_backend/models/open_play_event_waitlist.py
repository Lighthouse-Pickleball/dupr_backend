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

class OpenPlayEventWaitlist(object):
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
        'event_id': 'int',
        'message': 'str',
        'waitlist_position': 'int'
    }

    attribute_map = {
        'event_id': 'eventId',
        'message': 'message',
        'waitlist_position': 'waitlistPosition'
    }

    def __init__(self, event_id=None, message=None, waitlist_position=None):  # noqa: E501
        """OpenPlayEventWaitlist - a model defined in Swagger"""  # noqa: E501
        self._event_id = None
        self._message = None
        self._waitlist_position = None
        self.discriminator = None
        self.event_id = event_id
        if message is not None:
            self.message = message
        self.waitlist_position = waitlist_position

    @property
    def event_id(self):
        """Gets the event_id of this OpenPlayEventWaitlist.  # noqa: E501


        :return: The event_id of this OpenPlayEventWaitlist.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this OpenPlayEventWaitlist.


        :param event_id: The event_id of this OpenPlayEventWaitlist.  # noqa: E501
        :type: int
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def message(self):
        """Gets the message of this OpenPlayEventWaitlist.  # noqa: E501


        :return: The message of this OpenPlayEventWaitlist.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OpenPlayEventWaitlist.


        :param message: The message of this OpenPlayEventWaitlist.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def waitlist_position(self):
        """Gets the waitlist_position of this OpenPlayEventWaitlist.  # noqa: E501


        :return: The waitlist_position of this OpenPlayEventWaitlist.  # noqa: E501
        :rtype: int
        """
        return self._waitlist_position

    @waitlist_position.setter
    def waitlist_position(self, waitlist_position):
        """Sets the waitlist_position of this OpenPlayEventWaitlist.


        :param waitlist_position: The waitlist_position of this OpenPlayEventWaitlist.  # noqa: E501
        :type: int
        """
        if waitlist_position is None:
            raise ValueError("Invalid value for `waitlist_position`, must not be `None`")  # noqa: E501

        self._waitlist_position = waitlist_position

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
        if issubclass(OpenPlayEventWaitlist, dict):
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
        if not isinstance(other, OpenPlayEventWaitlist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
