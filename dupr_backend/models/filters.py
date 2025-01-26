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

class Filters(object):
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
        'is_registered': 'bool',
        'is_wait_listed': 'bool',
        'partner_status': 'str',
        'payment_status': 'str',
        'registration_status': 'str'
    }

    attribute_map = {
        'is_registered': 'isRegistered',
        'is_wait_listed': 'isWaitListed',
        'partner_status': 'partnerStatus',
        'payment_status': 'paymentStatus',
        'registration_status': 'registrationStatus'
    }

    def __init__(self, is_registered=None, is_wait_listed=None, partner_status=None, payment_status=None, registration_status=None):  # noqa: E501
        """Filters - a model defined in Swagger"""  # noqa: E501
        self._is_registered = None
        self._is_wait_listed = None
        self._partner_status = None
        self._payment_status = None
        self._registration_status = None
        self.discriminator = None
        if is_registered is not None:
            self.is_registered = is_registered
        if is_wait_listed is not None:
            self.is_wait_listed = is_wait_listed
        if partner_status is not None:
            self.partner_status = partner_status
        if payment_status is not None:
            self.payment_status = payment_status
        if registration_status is not None:
            self.registration_status = registration_status

    @property
    def is_registered(self):
        """Gets the is_registered of this Filters.  # noqa: E501


        :return: The is_registered of this Filters.  # noqa: E501
        :rtype: bool
        """
        return self._is_registered

    @is_registered.setter
    def is_registered(self, is_registered):
        """Sets the is_registered of this Filters.


        :param is_registered: The is_registered of this Filters.  # noqa: E501
        :type: bool
        """

        self._is_registered = is_registered

    @property
    def is_wait_listed(self):
        """Gets the is_wait_listed of this Filters.  # noqa: E501


        :return: The is_wait_listed of this Filters.  # noqa: E501
        :rtype: bool
        """
        return self._is_wait_listed

    @is_wait_listed.setter
    def is_wait_listed(self, is_wait_listed):
        """Sets the is_wait_listed of this Filters.


        :param is_wait_listed: The is_wait_listed of this Filters.  # noqa: E501
        :type: bool
        """

        self._is_wait_listed = is_wait_listed

    @property
    def partner_status(self):
        """Gets the partner_status of this Filters.  # noqa: E501


        :return: The partner_status of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._partner_status

    @partner_status.setter
    def partner_status(self, partner_status):
        """Sets the partner_status of this Filters.


        :param partner_status: The partner_status of this Filters.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_PARTNER", "PENDING", "REGISTERED"]  # noqa: E501
        if partner_status not in allowed_values:
            raise ValueError(
                "Invalid value for `partner_status` ({0}), must be one of {1}"  # noqa: E501
                .format(partner_status, allowed_values)
            )

        self._partner_status = partner_status

    @property
    def payment_status(self):
        """Gets the payment_status of this Filters.  # noqa: E501


        :return: The payment_status of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this Filters.


        :param payment_status: The payment_status of this Filters.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "CANCELLED", "COMPLETE", "CONFIRMED", "DELETED", "FORFEITED", "INACTIVE", "INVITED", "IN_PROGRESS", "MATCH_BYE", "NOT_CONFIRMED", "ONGOING", "PENDING", "SUSPENDED_TOS_13", "UPCOMING"]  # noqa: E501
        if payment_status not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_status` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_status, allowed_values)
            )

        self._payment_status = payment_status

    @property
    def registration_status(self):
        """Gets the registration_status of this Filters.  # noqa: E501


        :return: The registration_status of this Filters.  # noqa: E501
        :rtype: str
        """
        return self._registration_status

    @registration_status.setter
    def registration_status(self, registration_status):
        """Sets the registration_status of this Filters.


        :param registration_status: The registration_status of this Filters.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLOSED", "NOT_STARTED", "OPEN"]  # noqa: E501
        if registration_status not in allowed_values:
            raise ValueError(
                "Invalid value for `registration_status` ({0}), must be one of {1}"  # noqa: E501
                .format(registration_status, allowed_values)
            )

        self._registration_status = registration_status

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
        if issubclass(Filters, dict):
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
        if not isinstance(other, Filters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
