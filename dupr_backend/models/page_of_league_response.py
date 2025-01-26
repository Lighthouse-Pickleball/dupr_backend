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

class PageOfLeagueResponse(object):
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
        'empty': 'bool',
        'has_more': 'bool',
        'has_previous': 'bool',
        'hits': 'list[LeagueResponse]',
        'limit': 'int',
        'offset': 'int',
        'total': 'int',
        'total_value_relation': 'str'
    }

    attribute_map = {
        'empty': 'empty',
        'has_more': 'hasMore',
        'has_previous': 'hasPrevious',
        'hits': 'hits',
        'limit': 'limit',
        'offset': 'offset',
        'total': 'total',
        'total_value_relation': 'totalValueRelation'
    }

    def __init__(self, empty=None, has_more=None, has_previous=None, hits=None, limit=None, offset=None, total=None, total_value_relation=None):  # noqa: E501
        """PageOfLeagueResponse - a model defined in Swagger"""  # noqa: E501
        self._empty = None
        self._has_more = None
        self._has_previous = None
        self._hits = None
        self._limit = None
        self._offset = None
        self._total = None
        self._total_value_relation = None
        self.discriminator = None
        self.empty = empty
        self.has_more = has_more
        self.has_previous = has_previous
        if hits is not None:
            self.hits = hits
        self.limit = limit
        self.offset = offset
        self.total = total
        self.total_value_relation = total_value_relation

    @property
    def empty(self):
        """Gets the empty of this PageOfLeagueResponse.  # noqa: E501

        Are results empty  # noqa: E501

        :return: The empty of this PageOfLeagueResponse.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this PageOfLeagueResponse.

        Are results empty  # noqa: E501

        :param empty: The empty of this PageOfLeagueResponse.  # noqa: E501
        :type: bool
        """
        if empty is None:
            raise ValueError("Invalid value for `empty`, must not be `None`")  # noqa: E501

        self._empty = empty

    @property
    def has_more(self):
        """Gets the has_more of this PageOfLeagueResponse.  # noqa: E501

        Are there any more results to fetch  # noqa: E501

        :return: The has_more of this PageOfLeagueResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this PageOfLeagueResponse.

        Are there any more results to fetch  # noqa: E501

        :param has_more: The has_more of this PageOfLeagueResponse.  # noqa: E501
        :type: bool
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")  # noqa: E501

        self._has_more = has_more

    @property
    def has_previous(self):
        """Gets the has_previous of this PageOfLeagueResponse.  # noqa: E501

        Is there any previous page  # noqa: E501

        :return: The has_previous of this PageOfLeagueResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_previous

    @has_previous.setter
    def has_previous(self, has_previous):
        """Sets the has_previous of this PageOfLeagueResponse.

        Is there any previous page  # noqa: E501

        :param has_previous: The has_previous of this PageOfLeagueResponse.  # noqa: E501
        :type: bool
        """
        if has_previous is None:
            raise ValueError("Invalid value for `has_previous`, must not be `None`")  # noqa: E501

        self._has_previous = has_previous

    @property
    def hits(self):
        """Gets the hits of this PageOfLeagueResponse.  # noqa: E501

        Array of results, can be empty.  # noqa: E501

        :return: The hits of this PageOfLeagueResponse.  # noqa: E501
        :rtype: list[LeagueResponse]
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this PageOfLeagueResponse.

        Array of results, can be empty.  # noqa: E501

        :param hits: The hits of this PageOfLeagueResponse.  # noqa: E501
        :type: list[LeagueResponse]
        """

        self._hits = hits

    @property
    def limit(self):
        """Gets the limit of this PageOfLeagueResponse.  # noqa: E501

        Limit value you sent in the request  # noqa: E501

        :return: The limit of this PageOfLeagueResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfLeagueResponse.

        Limit value you sent in the request  # noqa: E501

        :param limit: The limit of this PageOfLeagueResponse.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this PageOfLeagueResponse.  # noqa: E501

        Offset value you sent in the request  # noqa: E501

        :return: The offset of this PageOfLeagueResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfLeagueResponse.

        Offset value you sent in the request  # noqa: E501

        :param offset: The offset of this PageOfLeagueResponse.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def total(self):
        """Gets the total of this PageOfLeagueResponse.  # noqa: E501

        Total number of results available in database  # noqa: E501

        :return: The total of this PageOfLeagueResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PageOfLeagueResponse.

        Total number of results available in database  # noqa: E501

        :param total: The total of this PageOfLeagueResponse.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def total_value_relation(self):
        """Gets the total_value_relation of this PageOfLeagueResponse.  # noqa: E501

        Relation to total results available.  # noqa: E501

        :return: The total_value_relation of this PageOfLeagueResponse.  # noqa: E501
        :rtype: str
        """
        return self._total_value_relation

    @total_value_relation.setter
    def total_value_relation(self, total_value_relation):
        """Sets the total_value_relation of this PageOfLeagueResponse.

        Relation to total results available.  # noqa: E501

        :param total_value_relation: The total_value_relation of this PageOfLeagueResponse.  # noqa: E501
        :type: str
        """
        if total_value_relation is None:
            raise ValueError("Invalid value for `total_value_relation`, must not be `None`")  # noqa: E501
        allowed_values = ["EQUAL_TO", "GREATER_THAN_OR_EQUAL_TO"]  # noqa: E501
        if total_value_relation not in allowed_values:
            raise ValueError(
                "Invalid value for `total_value_relation` ({0}), must be one of {1}"  # noqa: E501
                .format(total_value_relation, allowed_values)
            )

        self._total_value_relation = total_value_relation

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
        if issubclass(PageOfLeagueResponse, dict):
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
        if not isinstance(other, PageOfLeagueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
