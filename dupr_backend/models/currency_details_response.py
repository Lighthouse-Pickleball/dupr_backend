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

class CurrencyDetailsResponse(object):
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
        'currency_code': 'str',
        'currency_name': 'str',
        'currency_symbol': 'str',
        'min_limit': 'float'
    }

    attribute_map = {
        'currency_code': 'currencyCode',
        'currency_name': 'currencyName',
        'currency_symbol': 'currencySymbol',
        'min_limit': 'minLimit'
    }

    def __init__(self, currency_code=None, currency_name=None, currency_symbol=None, min_limit=None):  # noqa: E501
        """CurrencyDetailsResponse - a model defined in Swagger"""  # noqa: E501
        self._currency_code = None
        self._currency_name = None
        self._currency_symbol = None
        self._min_limit = None
        self.discriminator = None
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.currency_symbol = currency_symbol
        self.min_limit = min_limit

    @property
    def currency_code(self):
        """Gets the currency_code of this CurrencyDetailsResponse.  # noqa: E501


        :return: The currency_code of this CurrencyDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CurrencyDetailsResponse.


        :param currency_code: The currency_code of this CurrencyDetailsResponse.  # noqa: E501
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def currency_name(self):
        """Gets the currency_name of this CurrencyDetailsResponse.  # noqa: E501


        :return: The currency_name of this CurrencyDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency_name

    @currency_name.setter
    def currency_name(self, currency_name):
        """Sets the currency_name of this CurrencyDetailsResponse.


        :param currency_name: The currency_name of this CurrencyDetailsResponse.  # noqa: E501
        :type: str
        """
        if currency_name is None:
            raise ValueError("Invalid value for `currency_name`, must not be `None`")  # noqa: E501

        self._currency_name = currency_name

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this CurrencyDetailsResponse.  # noqa: E501


        :return: The currency_symbol of this CurrencyDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this CurrencyDetailsResponse.


        :param currency_symbol: The currency_symbol of this CurrencyDetailsResponse.  # noqa: E501
        :type: str
        """
        if currency_symbol is None:
            raise ValueError("Invalid value for `currency_symbol`, must not be `None`")  # noqa: E501

        self._currency_symbol = currency_symbol

    @property
    def min_limit(self):
        """Gets the min_limit of this CurrencyDetailsResponse.  # noqa: E501


        :return: The min_limit of this CurrencyDetailsResponse.  # noqa: E501
        :rtype: float
        """
        return self._min_limit

    @min_limit.setter
    def min_limit(self, min_limit):
        """Sets the min_limit of this CurrencyDetailsResponse.


        :param min_limit: The min_limit of this CurrencyDetailsResponse.  # noqa: E501
        :type: float
        """
        if min_limit is None:
            raise ValueError("Invalid value for `min_limit`, must not be `None`")  # noqa: E501

        self._min_limit = min_limit

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
        if issubclass(CurrencyDetailsResponse, dict):
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
        if not isinstance(other, CurrencyDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
