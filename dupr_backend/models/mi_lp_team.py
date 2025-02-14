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

class MiLPTeam(object):
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
        'status': 'str',
        'team_code': 'str',
        'team_id': 'int',
        'team_members': 'list[TeamMember]',
        'team_name': 'str'
    }

    attribute_map = {
        'created': 'created',
        'status': 'status',
        'team_code': 'teamCode',
        'team_id': 'teamId',
        'team_members': 'teamMembers',
        'team_name': 'teamName'
    }

    def __init__(self, created=None, status=None, team_code=None, team_id=None, team_members=None, team_name=None):  # noqa: E501
        """MiLPTeam - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._status = None
        self._team_code = None
        self._team_id = None
        self._team_members = None
        self._team_name = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if status is not None:
            self.status = status
        if team_code is not None:
            self.team_code = team_code
        self.team_id = team_id
        self.team_members = team_members
        self.team_name = team_name

    @property
    def created(self):
        """Gets the created of this MiLPTeam.  # noqa: E501


        :return: The created of this MiLPTeam.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MiLPTeam.


        :param created: The created of this MiLPTeam.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def status(self):
        """Gets the status of this MiLPTeam.  # noqa: E501


        :return: The status of this MiLPTeam.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MiLPTeam.


        :param status: The status of this MiLPTeam.  # noqa: E501
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
    def team_code(self):
        """Gets the team_code of this MiLPTeam.  # noqa: E501


        :return: The team_code of this MiLPTeam.  # noqa: E501
        :rtype: str
        """
        return self._team_code

    @team_code.setter
    def team_code(self, team_code):
        """Sets the team_code of this MiLPTeam.


        :param team_code: The team_code of this MiLPTeam.  # noqa: E501
        :type: str
        """

        self._team_code = team_code

    @property
    def team_id(self):
        """Gets the team_id of this MiLPTeam.  # noqa: E501


        :return: The team_id of this MiLPTeam.  # noqa: E501
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this MiLPTeam.


        :param team_id: The team_id of this MiLPTeam.  # noqa: E501
        :type: int
        """
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def team_members(self):
        """Gets the team_members of this MiLPTeam.  # noqa: E501


        :return: The team_members of this MiLPTeam.  # noqa: E501
        :rtype: list[TeamMember]
        """
        return self._team_members

    @team_members.setter
    def team_members(self, team_members):
        """Sets the team_members of this MiLPTeam.


        :param team_members: The team_members of this MiLPTeam.  # noqa: E501
        :type: list[TeamMember]
        """
        if team_members is None:
            raise ValueError("Invalid value for `team_members`, must not be `None`")  # noqa: E501

        self._team_members = team_members

    @property
    def team_name(self):
        """Gets the team_name of this MiLPTeam.  # noqa: E501


        :return: The team_name of this MiLPTeam.  # noqa: E501
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """Sets the team_name of this MiLPTeam.


        :param team_name: The team_name of this MiLPTeam.  # noqa: E501
        :type: str
        """
        if team_name is None:
            raise ValueError("Invalid value for `team_name`, must not be `None`")  # noqa: E501

        self._team_name = team_name

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
        if issubclass(MiLPTeam, dict):
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
        if not isinstance(other, MiLPTeam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
