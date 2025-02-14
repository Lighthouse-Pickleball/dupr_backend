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

class UserStatusUpdateRequest(object):
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
        'notes': 'str',
        'status': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'notes': 'notes',
        'status': 'status',
        'user_id': 'userId'
    }

    def __init__(self, notes=None, status=None, user_id=None):  # noqa: E501
        """UserStatusUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._notes = None
        self._status = None
        self._user_id = None
        self.discriminator = None
        if notes is not None:
            self.notes = notes
        self.status = status
        if user_id is not None:
            self.user_id = user_id

    @property
    def notes(self):
        """Gets the notes of this UserStatusUpdateRequest.  # noqa: E501


        :return: The notes of this UserStatusUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UserStatusUpdateRequest.


        :param notes: The notes of this UserStatusUpdateRequest.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def status(self):
        """Gets the status of this UserStatusUpdateRequest.  # noqa: E501


        :return: The status of this UserStatusUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserStatusUpdateRequest.


        :param status: The status of this UserStatusUpdateRequest.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE", "CANCELLED", "COMPLETE", "CONFIRMED", "DELETED", "FORFEITED", "INACTIVE", "INVITED", "IN_PROGRESS", "MATCH_BYE", "NOT_CONFIRMED", "ONGOING", "PENDING", "SUSPENDED_TOS_13", "UPCOMING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user_id(self):
        """Gets the user_id of this UserStatusUpdateRequest.  # noqa: E501


        :return: The user_id of this UserStatusUpdateRequest.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserStatusUpdateRequest.


        :param user_id: The user_id of this UserStatusUpdateRequest.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(UserStatusUpdateRequest, dict):
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
        if not isinstance(other, UserStatusUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
