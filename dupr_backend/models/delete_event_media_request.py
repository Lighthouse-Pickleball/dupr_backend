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

class DeleteEventMediaRequest(object):
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
        'league_id': 'int',
        'liability_waiver_id': 'int',
        'media_id': 'int'
    }

    attribute_map = {
        'league_id': 'leagueId',
        'liability_waiver_id': 'liabilityWaiverId',
        'media_id': 'mediaId'
    }

    def __init__(self, league_id=None, liability_waiver_id=None, media_id=None):  # noqa: E501
        """DeleteEventMediaRequest - a model defined in Swagger"""  # noqa: E501
        self._league_id = None
        self._liability_waiver_id = None
        self._media_id = None
        self.discriminator = None
        self.league_id = league_id
        if liability_waiver_id is not None:
            self.liability_waiver_id = liability_waiver_id
        if media_id is not None:
            self.media_id = media_id

    @property
    def league_id(self):
        """Gets the league_id of this DeleteEventMediaRequest.  # noqa: E501


        :return: The league_id of this DeleteEventMediaRequest.  # noqa: E501
        :rtype: int
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this DeleteEventMediaRequest.


        :param league_id: The league_id of this DeleteEventMediaRequest.  # noqa: E501
        :type: int
        """
        if league_id is None:
            raise ValueError("Invalid value for `league_id`, must not be `None`")  # noqa: E501

        self._league_id = league_id

    @property
    def liability_waiver_id(self):
        """Gets the liability_waiver_id of this DeleteEventMediaRequest.  # noqa: E501


        :return: The liability_waiver_id of this DeleteEventMediaRequest.  # noqa: E501
        :rtype: int
        """
        return self._liability_waiver_id

    @liability_waiver_id.setter
    def liability_waiver_id(self, liability_waiver_id):
        """Sets the liability_waiver_id of this DeleteEventMediaRequest.


        :param liability_waiver_id: The liability_waiver_id of this DeleteEventMediaRequest.  # noqa: E501
        :type: int
        """

        self._liability_waiver_id = liability_waiver_id

    @property
    def media_id(self):
        """Gets the media_id of this DeleteEventMediaRequest.  # noqa: E501


        :return: The media_id of this DeleteEventMediaRequest.  # noqa: E501
        :rtype: int
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this DeleteEventMediaRequest.


        :param media_id: The media_id of this DeleteEventMediaRequest.  # noqa: E501
        :type: int
        """

        self._media_id = media_id

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
        if issubclass(DeleteEventMediaRequest, dict):
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
        if not isinstance(other, DeleteEventMediaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
