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

class Player(object):
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
        'age': 'int',
        'birthdate': 'str',
        'created': 'str',
        'default_rating': 'str',
        'display_username': 'bool',
        'distance': 'str',
        'distance_in_miles': 'float',
        'doubles': 'float',
        'doubles_provisional': 'bool',
        'doubles_reliability': 'float',
        'doubles_verified': 'float',
        'email': 'str',
        'enable_privacy': 'bool',
        'first_name': 'str',
        'formatted_address': 'str',
        'full_name': 'str',
        'gender': 'str',
        'hand': 'str',
        'id': 'int',
        'image_url': 'str',
        'iso_alpha2_code': 'str',
        'last_name': 'str',
        'latitude': 'float',
        'location': 'str',
        'longitude': 'float',
        'lucra_connected': 'bool',
        'phone': 'str',
        'provisional_doubles_rating': 'float',
        'provisional_singles_rating': 'float',
        'referral_code': 'str',
        'registered': 'bool',
        'registration_type': 'str',
        'reliability_score': 'int',
        'short_address': 'str',
        'singles': 'float',
        'singles_provisional': 'bool',
        'singles_reliability': 'float',
        'singles_verified': 'float',
        'sponsor': 'Sponsor',
        'status': 'str',
        'username': 'str',
        'verified_email': 'bool',
        'verified_phone': 'bool'
    }

    attribute_map = {
        'age': 'age',
        'birthdate': 'birthdate',
        'created': 'created',
        'default_rating': 'defaultRating',
        'display_username': 'displayUsername',
        'distance': 'distance',
        'distance_in_miles': 'distanceInMiles',
        'doubles': 'doubles',
        'doubles_provisional': 'doublesProvisional',
        'doubles_reliability': 'doublesReliability',
        'doubles_verified': 'doublesVerified',
        'email': 'email',
        'enable_privacy': 'enablePrivacy',
        'first_name': 'firstName',
        'formatted_address': 'formattedAddress',
        'full_name': 'fullName',
        'gender': 'gender',
        'hand': 'hand',
        'id': 'id',
        'image_url': 'imageUrl',
        'iso_alpha2_code': 'isoAlpha2Code',
        'last_name': 'lastName',
        'latitude': 'latitude',
        'location': 'location',
        'longitude': 'longitude',
        'lucra_connected': 'lucraConnected',
        'phone': 'phone',
        'provisional_doubles_rating': 'provisionalDoublesRating',
        'provisional_singles_rating': 'provisionalSinglesRating',
        'referral_code': 'referralCode',
        'registered': 'registered',
        'registration_type': 'registrationType',
        'reliability_score': 'reliabilityScore',
        'short_address': 'shortAddress',
        'singles': 'singles',
        'singles_provisional': 'singlesProvisional',
        'singles_reliability': 'singlesReliability',
        'singles_verified': 'singlesVerified',
        'sponsor': 'sponsor',
        'status': 'status',
        'username': 'username',
        'verified_email': 'verifiedEmail',
        'verified_phone': 'verifiedPhone'
    }

    def __init__(self, age=None, birthdate=None, created=None, default_rating=None, display_username=None, distance=None, distance_in_miles=None, doubles=None, doubles_provisional=None, doubles_reliability=None, doubles_verified=None, email=None, enable_privacy=None, first_name=None, formatted_address=None, full_name=None, gender=None, hand=None, id=None, image_url=None, iso_alpha2_code=None, last_name=None, latitude=None, location=None, longitude=None, lucra_connected=None, phone=None, provisional_doubles_rating=None, provisional_singles_rating=None, referral_code=None, registered=None, registration_type=None, reliability_score=None, short_address=None, singles=None, singles_provisional=None, singles_reliability=None, singles_verified=None, sponsor=None, status=None, username=None, verified_email=None, verified_phone=None):  # noqa: E501
        """Player - a model defined in Swagger"""  # noqa: E501
        self._age = None
        self._birthdate = None
        self._created = None
        self._default_rating = None
        self._display_username = None
        self._distance = None
        self._distance_in_miles = None
        self._doubles = None
        self._doubles_provisional = None
        self._doubles_reliability = None
        self._doubles_verified = None
        self._email = None
        self._enable_privacy = None
        self._first_name = None
        self._formatted_address = None
        self._full_name = None
        self._gender = None
        self._hand = None
        self._id = None
        self._image_url = None
        self._iso_alpha2_code = None
        self._last_name = None
        self._latitude = None
        self._location = None
        self._longitude = None
        self._lucra_connected = None
        self._phone = None
        self._provisional_doubles_rating = None
        self._provisional_singles_rating = None
        self._referral_code = None
        self._registered = None
        self._registration_type = None
        self._reliability_score = None
        self._short_address = None
        self._singles = None
        self._singles_provisional = None
        self._singles_reliability = None
        self._singles_verified = None
        self._sponsor = None
        self._status = None
        self._username = None
        self._verified_email = None
        self._verified_phone = None
        self.discriminator = None
        if age is not None:
            self.age = age
        if birthdate is not None:
            self.birthdate = birthdate
        if created is not None:
            self.created = created
        if default_rating is not None:
            self.default_rating = default_rating
        self.display_username = display_username
        if distance is not None:
            self.distance = distance
        if distance_in_miles is not None:
            self.distance_in_miles = distance_in_miles
        if doubles is not None:
            self.doubles = doubles
        if doubles_provisional is not None:
            self.doubles_provisional = doubles_provisional
        if doubles_reliability is not None:
            self.doubles_reliability = doubles_reliability
        if doubles_verified is not None:
            self.doubles_verified = doubles_verified
        self.email = email
        self.enable_privacy = enable_privacy
        if first_name is not None:
            self.first_name = first_name
        if formatted_address is not None:
            self.formatted_address = formatted_address
        self.full_name = full_name
        if gender is not None:
            self.gender = gender
        if hand is not None:
            self.hand = hand
        self.id = id
        if image_url is not None:
            self.image_url = image_url
        if iso_alpha2_code is not None:
            self.iso_alpha2_code = iso_alpha2_code
        if last_name is not None:
            self.last_name = last_name
        if latitude is not None:
            self.latitude = latitude
        if location is not None:
            self.location = location
        if longitude is not None:
            self.longitude = longitude
        if lucra_connected is not None:
            self.lucra_connected = lucra_connected
        if phone is not None:
            self.phone = phone
        if provisional_doubles_rating is not None:
            self.provisional_doubles_rating = provisional_doubles_rating
        if provisional_singles_rating is not None:
            self.provisional_singles_rating = provisional_singles_rating
        if referral_code is not None:
            self.referral_code = referral_code
        self.registered = registered
        if registration_type is not None:
            self.registration_type = registration_type
        if reliability_score is not None:
            self.reliability_score = reliability_score
        if short_address is not None:
            self.short_address = short_address
        if singles is not None:
            self.singles = singles
        if singles_provisional is not None:
            self.singles_provisional = singles_provisional
        if singles_reliability is not None:
            self.singles_reliability = singles_reliability
        if singles_verified is not None:
            self.singles_verified = singles_verified
        if sponsor is not None:
            self.sponsor = sponsor
        if status is not None:
            self.status = status
        if username is not None:
            self.username = username
        self.verified_email = verified_email
        self.verified_phone = verified_phone

    @property
    def age(self):
        """Gets the age of this Player.  # noqa: E501


        :return: The age of this Player.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this Player.


        :param age: The age of this Player.  # noqa: E501
        :type: int
        """

        self._age = age

    @property
    def birthdate(self):
        """Gets the birthdate of this Player.  # noqa: E501


        :return: The birthdate of this Player.  # noqa: E501
        :rtype: str
        """
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        """Sets the birthdate of this Player.


        :param birthdate: The birthdate of this Player.  # noqa: E501
        :type: str
        """

        self._birthdate = birthdate

    @property
    def created(self):
        """Gets the created of this Player.  # noqa: E501


        :return: The created of this Player.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Player.


        :param created: The created of this Player.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def default_rating(self):
        """Gets the default_rating of this Player.  # noqa: E501


        :return: The default_rating of this Player.  # noqa: E501
        :rtype: str
        """
        return self._default_rating

    @default_rating.setter
    def default_rating(self, default_rating):
        """Sets the default_rating of this Player.


        :param default_rating: The default_rating of this Player.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOUBLES", "SINGLES"]  # noqa: E501
        if default_rating not in allowed_values:
            raise ValueError(
                "Invalid value for `default_rating` ({0}), must be one of {1}"  # noqa: E501
                .format(default_rating, allowed_values)
            )

        self._default_rating = default_rating

    @property
    def display_username(self):
        """Gets the display_username of this Player.  # noqa: E501


        :return: The display_username of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._display_username

    @display_username.setter
    def display_username(self, display_username):
        """Sets the display_username of this Player.


        :param display_username: The display_username of this Player.  # noqa: E501
        :type: bool
        """
        if display_username is None:
            raise ValueError("Invalid value for `display_username`, must not be `None`")  # noqa: E501

        self._display_username = display_username

    @property
    def distance(self):
        """Gets the distance of this Player.  # noqa: E501


        :return: The distance of this Player.  # noqa: E501
        :rtype: str
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Player.


        :param distance: The distance of this Player.  # noqa: E501
        :type: str
        """

        self._distance = distance

    @property
    def distance_in_miles(self):
        """Gets the distance_in_miles of this Player.  # noqa: E501


        :return: The distance_in_miles of this Player.  # noqa: E501
        :rtype: float
        """
        return self._distance_in_miles

    @distance_in_miles.setter
    def distance_in_miles(self, distance_in_miles):
        """Sets the distance_in_miles of this Player.


        :param distance_in_miles: The distance_in_miles of this Player.  # noqa: E501
        :type: float
        """

        self._distance_in_miles = distance_in_miles

    @property
    def doubles(self):
        """Gets the doubles of this Player.  # noqa: E501


        :return: The doubles of this Player.  # noqa: E501
        :rtype: float
        """
        return self._doubles

    @doubles.setter
    def doubles(self, doubles):
        """Sets the doubles of this Player.


        :param doubles: The doubles of this Player.  # noqa: E501
        :type: float
        """

        self._doubles = doubles

    @property
    def doubles_provisional(self):
        """Gets the doubles_provisional of this Player.  # noqa: E501


        :return: The doubles_provisional of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._doubles_provisional

    @doubles_provisional.setter
    def doubles_provisional(self, doubles_provisional):
        """Sets the doubles_provisional of this Player.


        :param doubles_provisional: The doubles_provisional of this Player.  # noqa: E501
        :type: bool
        """

        self._doubles_provisional = doubles_provisional

    @property
    def doubles_reliability(self):
        """Gets the doubles_reliability of this Player.  # noqa: E501


        :return: The doubles_reliability of this Player.  # noqa: E501
        :rtype: float
        """
        return self._doubles_reliability

    @doubles_reliability.setter
    def doubles_reliability(self, doubles_reliability):
        """Sets the doubles_reliability of this Player.


        :param doubles_reliability: The doubles_reliability of this Player.  # noqa: E501
        :type: float
        """

        self._doubles_reliability = doubles_reliability

    @property
    def doubles_verified(self):
        """Gets the doubles_verified of this Player.  # noqa: E501


        :return: The doubles_verified of this Player.  # noqa: E501
        :rtype: float
        """
        return self._doubles_verified

    @doubles_verified.setter
    def doubles_verified(self, doubles_verified):
        """Sets the doubles_verified of this Player.


        :param doubles_verified: The doubles_verified of this Player.  # noqa: E501
        :type: float
        """

        self._doubles_verified = doubles_verified

    @property
    def email(self):
        """Gets the email of this Player.  # noqa: E501


        :return: The email of this Player.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Player.


        :param email: The email of this Player.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def enable_privacy(self):
        """Gets the enable_privacy of this Player.  # noqa: E501


        :return: The enable_privacy of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._enable_privacy

    @enable_privacy.setter
    def enable_privacy(self, enable_privacy):
        """Sets the enable_privacy of this Player.


        :param enable_privacy: The enable_privacy of this Player.  # noqa: E501
        :type: bool
        """
        if enable_privacy is None:
            raise ValueError("Invalid value for `enable_privacy`, must not be `None`")  # noqa: E501

        self._enable_privacy = enable_privacy

    @property
    def first_name(self):
        """Gets the first_name of this Player.  # noqa: E501


        :return: The first_name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Player.


        :param first_name: The first_name of this Player.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def formatted_address(self):
        """Gets the formatted_address of this Player.  # noqa: E501


        :return: The formatted_address of this Player.  # noqa: E501
        :rtype: str
        """
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, formatted_address):
        """Sets the formatted_address of this Player.


        :param formatted_address: The formatted_address of this Player.  # noqa: E501
        :type: str
        """

        self._formatted_address = formatted_address

    @property
    def full_name(self):
        """Gets the full_name of this Player.  # noqa: E501


        :return: The full_name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Player.


        :param full_name: The full_name of this Player.  # noqa: E501
        :type: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def gender(self):
        """Gets the gender of this Player.  # noqa: E501


        :return: The gender of this Player.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Player.


        :param gender: The gender of this Player.  # noqa: E501
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
    def hand(self):
        """Gets the hand of this Player.  # noqa: E501


        :return: The hand of this Player.  # noqa: E501
        :rtype: str
        """
        return self._hand

    @hand.setter
    def hand(self, hand):
        """Sets the hand of this Player.


        :param hand: The hand of this Player.  # noqa: E501
        :type: str
        """
        allowed_values = ["BOTH", "LEFT", "NONE", "RIGHT"]  # noqa: E501
        if hand not in allowed_values:
            raise ValueError(
                "Invalid value for `hand` ({0}), must be one of {1}"  # noqa: E501
                .format(hand, allowed_values)
            )

        self._hand = hand

    @property
    def id(self):
        """Gets the id of this Player.  # noqa: E501


        :return: The id of this Player.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Player.


        :param id: The id of this Player.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image_url(self):
        """Gets the image_url of this Player.  # noqa: E501


        :return: The image_url of this Player.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Player.


        :param image_url: The image_url of this Player.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def iso_alpha2_code(self):
        """Gets the iso_alpha2_code of this Player.  # noqa: E501


        :return: The iso_alpha2_code of this Player.  # noqa: E501
        :rtype: str
        """
        return self._iso_alpha2_code

    @iso_alpha2_code.setter
    def iso_alpha2_code(self, iso_alpha2_code):
        """Sets the iso_alpha2_code of this Player.


        :param iso_alpha2_code: The iso_alpha2_code of this Player.  # noqa: E501
        :type: str
        """

        self._iso_alpha2_code = iso_alpha2_code

    @property
    def last_name(self):
        """Gets the last_name of this Player.  # noqa: E501


        :return: The last_name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Player.


        :param last_name: The last_name of this Player.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def latitude(self):
        """Gets the latitude of this Player.  # noqa: E501


        :return: The latitude of this Player.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Player.


        :param latitude: The latitude of this Player.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def location(self):
        """Gets the location of this Player.  # noqa: E501


        :return: The location of this Player.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Player.


        :param location: The location of this Player.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def longitude(self):
        """Gets the longitude of this Player.  # noqa: E501


        :return: The longitude of this Player.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Player.


        :param longitude: The longitude of this Player.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def lucra_connected(self):
        """Gets the lucra_connected of this Player.  # noqa: E501


        :return: The lucra_connected of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._lucra_connected

    @lucra_connected.setter
    def lucra_connected(self, lucra_connected):
        """Sets the lucra_connected of this Player.


        :param lucra_connected: The lucra_connected of this Player.  # noqa: E501
        :type: bool
        """

        self._lucra_connected = lucra_connected

    @property
    def phone(self):
        """Gets the phone of this Player.  # noqa: E501


        :return: The phone of this Player.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Player.


        :param phone: The phone of this Player.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def provisional_doubles_rating(self):
        """Gets the provisional_doubles_rating of this Player.  # noqa: E501


        :return: The provisional_doubles_rating of this Player.  # noqa: E501
        :rtype: float
        """
        return self._provisional_doubles_rating

    @provisional_doubles_rating.setter
    def provisional_doubles_rating(self, provisional_doubles_rating):
        """Sets the provisional_doubles_rating of this Player.


        :param provisional_doubles_rating: The provisional_doubles_rating of this Player.  # noqa: E501
        :type: float
        """

        self._provisional_doubles_rating = provisional_doubles_rating

    @property
    def provisional_singles_rating(self):
        """Gets the provisional_singles_rating of this Player.  # noqa: E501


        :return: The provisional_singles_rating of this Player.  # noqa: E501
        :rtype: float
        """
        return self._provisional_singles_rating

    @provisional_singles_rating.setter
    def provisional_singles_rating(self, provisional_singles_rating):
        """Sets the provisional_singles_rating of this Player.


        :param provisional_singles_rating: The provisional_singles_rating of this Player.  # noqa: E501
        :type: float
        """

        self._provisional_singles_rating = provisional_singles_rating

    @property
    def referral_code(self):
        """Gets the referral_code of this Player.  # noqa: E501


        :return: The referral_code of this Player.  # noqa: E501
        :rtype: str
        """
        return self._referral_code

    @referral_code.setter
    def referral_code(self, referral_code):
        """Sets the referral_code of this Player.


        :param referral_code: The referral_code of this Player.  # noqa: E501
        :type: str
        """

        self._referral_code = referral_code

    @property
    def registered(self):
        """Gets the registered of this Player.  # noqa: E501


        :return: The registered of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._registered

    @registered.setter
    def registered(self, registered):
        """Sets the registered of this Player.


        :param registered: The registered of this Player.  # noqa: E501
        :type: bool
        """
        if registered is None:
            raise ValueError("Invalid value for `registered`, must not be `None`")  # noqa: E501

        self._registered = registered

    @property
    def registration_type(self):
        """Gets the registration_type of this Player.  # noqa: E501


        :return: The registration_type of this Player.  # noqa: E501
        :rtype: str
        """
        return self._registration_type

    @registration_type.setter
    def registration_type(self, registration_type):
        """Sets the registration_type of this Player.


        :param registration_type: The registration_type of this Player.  # noqa: E501
        :type: str
        """
        allowed_values = ["INVITATION", "UNCLAIMED"]  # noqa: E501
        if registration_type not in allowed_values:
            raise ValueError(
                "Invalid value for `registration_type` ({0}), must be one of {1}"  # noqa: E501
                .format(registration_type, allowed_values)
            )

        self._registration_type = registration_type

    @property
    def reliability_score(self):
        """Gets the reliability_score of this Player.  # noqa: E501


        :return: The reliability_score of this Player.  # noqa: E501
        :rtype: int
        """
        return self._reliability_score

    @reliability_score.setter
    def reliability_score(self, reliability_score):
        """Sets the reliability_score of this Player.


        :param reliability_score: The reliability_score of this Player.  # noqa: E501
        :type: int
        """

        self._reliability_score = reliability_score

    @property
    def short_address(self):
        """Gets the short_address of this Player.  # noqa: E501


        :return: The short_address of this Player.  # noqa: E501
        :rtype: str
        """
        return self._short_address

    @short_address.setter
    def short_address(self, short_address):
        """Sets the short_address of this Player.


        :param short_address: The short_address of this Player.  # noqa: E501
        :type: str
        """

        self._short_address = short_address

    @property
    def singles(self):
        """Gets the singles of this Player.  # noqa: E501


        :return: The singles of this Player.  # noqa: E501
        :rtype: float
        """
        return self._singles

    @singles.setter
    def singles(self, singles):
        """Sets the singles of this Player.


        :param singles: The singles of this Player.  # noqa: E501
        :type: float
        """

        self._singles = singles

    @property
    def singles_provisional(self):
        """Gets the singles_provisional of this Player.  # noqa: E501


        :return: The singles_provisional of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._singles_provisional

    @singles_provisional.setter
    def singles_provisional(self, singles_provisional):
        """Sets the singles_provisional of this Player.


        :param singles_provisional: The singles_provisional of this Player.  # noqa: E501
        :type: bool
        """

        self._singles_provisional = singles_provisional

    @property
    def singles_reliability(self):
        """Gets the singles_reliability of this Player.  # noqa: E501


        :return: The singles_reliability of this Player.  # noqa: E501
        :rtype: float
        """
        return self._singles_reliability

    @singles_reliability.setter
    def singles_reliability(self, singles_reliability):
        """Sets the singles_reliability of this Player.


        :param singles_reliability: The singles_reliability of this Player.  # noqa: E501
        :type: float
        """

        self._singles_reliability = singles_reliability

    @property
    def singles_verified(self):
        """Gets the singles_verified of this Player.  # noqa: E501


        :return: The singles_verified of this Player.  # noqa: E501
        :rtype: float
        """
        return self._singles_verified

    @singles_verified.setter
    def singles_verified(self, singles_verified):
        """Sets the singles_verified of this Player.


        :param singles_verified: The singles_verified of this Player.  # noqa: E501
        :type: float
        """

        self._singles_verified = singles_verified

    @property
    def sponsor(self):
        """Gets the sponsor of this Player.  # noqa: E501


        :return: The sponsor of this Player.  # noqa: E501
        :rtype: Sponsor
        """
        return self._sponsor

    @sponsor.setter
    def sponsor(self, sponsor):
        """Sets the sponsor of this Player.


        :param sponsor: The sponsor of this Player.  # noqa: E501
        :type: Sponsor
        """

        self._sponsor = sponsor

    @property
    def status(self):
        """Gets the status of this Player.  # noqa: E501


        :return: The status of this Player.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Player.


        :param status: The status of this Player.  # noqa: E501
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
    def username(self):
        """Gets the username of this Player.  # noqa: E501


        :return: The username of this Player.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Player.


        :param username: The username of this Player.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def verified_email(self):
        """Gets the verified_email of this Player.  # noqa: E501


        :return: The verified_email of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._verified_email

    @verified_email.setter
    def verified_email(self, verified_email):
        """Sets the verified_email of this Player.


        :param verified_email: The verified_email of this Player.  # noqa: E501
        :type: bool
        """
        if verified_email is None:
            raise ValueError("Invalid value for `verified_email`, must not be `None`")  # noqa: E501

        self._verified_email = verified_email

    @property
    def verified_phone(self):
        """Gets the verified_phone of this Player.  # noqa: E501


        :return: The verified_phone of this Player.  # noqa: E501
        :rtype: bool
        """
        return self._verified_phone

    @verified_phone.setter
    def verified_phone(self, verified_phone):
        """Sets the verified_phone of this Player.


        :param verified_phone: The verified_phone of this Player.  # noqa: E501
        :type: bool
        """
        if verified_phone is None:
            raise ValueError("Invalid value for `verified_phone`, must not be `None`")  # noqa: E501

        self._verified_phone = verified_phone

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
        if issubclass(Player, dict):
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
        if not isinstance(other, Player):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
