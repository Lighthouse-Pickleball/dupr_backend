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

class ClaimPlayerSearchFilter(object):
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
        'age': 'AgeFilter',
        'gender': 'str',
        'lat': 'float',
        'lng': 'float',
        'radius_in_meters': 'float',
        'rating': 'ClaimPlayerRatingFilter',
        'short_address': 'str'
    }

    attribute_map = {
        'age': 'age',
        'gender': 'gender',
        'lat': 'lat',
        'lng': 'lng',
        'radius_in_meters': 'radiusInMeters',
        'rating': 'rating',
        'short_address': 'shortAddress'
    }

    def __init__(self, age=None, gender=None, lat=None, lng=None, radius_in_meters=None, rating=None, short_address=None):  # noqa: E501
        """ClaimPlayerSearchFilter - a model defined in Swagger"""  # noqa: E501
        self._age = None
        self._gender = None
        self._lat = None
        self._lng = None
        self._radius_in_meters = None
        self._rating = None
        self._short_address = None
        self.discriminator = None
        if age is not None:
            self.age = age
        if gender is not None:
            self.gender = gender
        if lat is not None:
            self.lat = lat
        if lng is not None:
            self.lng = lng
        if radius_in_meters is not None:
            self.radius_in_meters = radius_in_meters
        if rating is not None:
            self.rating = rating
        if short_address is not None:
            self.short_address = short_address

    @property
    def age(self):
        """Gets the age of this ClaimPlayerSearchFilter.  # noqa: E501


        :return: The age of this ClaimPlayerSearchFilter.  # noqa: E501
        :rtype: AgeFilter
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this ClaimPlayerSearchFilter.


        :param age: The age of this ClaimPlayerSearchFilter.  # noqa: E501
        :type: AgeFilter
        """

        self._age = age

    @property
    def gender(self):
        """Gets the gender of this ClaimPlayerSearchFilter.  # noqa: E501


        :return: The gender of this ClaimPlayerSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ClaimPlayerSearchFilter.


        :param gender: The gender of this ClaimPlayerSearchFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["FEMALE", "MALE"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def lat(self):
        """Gets the lat of this ClaimPlayerSearchFilter.  # noqa: E501


        :return: The lat of this ClaimPlayerSearchFilter.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this ClaimPlayerSearchFilter.


        :param lat: The lat of this ClaimPlayerSearchFilter.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lng(self):
        """Gets the lng of this ClaimPlayerSearchFilter.  # noqa: E501


        :return: The lng of this ClaimPlayerSearchFilter.  # noqa: E501
        :rtype: float
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """Sets the lng of this ClaimPlayerSearchFilter.


        :param lng: The lng of this ClaimPlayerSearchFilter.  # noqa: E501
        :type: float
        """

        self._lng = lng

    @property
    def radius_in_meters(self):
        """Gets the radius_in_meters of this ClaimPlayerSearchFilter.  # noqa: E501


        :return: The radius_in_meters of this ClaimPlayerSearchFilter.  # noqa: E501
        :rtype: float
        """
        return self._radius_in_meters

    @radius_in_meters.setter
    def radius_in_meters(self, radius_in_meters):
        """Sets the radius_in_meters of this ClaimPlayerSearchFilter.


        :param radius_in_meters: The radius_in_meters of this ClaimPlayerSearchFilter.  # noqa: E501
        :type: float
        """

        self._radius_in_meters = radius_in_meters

    @property
    def rating(self):
        """Gets the rating of this ClaimPlayerSearchFilter.  # noqa: E501


        :return: The rating of this ClaimPlayerSearchFilter.  # noqa: E501
        :rtype: ClaimPlayerRatingFilter
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this ClaimPlayerSearchFilter.


        :param rating: The rating of this ClaimPlayerSearchFilter.  # noqa: E501
        :type: ClaimPlayerRatingFilter
        """

        self._rating = rating

    @property
    def short_address(self):
        """Gets the short_address of this ClaimPlayerSearchFilter.  # noqa: E501


        :return: The short_address of this ClaimPlayerSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._short_address

    @short_address.setter
    def short_address(self, short_address):
        """Sets the short_address of this ClaimPlayerSearchFilter.


        :param short_address: The short_address of this ClaimPlayerSearchFilter.  # noqa: E501
        :type: str
        """

        self._short_address = short_address

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
        if issubclass(ClaimPlayerSearchFilter, dict):
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
        if not isinstance(other, ClaimPlayerSearchFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
