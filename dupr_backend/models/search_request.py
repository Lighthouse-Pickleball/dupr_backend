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

class SearchRequest(object):
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
        'bracket_id': 'int',
        'exclude': 'list[int]',
        'exclude_club_members': 'ExcludeClubMembers',
        'filter': 'SearchFilter',
        'include_unclaimed_players': 'bool',
        'limit': 'int',
        'offset': 'int',
        'page_source': 'str',
        'query': 'str',
        'verified_email': 'bool'
    }

    attribute_map = {
        'bracket_id': 'bracketId',
        'exclude': 'exclude',
        'exclude_club_members': 'excludeClubMembers',
        'filter': 'filter',
        'include_unclaimed_players': 'includeUnclaimedPlayers',
        'limit': 'limit',
        'offset': 'offset',
        'page_source': 'pageSource',
        'query': 'query',
        'verified_email': 'verifiedEmail'
    }

    def __init__(self, bracket_id=None, exclude=None, exclude_club_members=None, filter=None, include_unclaimed_players=None, limit=None, offset=None, page_source=None, query=None, verified_email=None):  # noqa: E501
        """SearchRequest - a model defined in Swagger"""  # noqa: E501
        self._bracket_id = None
        self._exclude = None
        self._exclude_club_members = None
        self._filter = None
        self._include_unclaimed_players = None
        self._limit = None
        self._offset = None
        self._page_source = None
        self._query = None
        self._verified_email = None
        self.discriminator = None
        if bracket_id is not None:
            self.bracket_id = bracket_id
        if exclude is not None:
            self.exclude = exclude
        if exclude_club_members is not None:
            self.exclude_club_members = exclude_club_members
        self.filter = filter
        if include_unclaimed_players is not None:
            self.include_unclaimed_players = include_unclaimed_players
        self.limit = limit
        self.offset = offset
        if page_source is not None:
            self.page_source = page_source
        self.query = query
        if verified_email is not None:
            self.verified_email = verified_email

    @property
    def bracket_id(self):
        """Gets the bracket_id of this SearchRequest.  # noqa: E501


        :return: The bracket_id of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._bracket_id

    @bracket_id.setter
    def bracket_id(self, bracket_id):
        """Sets the bracket_id of this SearchRequest.


        :param bracket_id: The bracket_id of this SearchRequest.  # noqa: E501
        :type: int
        """

        self._bracket_id = bracket_id

    @property
    def exclude(self):
        """Gets the exclude of this SearchRequest.  # noqa: E501


        :return: The exclude of this SearchRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this SearchRequest.


        :param exclude: The exclude of this SearchRequest.  # noqa: E501
        :type: list[int]
        """

        self._exclude = exclude

    @property
    def exclude_club_members(self):
        """Gets the exclude_club_members of this SearchRequest.  # noqa: E501


        :return: The exclude_club_members of this SearchRequest.  # noqa: E501
        :rtype: ExcludeClubMembers
        """
        return self._exclude_club_members

    @exclude_club_members.setter
    def exclude_club_members(self, exclude_club_members):
        """Sets the exclude_club_members of this SearchRequest.


        :param exclude_club_members: The exclude_club_members of this SearchRequest.  # noqa: E501
        :type: ExcludeClubMembers
        """

        self._exclude_club_members = exclude_club_members

    @property
    def filter(self):
        """Gets the filter of this SearchRequest.  # noqa: E501


        :return: The filter of this SearchRequest.  # noqa: E501
        :rtype: SearchFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this SearchRequest.


        :param filter: The filter of this SearchRequest.  # noqa: E501
        :type: SearchFilter
        """
        if filter is None:
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def include_unclaimed_players(self):
        """Gets the include_unclaimed_players of this SearchRequest.  # noqa: E501


        :return: The include_unclaimed_players of this SearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_unclaimed_players

    @include_unclaimed_players.setter
    def include_unclaimed_players(self, include_unclaimed_players):
        """Sets the include_unclaimed_players of this SearchRequest.


        :param include_unclaimed_players: The include_unclaimed_players of this SearchRequest.  # noqa: E501
        :type: bool
        """

        self._include_unclaimed_players = include_unclaimed_players

    @property
    def limit(self):
        """Gets the limit of this SearchRequest.  # noqa: E501


        :return: The limit of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchRequest.


        :param limit: The limit of this SearchRequest.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchRequest.  # noqa: E501


        :return: The offset of this SearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchRequest.


        :param offset: The offset of this SearchRequest.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def page_source(self):
        """Gets the page_source of this SearchRequest.  # noqa: E501


        :return: The page_source of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._page_source

    @page_source.setter
    def page_source(self, page_source):
        """Sets the page_source of this SearchRequest.


        :param page_source: The page_source of this SearchRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["LD_ADD_PARTICIPANT"]  # noqa: E501
        if page_source not in allowed_values:
            raise ValueError(
                "Invalid value for `page_source` ({0}), must be one of {1}"  # noqa: E501
                .format(page_source, allowed_values)
            )

        self._page_source = page_source

    @property
    def query(self):
        """Gets the query of this SearchRequest.  # noqa: E501


        :return: The query of this SearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchRequest.


        :param query: The query of this SearchRequest.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def verified_email(self):
        """Gets the verified_email of this SearchRequest.  # noqa: E501


        :return: The verified_email of this SearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._verified_email

    @verified_email.setter
    def verified_email(self, verified_email):
        """Sets the verified_email of this SearchRequest.


        :param verified_email: The verified_email of this SearchRequest.  # noqa: E501
        :type: bool
        """

        self._verified_email = verified_email

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
        if issubclass(SearchRequest, dict):
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
        if not isinstance(other, SearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
