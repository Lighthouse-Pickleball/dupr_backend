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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class TeamMember(BaseModel):
    """
    TeamMember
    """
    created: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    full_name: Optional[StrictStr] = Field(None, alias="fullName")
    image_url: Optional[StrictStr] = Field(None, alias="imageUrl")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    role: StrictStr = Field(...)
    status: Optional[StrictStr] = None
    team_id: StrictInt = Field(..., alias="teamId")
    user_id: StrictInt = Field(..., alias="userId")
    __properties = ["created", "firstName", "fullName", "imageUrl", "lastName", "role", "status", "teamId", "userId"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING'):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TeamMember:
        """Create an instance of TeamMember from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamMember:
        """Create an instance of TeamMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamMember.parse_obj(obj)

        _obj = TeamMember.parse_obj({
            "created": obj.get("created"),
            "first_name": obj.get("firstName"),
            "full_name": obj.get("fullName"),
            "image_url": obj.get("imageUrl"),
            "last_name": obj.get("lastName"),
            "role": obj.get("role"),
            "status": obj.get("status"),
            "team_id": obj.get("teamId"),
            "user_id": obj.get("userId")
        })
        return _obj


