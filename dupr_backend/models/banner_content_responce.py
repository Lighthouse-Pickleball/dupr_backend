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

class BannerContentResponce(object):
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
        'content': 'str',
        'content_id': 'int',
        'content_type': 'str',
        'footer': 'str',
        'footer_type': 'str',
        'header': 'str',
        'header_type': 'str'
    }

    attribute_map = {
        'content': 'content',
        'content_id': 'contentId',
        'content_type': 'contentType',
        'footer': 'footer',
        'footer_type': 'footerType',
        'header': 'header',
        'header_type': 'headerType'
    }

    def __init__(self, content=None, content_id=None, content_type=None, footer=None, footer_type=None, header=None, header_type=None):  # noqa: E501
        """BannerContentResponce - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._content_id = None
        self._content_type = None
        self._footer = None
        self._footer_type = None
        self._header = None
        self._header_type = None
        self.discriminator = None
        if content is not None:
            self.content = content
        self.content_id = content_id
        if content_type is not None:
            self.content_type = content_type
        if footer is not None:
            self.footer = footer
        if footer_type is not None:
            self.footer_type = footer_type
        if header is not None:
            self.header = header
        if header_type is not None:
            self.header_type = header_type

    @property
    def content(self):
        """Gets the content of this BannerContentResponce.  # noqa: E501


        :return: The content of this BannerContentResponce.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this BannerContentResponce.


        :param content: The content of this BannerContentResponce.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_id(self):
        """Gets the content_id of this BannerContentResponce.  # noqa: E501


        :return: The content_id of this BannerContentResponce.  # noqa: E501
        :rtype: int
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this BannerContentResponce.


        :param content_id: The content_id of this BannerContentResponce.  # noqa: E501
        :type: int
        """
        if content_id is None:
            raise ValueError("Invalid value for `content_id`, must not be `None`")  # noqa: E501

        self._content_id = content_id

    @property
    def content_type(self):
        """Gets the content_type of this BannerContentResponce.  # noqa: E501


        :return: The content_type of this BannerContentResponce.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this BannerContentResponce.


        :param content_type: The content_type of this BannerContentResponce.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def footer(self):
        """Gets the footer of this BannerContentResponce.  # noqa: E501


        :return: The footer of this BannerContentResponce.  # noqa: E501
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """Sets the footer of this BannerContentResponce.


        :param footer: The footer of this BannerContentResponce.  # noqa: E501
        :type: str
        """

        self._footer = footer

    @property
    def footer_type(self):
        """Gets the footer_type of this BannerContentResponce.  # noqa: E501


        :return: The footer_type of this BannerContentResponce.  # noqa: E501
        :rtype: str
        """
        return self._footer_type

    @footer_type.setter
    def footer_type(self, footer_type):
        """Sets the footer_type of this BannerContentResponce.


        :param footer_type: The footer_type of this BannerContentResponce.  # noqa: E501
        :type: str
        """

        self._footer_type = footer_type

    @property
    def header(self):
        """Gets the header of this BannerContentResponce.  # noqa: E501


        :return: The header of this BannerContentResponce.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this BannerContentResponce.


        :param header: The header of this BannerContentResponce.  # noqa: E501
        :type: str
        """

        self._header = header

    @property
    def header_type(self):
        """Gets the header_type of this BannerContentResponce.  # noqa: E501


        :return: The header_type of this BannerContentResponce.  # noqa: E501
        :rtype: str
        """
        return self._header_type

    @header_type.setter
    def header_type(self, header_type):
        """Sets the header_type of this BannerContentResponce.


        :param header_type: The header_type of this BannerContentResponce.  # noqa: E501
        :type: str
        """

        self._header_type = header_type

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
        if issubclass(BannerContentResponce, dict):
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
        if not isinstance(other, BannerContentResponce):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
