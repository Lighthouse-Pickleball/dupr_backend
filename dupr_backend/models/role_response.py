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

class RoleResponse(object):
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
        'id': 'int',
        'permissions': 'dict(str, list[str])',
        'role': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permissions': 'permissions',
        'role': 'role'
    }

    def __init__(self, id=None, permissions=None, role=None):  # noqa: E501
        """RoleResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._permissions = None
        self._role = None
        self.discriminator = None
        self.id = id
        if permissions is not None:
            self.permissions = permissions
        self.role = role

    @property
    def id(self):
        """Gets the id of this RoleResponse.  # noqa: E501


        :return: The id of this RoleResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleResponse.


        :param id: The id of this RoleResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def permissions(self):
        """Gets the permissions of this RoleResponse.  # noqa: E501


        :return: The permissions of this RoleResponse.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this RoleResponse.


        :param permissions: The permissions of this RoleResponse.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._permissions = permissions

    @property
    def role(self):
        """Gets the role of this RoleResponse.  # noqa: E501


        :return: The role of this RoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RoleResponse.


        :param role: The role of this RoleResponse.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

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
        if issubclass(RoleResponse, dict):
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
        if not isinstance(other, RoleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
