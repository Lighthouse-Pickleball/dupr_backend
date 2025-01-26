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

class SessionResponse(object):
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
        'checkout_url': 'str',
        'previously_paid': 'bool',
        'session_id': 'str'
    }

    attribute_map = {
        'checkout_url': 'checkoutUrl',
        'previously_paid': 'previouslyPaid',
        'session_id': 'sessionId'
    }

    def __init__(self, checkout_url=None, previously_paid=None, session_id=None):  # noqa: E501
        """SessionResponse - a model defined in Swagger"""  # noqa: E501
        self._checkout_url = None
        self._previously_paid = None
        self._session_id = None
        self.discriminator = None
        self.checkout_url = checkout_url
        if previously_paid is not None:
            self.previously_paid = previously_paid
        self.session_id = session_id

    @property
    def checkout_url(self):
        """Gets the checkout_url of this SessionResponse.  # noqa: E501


        :return: The checkout_url of this SessionResponse.  # noqa: E501
        :rtype: str
        """
        return self._checkout_url

    @checkout_url.setter
    def checkout_url(self, checkout_url):
        """Sets the checkout_url of this SessionResponse.


        :param checkout_url: The checkout_url of this SessionResponse.  # noqa: E501
        :type: str
        """
        if checkout_url is None:
            raise ValueError("Invalid value for `checkout_url`, must not be `None`")  # noqa: E501

        self._checkout_url = checkout_url

    @property
    def previously_paid(self):
        """Gets the previously_paid of this SessionResponse.  # noqa: E501


        :return: The previously_paid of this SessionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._previously_paid

    @previously_paid.setter
    def previously_paid(self, previously_paid):
        """Sets the previously_paid of this SessionResponse.


        :param previously_paid: The previously_paid of this SessionResponse.  # noqa: E501
        :type: bool
        """

        self._previously_paid = previously_paid

    @property
    def session_id(self):
        """Gets the session_id of this SessionResponse.  # noqa: E501


        :return: The session_id of this SessionResponse.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this SessionResponse.


        :param session_id: The session_id of this SessionResponse.  # noqa: E501
        :type: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

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
        if issubclass(SessionResponse, dict):
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
        if not isinstance(other, SessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
