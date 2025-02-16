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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class StaffClubMemberRequest(BaseModel):
    """
    StaffClubMemberRequest
    """
    club_id: StrictInt = Field(..., alias="clubId")
    email: StrictStr = Field(...)
    iso_alpha2_code: StrictStr = Field(..., alias="isoAlpha2Code")
    name: StrictStr = Field(...)
    phone: Optional[StrictStr] = None
    role_id: StrictInt = Field(..., alias="roleId")
    user_id: StrictInt = Field(..., alias="userId")
    __properties = ["clubId", "email", "isoAlpha2Code", "name", "phone", "roleId", "userId"]

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
    def from_json(cls, json_str: str) -> StaffClubMemberRequest:
        """Create an instance of StaffClubMemberRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StaffClubMemberRequest:
        """Create an instance of StaffClubMemberRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StaffClubMemberRequest.parse_obj(obj)

        _obj = StaffClubMemberRequest.parse_obj({
            "club_id": obj.get("clubId"),
            "email": obj.get("email"),
            "iso_alpha2_code": obj.get("isoAlpha2Code"),
            "name": obj.get("name"),
            "phone": obj.get("phone"),
            "role_id": obj.get("roleId"),
            "user_id": obj.get("userId")
        })
        return _obj


