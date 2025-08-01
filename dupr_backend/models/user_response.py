# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from dupr_backend.models.address_response import AddressResponse
from dupr_backend.models.player_rating_response import PlayerRatingResponse
from dupr_backend.models.role_response import RoleResponse
from dupr_backend.models.user_preferences_response import UserPreferencesResponse
from typing import Optional, Set
from typing_extensions import Self

class UserResponse(BaseModel):
    """
    UserResponse
    """ # noqa: E501
    id: StrictInt
    full_name: StrictStr = Field(alias="fullName")
    first_name: StrictStr = Field(alias="firstName")
    last_name: StrictStr = Field(alias="lastName")
    username: Optional[StrictStr] = None
    display_username: Optional[StrictBool] = Field(default=None, alias="displayUsername")
    iso_code: Optional[StrictStr] = Field(default=None, alias="isoCode")
    phone: Optional[StrictStr] = None
    is_valid_phone: Optional[StrictBool] = Field(default=None, alias="isValidPhone")
    email: StrictStr
    is_valid_email: Optional[StrictBool] = Field(default=None, alias="isValidEmail")
    image_url: Optional[StrictStr] = Field(default=None, alias="imageUrl")
    referral_code: Optional[StrictStr] = Field(default=None, alias="referralCode")
    birthdate: Optional[date] = None
    gender: Optional[StrictStr] = None
    hand: Optional[StrictStr] = None
    role: Optional[RoleResponse] = None
    stats: Optional[PlayerRatingResponse] = None
    addresses: Optional[List[AddressResponse]] = None
    active: StrictBool
    user_preferences: Optional[UserPreferencesResponse] = Field(default=None, alias="userPreferences")
    paddle_brand: Optional[StrictStr] = Field(default=None, alias="paddleBrand")
    shoe_brand: Optional[StrictStr] = Field(default=None, alias="shoeBrand")
    apparel_brand: Optional[StrictStr] = Field(default=None, alias="apparelBrand")
    preferred_ball: Optional[StrictStr] = Field(default=None, alias="preferredBall")
    preferred_side: Optional[StrictStr] = Field(default=None, alias="preferredSide")
    restricted: Optional[StrictBool] = None
    lucra_connected: Optional[StrictBool] = Field(default=None, alias="lucraConnected")
    valid_email: Optional[StrictBool] = Field(default=None, alias="validEmail")
    valid_phone: Optional[StrictBool] = Field(default=None, alias="validPhone")
    __properties: ClassVar[List[str]] = ["id", "fullName", "firstName", "lastName", "username", "displayUsername", "isoCode", "phone", "isValidPhone", "email", "isValidEmail", "imageUrl", "referralCode", "birthdate", "gender", "hand", "role", "stats", "addresses", "active", "userPreferences", "paddleBrand", "shoeBrand", "apparelBrand", "preferredBall", "preferredSide", "restricted", "lucraConnected", "validEmail", "validPhone"]

    @field_validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MALE', 'FEMALE']):
            raise ValueError("must be one of enum values ('MALE', 'FEMALE')")
        return value

    @field_validator('hand')
    def hand_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RIGHT', 'LEFT', 'BOTH', 'NONE']):
            raise ValueError("must be one of enum values ('RIGHT', 'LEFT', 'BOTH', 'NONE')")
        return value

    @field_validator('preferred_side')
    def preferred_side_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RIGHT', 'LEFT', 'EITHER']):
            raise ValueError("must be one of enum values ('RIGHT', 'LEFT', 'EITHER')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item_addresses in self.addresses:
                if _item_addresses:
                    _items.append(_item_addresses.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of user_preferences
        if self.user_preferences:
            _dict['userPreferences'] = self.user_preferences.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "fullName": obj.get("fullName"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "username": obj.get("username"),
            "displayUsername": obj.get("displayUsername"),
            "isoCode": obj.get("isoCode"),
            "phone": obj.get("phone"),
            "isValidPhone": obj.get("isValidPhone"),
            "email": obj.get("email"),
            "isValidEmail": obj.get("isValidEmail"),
            "imageUrl": obj.get("imageUrl"),
            "referralCode": obj.get("referralCode"),
            "birthdate": obj.get("birthdate"),
            "gender": obj.get("gender"),
            "hand": obj.get("hand"),
            "role": RoleResponse.from_dict(obj["role"]) if obj.get("role") is not None else None,
            "stats": PlayerRatingResponse.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "addresses": [AddressResponse.from_dict(_item) for _item in obj["addresses"]] if obj.get("addresses") is not None else None,
            "active": obj.get("active"),
            "userPreferences": UserPreferencesResponse.from_dict(obj["userPreferences"]) if obj.get("userPreferences") is not None else None,
            "paddleBrand": obj.get("paddleBrand"),
            "shoeBrand": obj.get("shoeBrand"),
            "apparelBrand": obj.get("apparelBrand"),
            "preferredBall": obj.get("preferredBall"),
            "preferredSide": obj.get("preferredSide"),
            "restricted": obj.get("restricted"),
            "lucraConnected": obj.get("lucraConnected"),
            "validEmail": obj.get("validEmail"),
            "validPhone": obj.get("validPhone")
        })
        return _obj


