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

class PlayerRatingHistory(object):
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
        'changed_by_admin': 'bool',
        'created': 'str',
        'doubles': 'float',
        'doubles_provisional': 'bool',
        'match_date': 'str',
        'rating_history_id': 'int',
        'singles': 'float',
        'singles_provisional': 'bool',
        'status': 'str',
        'user_email': 'str',
        'user_id': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'changed_by_admin': 'changedByAdmin',
        'created': 'created',
        'doubles': 'doubles',
        'doubles_provisional': 'doublesProvisional',
        'match_date': 'matchDate',
        'rating_history_id': 'ratingHistoryId',
        'singles': 'singles',
        'singles_provisional': 'singlesProvisional',
        'status': 'status',
        'user_email': 'userEmail',
        'user_id': 'userId',
        'user_name': 'userName'
    }

    def __init__(self, changed_by_admin=None, created=None, doubles=None, doubles_provisional=None, match_date=None, rating_history_id=None, singles=None, singles_provisional=None, status=None, user_email=None, user_id=None, user_name=None):  # noqa: E501
        """PlayerRatingHistory - a model defined in Swagger"""  # noqa: E501
        self._changed_by_admin = None
        self._created = None
        self._doubles = None
        self._doubles_provisional = None
        self._match_date = None
        self._rating_history_id = None
        self._singles = None
        self._singles_provisional = None
        self._status = None
        self._user_email = None
        self._user_id = None
        self._user_name = None
        self.discriminator = None
        self.changed_by_admin = changed_by_admin
        self.created = created
        if doubles is not None:
            self.doubles = doubles
        self.doubles_provisional = doubles_provisional
        if match_date is not None:
            self.match_date = match_date
        self.rating_history_id = rating_history_id
        if singles is not None:
            self.singles = singles
        self.singles_provisional = singles_provisional
        if status is not None:
            self.status = status
        self.user_email = user_email
        self.user_id = user_id
        self.user_name = user_name

    @property
    def changed_by_admin(self):
        """Gets the changed_by_admin of this PlayerRatingHistory.  # noqa: E501


        :return: The changed_by_admin of this PlayerRatingHistory.  # noqa: E501
        :rtype: bool
        """
        return self._changed_by_admin

    @changed_by_admin.setter
    def changed_by_admin(self, changed_by_admin):
        """Sets the changed_by_admin of this PlayerRatingHistory.


        :param changed_by_admin: The changed_by_admin of this PlayerRatingHistory.  # noqa: E501
        :type: bool
        """
        if changed_by_admin is None:
            raise ValueError("Invalid value for `changed_by_admin`, must not be `None`")  # noqa: E501

        self._changed_by_admin = changed_by_admin

    @property
    def created(self):
        """Gets the created of this PlayerRatingHistory.  # noqa: E501


        :return: The created of this PlayerRatingHistory.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PlayerRatingHistory.


        :param created: The created of this PlayerRatingHistory.  # noqa: E501
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def doubles(self):
        """Gets the doubles of this PlayerRatingHistory.  # noqa: E501


        :return: The doubles of this PlayerRatingHistory.  # noqa: E501
        :rtype: float
        """
        return self._doubles

    @doubles.setter
    def doubles(self, doubles):
        """Sets the doubles of this PlayerRatingHistory.


        :param doubles: The doubles of this PlayerRatingHistory.  # noqa: E501
        :type: float
        """

        self._doubles = doubles

    @property
    def doubles_provisional(self):
        """Gets the doubles_provisional of this PlayerRatingHistory.  # noqa: E501


        :return: The doubles_provisional of this PlayerRatingHistory.  # noqa: E501
        :rtype: bool
        """
        return self._doubles_provisional

    @doubles_provisional.setter
    def doubles_provisional(self, doubles_provisional):
        """Sets the doubles_provisional of this PlayerRatingHistory.


        :param doubles_provisional: The doubles_provisional of this PlayerRatingHistory.  # noqa: E501
        :type: bool
        """
        if doubles_provisional is None:
            raise ValueError("Invalid value for `doubles_provisional`, must not be `None`")  # noqa: E501

        self._doubles_provisional = doubles_provisional

    @property
    def match_date(self):
        """Gets the match_date of this PlayerRatingHistory.  # noqa: E501


        :return: The match_date of this PlayerRatingHistory.  # noqa: E501
        :rtype: str
        """
        return self._match_date

    @match_date.setter
    def match_date(self, match_date):
        """Sets the match_date of this PlayerRatingHistory.


        :param match_date: The match_date of this PlayerRatingHistory.  # noqa: E501
        :type: str
        """

        self._match_date = match_date

    @property
    def rating_history_id(self):
        """Gets the rating_history_id of this PlayerRatingHistory.  # noqa: E501


        :return: The rating_history_id of this PlayerRatingHistory.  # noqa: E501
        :rtype: int
        """
        return self._rating_history_id

    @rating_history_id.setter
    def rating_history_id(self, rating_history_id):
        """Sets the rating_history_id of this PlayerRatingHistory.


        :param rating_history_id: The rating_history_id of this PlayerRatingHistory.  # noqa: E501
        :type: int
        """
        if rating_history_id is None:
            raise ValueError("Invalid value for `rating_history_id`, must not be `None`")  # noqa: E501

        self._rating_history_id = rating_history_id

    @property
    def singles(self):
        """Gets the singles of this PlayerRatingHistory.  # noqa: E501


        :return: The singles of this PlayerRatingHistory.  # noqa: E501
        :rtype: float
        """
        return self._singles

    @singles.setter
    def singles(self, singles):
        """Sets the singles of this PlayerRatingHistory.


        :param singles: The singles of this PlayerRatingHistory.  # noqa: E501
        :type: float
        """

        self._singles = singles

    @property
    def singles_provisional(self):
        """Gets the singles_provisional of this PlayerRatingHistory.  # noqa: E501


        :return: The singles_provisional of this PlayerRatingHistory.  # noqa: E501
        :rtype: bool
        """
        return self._singles_provisional

    @singles_provisional.setter
    def singles_provisional(self, singles_provisional):
        """Sets the singles_provisional of this PlayerRatingHistory.


        :param singles_provisional: The singles_provisional of this PlayerRatingHistory.  # noqa: E501
        :type: bool
        """
        if singles_provisional is None:
            raise ValueError("Invalid value for `singles_provisional`, must not be `None`")  # noqa: E501

        self._singles_provisional = singles_provisional

    @property
    def status(self):
        """Gets the status of this PlayerRatingHistory.  # noqa: E501


        :return: The status of this PlayerRatingHistory.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlayerRatingHistory.


        :param status: The status of this PlayerRatingHistory.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_email(self):
        """Gets the user_email of this PlayerRatingHistory.  # noqa: E501


        :return: The user_email of this PlayerRatingHistory.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this PlayerRatingHistory.


        :param user_email: The user_email of this PlayerRatingHistory.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def user_id(self):
        """Gets the user_id of this PlayerRatingHistory.  # noqa: E501


        :return: The user_id of this PlayerRatingHistory.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PlayerRatingHistory.


        :param user_id: The user_id of this PlayerRatingHistory.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this PlayerRatingHistory.  # noqa: E501


        :return: The user_name of this PlayerRatingHistory.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this PlayerRatingHistory.


        :param user_name: The user_name of this PlayerRatingHistory.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

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
        if issubclass(PlayerRatingHistory, dict):
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
        if not isinstance(other, PlayerRatingHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
