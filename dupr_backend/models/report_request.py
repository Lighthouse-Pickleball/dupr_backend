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

class ReportRequest(object):
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
        'id': 'str',
        'note': 'str',
        'reason': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'note': 'note',
        'reason': 'reason',
        'type': 'type'
    }

    def __init__(self, id=None, note=None, reason=None, type=None):  # noqa: E501
        """ReportRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._note = None
        self._reason = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if note is not None:
            self.note = note
        if reason is not None:
            self.reason = reason
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this ReportRequest.  # noqa: E501


        :return: The id of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportRequest.


        :param id: The id of this ReportRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def note(self):
        """Gets the note of this ReportRequest.  # noqa: E501


        :return: The note of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ReportRequest.


        :param note: The note of this ReportRequest.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def reason(self):
        """Gets the reason of this ReportRequest.  # noqa: E501


        :return: The reason of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ReportRequest.


        :param reason: The reason of this ReportRequest.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def type(self):
        """Gets the type of this ReportRequest.  # noqa: E501


        :return: The type of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReportRequest.


        :param type: The type of this ReportRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMMENT", "POST"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ReportRequest, dict):
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
        if not isinstance(other, ReportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
