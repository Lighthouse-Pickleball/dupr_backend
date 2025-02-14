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

class AddPartnerRequest(object):
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
        'partner_id': 'int',
        'partner_status': 'str'
    }

    attribute_map = {
        'partner_id': 'partnerId',
        'partner_status': 'partnerStatus'
    }

    def __init__(self, partner_id=None, partner_status=None):  # noqa: E501
        """AddPartnerRequest - a model defined in Swagger"""  # noqa: E501
        self._partner_id = None
        self._partner_status = None
        self.discriminator = None
        self.partner_id = partner_id
        self.partner_status = partner_status

    @property
    def partner_id(self):
        """Gets the partner_id of this AddPartnerRequest.  # noqa: E501


        :return: The partner_id of this AddPartnerRequest.  # noqa: E501
        :rtype: int
        """
        return self._partner_id

    @partner_id.setter
    def partner_id(self, partner_id):
        """Sets the partner_id of this AddPartnerRequest.


        :param partner_id: The partner_id of this AddPartnerRequest.  # noqa: E501
        :type: int
        """
        if partner_id is None:
            raise ValueError("Invalid value for `partner_id`, must not be `None`")  # noqa: E501

        self._partner_id = partner_id

    @property
    def partner_status(self):
        """Gets the partner_status of this AddPartnerRequest.  # noqa: E501


        :return: The partner_status of this AddPartnerRequest.  # noqa: E501
        :rtype: str
        """
        return self._partner_status

    @partner_status.setter
    def partner_status(self, partner_status):
        """Sets the partner_status of this AddPartnerRequest.


        :param partner_status: The partner_status of this AddPartnerRequest.  # noqa: E501
        :type: str
        """
        if partner_status is None:
            raise ValueError("Invalid value for `partner_status`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE", "CANCELLED", "COMPLETE", "CONFIRMED", "DELETED", "FORFEITED", "INACTIVE", "INVITED", "IN_PROGRESS", "MATCH_BYE", "NOT_CONFIRMED", "ONGOING", "PENDING", "SUSPENDED_TOS_13", "UPCOMING"]  # noqa: E501
        if partner_status not in allowed_values:
            raise ValueError(
                "Invalid value for `partner_status` ({0}), must be one of {1}"  # noqa: E501
                .format(partner_status, allowed_values)
            )

        self._partner_status = partner_status

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
        if issubclass(AddPartnerRequest, dict):
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
        if not isinstance(other, AddPartnerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
