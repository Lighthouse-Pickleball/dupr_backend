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

class StaffClubMember(object):
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
        'approval': 'str',
        'club_id': 'int',
        'dupr_id': 'str',
        'email': 'str',
        'iso_alpha2_code': 'str',
        'media_url': 'str',
        'name': 'str',
        'phone': 'str',
        'role_id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'approval': 'approval',
        'club_id': 'clubId',
        'dupr_id': 'duprId',
        'email': 'email',
        'iso_alpha2_code': 'isoAlpha2Code',
        'media_url': 'mediaUrl',
        'name': 'name',
        'phone': 'phone',
        'role_id': 'roleId',
        'user_id': 'userId'
    }

    def __init__(self, approval=None, club_id=None, dupr_id=None, email=None, iso_alpha2_code=None, media_url=None, name=None, phone=None, role_id=None, user_id=None):  # noqa: E501
        """StaffClubMember - a model defined in Swagger"""  # noqa: E501
        self._approval = None
        self._club_id = None
        self._dupr_id = None
        self._email = None
        self._iso_alpha2_code = None
        self._media_url = None
        self._name = None
        self._phone = None
        self._role_id = None
        self._user_id = None
        self.discriminator = None
        self.approval = approval
        self.club_id = club_id
        self.dupr_id = dupr_id
        self.email = email
        self.iso_alpha2_code = iso_alpha2_code
        if media_url is not None:
            self.media_url = media_url
        self.name = name
        if phone is not None:
            self.phone = phone
        self.role_id = role_id
        self.user_id = user_id

    @property
    def approval(self):
        """Gets the approval of this StaffClubMember.  # noqa: E501


        :return: The approval of this StaffClubMember.  # noqa: E501
        :rtype: str
        """
        return self._approval

    @approval.setter
    def approval(self, approval):
        """Sets the approval of this StaffClubMember.


        :param approval: The approval of this StaffClubMember.  # noqa: E501
        :type: str
        """
        if approval is None:
            raise ValueError("Invalid value for `approval`, must not be `None`")  # noqa: E501
        allowed_values = ["APPROVED", "IN_REVIEW", "PENDING", "REJECTED"]  # noqa: E501
        if approval not in allowed_values:
            raise ValueError(
                "Invalid value for `approval` ({0}), must be one of {1}"  # noqa: E501
                .format(approval, allowed_values)
            )

        self._approval = approval

    @property
    def club_id(self):
        """Gets the club_id of this StaffClubMember.  # noqa: E501


        :return: The club_id of this StaffClubMember.  # noqa: E501
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id):
        """Sets the club_id of this StaffClubMember.


        :param club_id: The club_id of this StaffClubMember.  # noqa: E501
        :type: int
        """
        if club_id is None:
            raise ValueError("Invalid value for `club_id`, must not be `None`")  # noqa: E501

        self._club_id = club_id

    @property
    def dupr_id(self):
        """Gets the dupr_id of this StaffClubMember.  # noqa: E501


        :return: The dupr_id of this StaffClubMember.  # noqa: E501
        :rtype: str
        """
        return self._dupr_id

    @dupr_id.setter
    def dupr_id(self, dupr_id):
        """Sets the dupr_id of this StaffClubMember.


        :param dupr_id: The dupr_id of this StaffClubMember.  # noqa: E501
        :type: str
        """
        if dupr_id is None:
            raise ValueError("Invalid value for `dupr_id`, must not be `None`")  # noqa: E501

        self._dupr_id = dupr_id

    @property
    def email(self):
        """Gets the email of this StaffClubMember.  # noqa: E501


        :return: The email of this StaffClubMember.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this StaffClubMember.


        :param email: The email of this StaffClubMember.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def iso_alpha2_code(self):
        """Gets the iso_alpha2_code of this StaffClubMember.  # noqa: E501


        :return: The iso_alpha2_code of this StaffClubMember.  # noqa: E501
        :rtype: str
        """
        return self._iso_alpha2_code

    @iso_alpha2_code.setter
    def iso_alpha2_code(self, iso_alpha2_code):
        """Sets the iso_alpha2_code of this StaffClubMember.


        :param iso_alpha2_code: The iso_alpha2_code of this StaffClubMember.  # noqa: E501
        :type: str
        """
        if iso_alpha2_code is None:
            raise ValueError("Invalid value for `iso_alpha2_code`, must not be `None`")  # noqa: E501

        self._iso_alpha2_code = iso_alpha2_code

    @property
    def media_url(self):
        """Gets the media_url of this StaffClubMember.  # noqa: E501


        :return: The media_url of this StaffClubMember.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this StaffClubMember.


        :param media_url: The media_url of this StaffClubMember.  # noqa: E501
        :type: str
        """

        self._media_url = media_url

    @property
    def name(self):
        """Gets the name of this StaffClubMember.  # noqa: E501


        :return: The name of this StaffClubMember.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StaffClubMember.


        :param name: The name of this StaffClubMember.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this StaffClubMember.  # noqa: E501


        :return: The phone of this StaffClubMember.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this StaffClubMember.


        :param phone: The phone of this StaffClubMember.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def role_id(self):
        """Gets the role_id of this StaffClubMember.  # noqa: E501


        :return: The role_id of this StaffClubMember.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this StaffClubMember.


        :param role_id: The role_id of this StaffClubMember.  # noqa: E501
        :type: int
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def user_id(self):
        """Gets the user_id of this StaffClubMember.  # noqa: E501


        :return: The user_id of this StaffClubMember.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this StaffClubMember.


        :param user_id: The user_id of this StaffClubMember.  # noqa: E501
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
        if issubclass(StaffClubMember, dict):
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
        if not isinstance(other, StaffClubMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
