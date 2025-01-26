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

class ClubListingResponse(object):
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
        'club_id': 'int',
        'club_member_count': 'int',
        'club_name': 'str',
        'created': 'str',
        'media_url': 'str',
        'role': 'ClubRoleResponse',
        'short_address': 'str'
    }

    attribute_map = {
        'club_id': 'clubId',
        'club_member_count': 'clubMemberCount',
        'club_name': 'clubName',
        'created': 'created',
        'media_url': 'mediaUrl',
        'role': 'role',
        'short_address': 'shortAddress'
    }

    def __init__(self, club_id=None, club_member_count=None, club_name=None, created=None, media_url=None, role=None, short_address=None):  # noqa: E501
        """ClubListingResponse - a model defined in Swagger"""  # noqa: E501
        self._club_id = None
        self._club_member_count = None
        self._club_name = None
        self._created = None
        self._media_url = None
        self._role = None
        self._short_address = None
        self.discriminator = None
        self.club_id = club_id
        if club_member_count is not None:
            self.club_member_count = club_member_count
        self.club_name = club_name
        if created is not None:
            self.created = created
        if media_url is not None:
            self.media_url = media_url
        if role is not None:
            self.role = role
        if short_address is not None:
            self.short_address = short_address

    @property
    def club_id(self):
        """Gets the club_id of this ClubListingResponse.  # noqa: E501


        :return: The club_id of this ClubListingResponse.  # noqa: E501
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id):
        """Sets the club_id of this ClubListingResponse.


        :param club_id: The club_id of this ClubListingResponse.  # noqa: E501
        :type: int
        """
        if club_id is None:
            raise ValueError("Invalid value for `club_id`, must not be `None`")  # noqa: E501

        self._club_id = club_id

    @property
    def club_member_count(self):
        """Gets the club_member_count of this ClubListingResponse.  # noqa: E501


        :return: The club_member_count of this ClubListingResponse.  # noqa: E501
        :rtype: int
        """
        return self._club_member_count

    @club_member_count.setter
    def club_member_count(self, club_member_count):
        """Sets the club_member_count of this ClubListingResponse.


        :param club_member_count: The club_member_count of this ClubListingResponse.  # noqa: E501
        :type: int
        """

        self._club_member_count = club_member_count

    @property
    def club_name(self):
        """Gets the club_name of this ClubListingResponse.  # noqa: E501


        :return: The club_name of this ClubListingResponse.  # noqa: E501
        :rtype: str
        """
        return self._club_name

    @club_name.setter
    def club_name(self, club_name):
        """Sets the club_name of this ClubListingResponse.


        :param club_name: The club_name of this ClubListingResponse.  # noqa: E501
        :type: str
        """
        if club_name is None:
            raise ValueError("Invalid value for `club_name`, must not be `None`")  # noqa: E501

        self._club_name = club_name

    @property
    def created(self):
        """Gets the created of this ClubListingResponse.  # noqa: E501


        :return: The created of this ClubListingResponse.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ClubListingResponse.


        :param created: The created of this ClubListingResponse.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def media_url(self):
        """Gets the media_url of this ClubListingResponse.  # noqa: E501


        :return: The media_url of this ClubListingResponse.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this ClubListingResponse.


        :param media_url: The media_url of this ClubListingResponse.  # noqa: E501
        :type: str
        """

        self._media_url = media_url

    @property
    def role(self):
        """Gets the role of this ClubListingResponse.  # noqa: E501


        :return: The role of this ClubListingResponse.  # noqa: E501
        :rtype: ClubRoleResponse
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ClubListingResponse.


        :param role: The role of this ClubListingResponse.  # noqa: E501
        :type: ClubRoleResponse
        """

        self._role = role

    @property
    def short_address(self):
        """Gets the short_address of this ClubListingResponse.  # noqa: E501


        :return: The short_address of this ClubListingResponse.  # noqa: E501
        :rtype: str
        """
        return self._short_address

    @short_address.setter
    def short_address(self, short_address):
        """Sets the short_address of this ClubListingResponse.


        :param short_address: The short_address of this ClubListingResponse.  # noqa: E501
        :type: str
        """

        self._short_address = short_address

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
        if issubclass(ClubListingResponse, dict):
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
        if not isinstance(other, ClubListingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
