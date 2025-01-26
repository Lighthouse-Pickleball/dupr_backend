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

class OpenPlayMember(object):
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
        'create_at': 'str',
        'doubles': 'str',
        'dupr_id': 'str',
        'event_id': 'int',
        'id': 'int',
        'name': 'str',
        'singles': 'str'
    }

    attribute_map = {
        'create_at': 'createAt',
        'doubles': 'doubles',
        'dupr_id': 'duprId',
        'event_id': 'eventId',
        'id': 'id',
        'name': 'name',
        'singles': 'singles'
    }

    def __init__(self, create_at=None, doubles=None, dupr_id=None, event_id=None, id=None, name=None, singles=None):  # noqa: E501
        """OpenPlayMember - a model defined in Swagger"""  # noqa: E501
        self._create_at = None
        self._doubles = None
        self._dupr_id = None
        self._event_id = None
        self._id = None
        self._name = None
        self._singles = None
        self.discriminator = None
        if create_at is not None:
            self.create_at = create_at
        if doubles is not None:
            self.doubles = doubles
        if dupr_id is not None:
            self.dupr_id = dupr_id
        self.event_id = event_id
        self.id = id
        if name is not None:
            self.name = name
        if singles is not None:
            self.singles = singles

    @property
    def create_at(self):
        """Gets the create_at of this OpenPlayMember.  # noqa: E501


        :return: The create_at of this OpenPlayMember.  # noqa: E501
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this OpenPlayMember.


        :param create_at: The create_at of this OpenPlayMember.  # noqa: E501
        :type: str
        """

        self._create_at = create_at

    @property
    def doubles(self):
        """Gets the doubles of this OpenPlayMember.  # noqa: E501


        :return: The doubles of this OpenPlayMember.  # noqa: E501
        :rtype: str
        """
        return self._doubles

    @doubles.setter
    def doubles(self, doubles):
        """Sets the doubles of this OpenPlayMember.


        :param doubles: The doubles of this OpenPlayMember.  # noqa: E501
        :type: str
        """

        self._doubles = doubles

    @property
    def dupr_id(self):
        """Gets the dupr_id of this OpenPlayMember.  # noqa: E501


        :return: The dupr_id of this OpenPlayMember.  # noqa: E501
        :rtype: str
        """
        return self._dupr_id

    @dupr_id.setter
    def dupr_id(self, dupr_id):
        """Sets the dupr_id of this OpenPlayMember.


        :param dupr_id: The dupr_id of this OpenPlayMember.  # noqa: E501
        :type: str
        """

        self._dupr_id = dupr_id

    @property
    def event_id(self):
        """Gets the event_id of this OpenPlayMember.  # noqa: E501


        :return: The event_id of this OpenPlayMember.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this OpenPlayMember.


        :param event_id: The event_id of this OpenPlayMember.  # noqa: E501
        :type: int
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def id(self):
        """Gets the id of this OpenPlayMember.  # noqa: E501


        :return: The id of this OpenPlayMember.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OpenPlayMember.


        :param id: The id of this OpenPlayMember.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this OpenPlayMember.  # noqa: E501


        :return: The name of this OpenPlayMember.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenPlayMember.


        :param name: The name of this OpenPlayMember.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def singles(self):
        """Gets the singles of this OpenPlayMember.  # noqa: E501


        :return: The singles of this OpenPlayMember.  # noqa: E501
        :rtype: str
        """
        return self._singles

    @singles.setter
    def singles(self, singles):
        """Sets the singles of this OpenPlayMember.


        :param singles: The singles of this OpenPlayMember.  # noqa: E501
        :type: str
        """

        self._singles = singles

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
        if issubclass(OpenPlayMember, dict):
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
        if not isinstance(other, OpenPlayMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
