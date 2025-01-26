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

class ArrayWrapperOfLeagueTeamsResponse(object):
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
        'message': 'str',
        'results': 'list[LeagueTeamsResponse]',
        'status': 'str'
    }

    attribute_map = {
        'message': 'message',
        'results': 'results',
        'status': 'status'
    }

    def __init__(self, message=None, results=None, status=None):  # noqa: E501
        """ArrayWrapperOfLeagueTeamsResponse - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._results = None
        self._status = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if results is not None:
            self.results = results
        if status is not None:
            self.status = status

    @property
    def message(self):
        """Gets the message of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501


        :return: The message of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ArrayWrapperOfLeagueTeamsResponse.


        :param message: The message of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def results(self):
        """Gets the results of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501


        :return: The results of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501
        :rtype: list[LeagueTeamsResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ArrayWrapperOfLeagueTeamsResponse.


        :param results: The results of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501
        :type: list[LeagueTeamsResponse]
        """

        self._results = results

    @property
    def status(self):
        """Gets the status of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501


        :return: The status of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ArrayWrapperOfLeagueTeamsResponse.


        :param status: The status of this ArrayWrapperOfLeagueTeamsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["FAILURE", "REDIRECT", "SUCCESS"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(ArrayWrapperOfLeagueTeamsResponse, dict):
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
        if not isinstance(other, ArrayWrapperOfLeagueTeamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
