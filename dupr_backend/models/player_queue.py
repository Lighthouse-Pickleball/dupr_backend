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

class PlayerQueue(object):
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
        'create_at': 'str',
        'event': 'OpenPlayEvent'
    }

    attribute_map = {
        'create_at': 'createAt',
        'event': 'event'
    }

    def __init__(self, create_at=None, event=None):  # noqa: E501
        """PlayerQueue - a model defined in Swagger"""  # noqa: E501
        self._create_at = None
        self._event = None
        self.discriminator = None
        if create_at is not None:
            self.create_at = create_at
        if event is not None:
            self.event = event

    @property
    def create_at(self):
        """Gets the create_at of this PlayerQueue.  # noqa: E501


        :return: The create_at of this PlayerQueue.  # noqa: E501
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this PlayerQueue.


        :param create_at: The create_at of this PlayerQueue.  # noqa: E501
        :type: str
        """

        self._create_at = create_at

    @property
    def event(self):
        """Gets the event of this PlayerQueue.  # noqa: E501


        :return: The event of this PlayerQueue.  # noqa: E501
        :rtype: OpenPlayEvent
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this PlayerQueue.


        :param event: The event of this PlayerQueue.  # noqa: E501
        :type: OpenPlayEvent
        """

        self._event = event

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
        if issubclass(PlayerQueue, dict):
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
        if not isinstance(other, PlayerQueue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
