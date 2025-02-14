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

class UserSearchRequest(object):
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
        'limit': 'int',
        'offset': 'int',
        'query': 'str',
        'search_field': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'query': 'query',
        'search_field': 'searchField'
    }

    def __init__(self, limit=None, offset=None, query=None, search_field=None):  # noqa: E501
        """UserSearchRequest - a model defined in Swagger"""  # noqa: E501
        self._limit = None
        self._offset = None
        self._query = None
        self._search_field = None
        self.discriminator = None
        self.limit = limit
        self.offset = offset
        self.query = query
        if search_field is not None:
            self.search_field = search_field

    @property
    def limit(self):
        """Gets the limit of this UserSearchRequest.  # noqa: E501


        :return: The limit of this UserSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this UserSearchRequest.


        :param limit: The limit of this UserSearchRequest.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this UserSearchRequest.  # noqa: E501


        :return: The offset of this UserSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this UserSearchRequest.


        :param offset: The offset of this UserSearchRequest.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def query(self):
        """Gets the query of this UserSearchRequest.  # noqa: E501


        :return: The query of this UserSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this UserSearchRequest.


        :param query: The query of this UserSearchRequest.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def search_field(self):
        """Gets the search_field of this UserSearchRequest.  # noqa: E501


        :return: The search_field of this UserSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._search_field

    @search_field.setter
    def search_field(self, search_field):
        """Sets the search_field of this UserSearchRequest.


        :param search_field: The search_field of this UserSearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["DUPR_ID", "EMAIL", "FULLNAME", "PHONE"]  # noqa: E501
        if search_field not in allowed_values:
            raise ValueError(
                "Invalid value for `search_field` ({0}), must be one of {1}"  # noqa: E501
                .format(search_field, allowed_values)
            )

        self._search_field = search_field

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
        if issubclass(UserSearchRequest, dict):
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
        if not isinstance(other, UserSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
