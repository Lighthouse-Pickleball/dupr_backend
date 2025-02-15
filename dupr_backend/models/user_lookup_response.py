# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
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
from dupr_backend.models.role_response import RoleResponse
from typing import Optional, Set
from typing_extensions import Self

class UserLookupResponse(BaseModel):
    """
    UserLookupResponse
    """ # noqa: E501
    birthdate: Optional[date] = None
    created: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    external_id: Optional[StrictStr] = Field(default=None, alias="externalId")
    full_name: Optional[StrictStr] = Field(default=None, alias="fullName")
    gender: Optional[StrictStr] = None
    hand: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    image_url: Optional[StrictStr] = Field(default=None, alias="imageUrl")
    is_valid_email: Optional[StrictBool] = Field(default=None, alias="isValidEmail")
    is_valid_phone: Optional[StrictBool] = Field(default=None, alias="isValidPhone")
    phone_number: Optional[StrictStr] = Field(default=None, alias="phoneNumber")
    referral_code: Optional[StrictStr] = Field(default=None, alias="referralCode")
    registered: Optional[StrictBool] = None
    restricted: Optional[StrictBool] = None
    role: Optional[RoleResponse] = None
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["birthdate", "created", "email", "externalId", "fullName", "gender", "hand", "id", "imageUrl", "isValidEmail", "isValidPhone", "phoneNumber", "referralCode", "registered", "restricted", "role", "status"]

    @field_validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['FEMALE', 'MALE']):
            raise ValueError("must be one of enum values ('FEMALE', 'MALE')")
        return value

    @field_validator('hand')
    def hand_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BOTH', 'LEFT', 'NONE', 'RIGHT']):
            raise ValueError("must be one of enum values ('BOTH', 'LEFT', 'NONE', 'RIGHT')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING']):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
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
        """Create an instance of UserLookupResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserLookupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "birthdate": obj.get("birthdate"),
            "created": obj.get("created"),
            "email": obj.get("email"),
            "externalId": obj.get("externalId"),
            "fullName": obj.get("fullName"),
            "gender": obj.get("gender"),
            "hand": obj.get("hand"),
            "id": obj.get("id"),
            "imageUrl": obj.get("imageUrl"),
            "isValidEmail": obj.get("isValidEmail"),
            "isValidPhone": obj.get("isValidPhone"),
            "phoneNumber": obj.get("phoneNumber"),
            "referralCode": obj.get("referralCode"),
            "registered": obj.get("registered"),
            "restricted": obj.get("restricted"),
            "role": RoleResponse.from_dict(obj["role"]) if obj.get("role") is not None else None,
            "status": obj.get("status")
        })
        return _obj


