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
from pydantic import BaseModel, StrictStr, validator

class ReportRequest(BaseModel):
    """
    ReportRequest
    """
    id: Optional[StrictStr] = None
    note: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties = ["id", "note", "reason", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('COMMENT', 'POST'):
            raise ValueError("must be one of enum values ('COMMENT', 'POST')")
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
    def from_json(cls, json_str: str) -> ReportRequest:
        """Create an instance of ReportRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReportRequest:
        """Create an instance of ReportRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReportRequest.parse_obj(obj)

        _obj = ReportRequest.parse_obj({
            "id": obj.get("id"),
            "note": obj.get("note"),
            "reason": obj.get("reason"),
            "type": obj.get("type")
        })
        return _obj


