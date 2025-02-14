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

class ClubMemberManyResponse(object):
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
        'add_members_action_s3_url': 'str',
        'in_valid_email': 'list[str]',
        'invalid_email': 'int',
        'players_added': 'int',
        'players_invited': 'int',
        'valid_email': 'list[str]'
    }

    attribute_map = {
        'add_members_action_s3_url': 'addMembersActionS3Url',
        'in_valid_email': 'inValidEmail',
        'invalid_email': 'invalidEmail',
        'players_added': 'playersAdded',
        'players_invited': 'playersInvited',
        'valid_email': 'validEmail'
    }

    def __init__(self, add_members_action_s3_url=None, in_valid_email=None, invalid_email=None, players_added=None, players_invited=None, valid_email=None):  # noqa: E501
        """ClubMemberManyResponse - a model defined in Swagger"""  # noqa: E501
        self._add_members_action_s3_url = None
        self._in_valid_email = None
        self._invalid_email = None
        self._players_added = None
        self._players_invited = None
        self._valid_email = None
        self.discriminator = None
        if add_members_action_s3_url is not None:
            self.add_members_action_s3_url = add_members_action_s3_url
        if in_valid_email is not None:
            self.in_valid_email = in_valid_email
        self.invalid_email = invalid_email
        self.players_added = players_added
        self.players_invited = players_invited
        if valid_email is not None:
            self.valid_email = valid_email

    @property
    def add_members_action_s3_url(self):
        """Gets the add_members_action_s3_url of this ClubMemberManyResponse.  # noqa: E501


        :return: The add_members_action_s3_url of this ClubMemberManyResponse.  # noqa: E501
        :rtype: str
        """
        return self._add_members_action_s3_url

    @add_members_action_s3_url.setter
    def add_members_action_s3_url(self, add_members_action_s3_url):
        """Sets the add_members_action_s3_url of this ClubMemberManyResponse.


        :param add_members_action_s3_url: The add_members_action_s3_url of this ClubMemberManyResponse.  # noqa: E501
        :type: str
        """

        self._add_members_action_s3_url = add_members_action_s3_url

    @property
    def in_valid_email(self):
        """Gets the in_valid_email of this ClubMemberManyResponse.  # noqa: E501


        :return: The in_valid_email of this ClubMemberManyResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._in_valid_email

    @in_valid_email.setter
    def in_valid_email(self, in_valid_email):
        """Sets the in_valid_email of this ClubMemberManyResponse.


        :param in_valid_email: The in_valid_email of this ClubMemberManyResponse.  # noqa: E501
        :type: list[str]
        """

        self._in_valid_email = in_valid_email

    @property
    def invalid_email(self):
        """Gets the invalid_email of this ClubMemberManyResponse.  # noqa: E501


        :return: The invalid_email of this ClubMemberManyResponse.  # noqa: E501
        :rtype: int
        """
        return self._invalid_email

    @invalid_email.setter
    def invalid_email(self, invalid_email):
        """Sets the invalid_email of this ClubMemberManyResponse.


        :param invalid_email: The invalid_email of this ClubMemberManyResponse.  # noqa: E501
        :type: int
        """
        if invalid_email is None:
            raise ValueError("Invalid value for `invalid_email`, must not be `None`")  # noqa: E501

        self._invalid_email = invalid_email

    @property
    def players_added(self):
        """Gets the players_added of this ClubMemberManyResponse.  # noqa: E501


        :return: The players_added of this ClubMemberManyResponse.  # noqa: E501
        :rtype: int
        """
        return self._players_added

    @players_added.setter
    def players_added(self, players_added):
        """Sets the players_added of this ClubMemberManyResponse.


        :param players_added: The players_added of this ClubMemberManyResponse.  # noqa: E501
        :type: int
        """
        if players_added is None:
            raise ValueError("Invalid value for `players_added`, must not be `None`")  # noqa: E501

        self._players_added = players_added

    @property
    def players_invited(self):
        """Gets the players_invited of this ClubMemberManyResponse.  # noqa: E501


        :return: The players_invited of this ClubMemberManyResponse.  # noqa: E501
        :rtype: int
        """
        return self._players_invited

    @players_invited.setter
    def players_invited(self, players_invited):
        """Sets the players_invited of this ClubMemberManyResponse.


        :param players_invited: The players_invited of this ClubMemberManyResponse.  # noqa: E501
        :type: int
        """
        if players_invited is None:
            raise ValueError("Invalid value for `players_invited`, must not be `None`")  # noqa: E501

        self._players_invited = players_invited

    @property
    def valid_email(self):
        """Gets the valid_email of this ClubMemberManyResponse.  # noqa: E501


        :return: The valid_email of this ClubMemberManyResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._valid_email

    @valid_email.setter
    def valid_email(self, valid_email):
        """Sets the valid_email of this ClubMemberManyResponse.


        :param valid_email: The valid_email of this ClubMemberManyResponse.  # noqa: E501
        :type: list[str]
        """

        self._valid_email = valid_email

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
        if issubclass(ClubMemberManyResponse, dict):
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
        if not isinstance(other, ClubMemberManyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
