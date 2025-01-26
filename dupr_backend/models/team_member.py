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

class TeamMember(object):
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
        'created': 'str',
        'first_name': 'str',
        'full_name': 'str',
        'image_url': 'str',
        'last_name': 'str',
        'role': 'str',
        'status': 'str',
        'team_id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'created': 'created',
        'first_name': 'firstName',
        'full_name': 'fullName',
        'image_url': 'imageUrl',
        'last_name': 'lastName',
        'role': 'role',
        'status': 'status',
        'team_id': 'teamId',
        'user_id': 'userId'
    }

    def __init__(self, created=None, first_name=None, full_name=None, image_url=None, last_name=None, role=None, status=None, team_id=None, user_id=None):  # noqa: E501
        """TeamMember - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._first_name = None
        self._full_name = None
        self._image_url = None
        self._last_name = None
        self._role = None
        self._status = None
        self._team_id = None
        self._user_id = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if first_name is not None:
            self.first_name = first_name
        if full_name is not None:
            self.full_name = full_name
        if image_url is not None:
            self.image_url = image_url
        if last_name is not None:
            self.last_name = last_name
        self.role = role
        if status is not None:
            self.status = status
        self.team_id = team_id
        self.user_id = user_id

    @property
    def created(self):
        """Gets the created of this TeamMember.  # noqa: E501


        :return: The created of this TeamMember.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TeamMember.


        :param created: The created of this TeamMember.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def first_name(self):
        """Gets the first_name of this TeamMember.  # noqa: E501


        :return: The first_name of this TeamMember.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this TeamMember.


        :param first_name: The first_name of this TeamMember.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def full_name(self):
        """Gets the full_name of this TeamMember.  # noqa: E501


        :return: The full_name of this TeamMember.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this TeamMember.


        :param full_name: The full_name of this TeamMember.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def image_url(self):
        """Gets the image_url of this TeamMember.  # noqa: E501


        :return: The image_url of this TeamMember.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this TeamMember.


        :param image_url: The image_url of this TeamMember.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def last_name(self):
        """Gets the last_name of this TeamMember.  # noqa: E501


        :return: The last_name of this TeamMember.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this TeamMember.


        :param last_name: The last_name of this TeamMember.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def role(self):
        """Gets the role of this TeamMember.  # noqa: E501


        :return: The role of this TeamMember.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this TeamMember.


        :param role: The role of this TeamMember.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def status(self):
        """Gets the status of this TeamMember.  # noqa: E501


        :return: The status of this TeamMember.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TeamMember.


        :param status: The status of this TeamMember.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "CANCELLED", "COMPLETE", "CONFIRMED", "DELETED", "FORFEITED", "INACTIVE", "INVITED", "IN_PROGRESS", "MATCH_BYE", "NOT_CONFIRMED", "ONGOING", "PENDING", "SUSPENDED_TOS_13", "UPCOMING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def team_id(self):
        """Gets the team_id of this TeamMember.  # noqa: E501


        :return: The team_id of this TeamMember.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this TeamMember.


        :param team_id: The team_id of this TeamMember.  # noqa: E501
        :type: int
        """
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def user_id(self):
        """Gets the user_id of this TeamMember.  # noqa: E501


        :return: The user_id of this TeamMember.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TeamMember.


        :param user_id: The user_id of this TeamMember.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

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
        if issubclass(TeamMember, dict):
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
        if not isinstance(other, TeamMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
