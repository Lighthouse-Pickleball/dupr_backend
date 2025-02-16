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
from dupr_backend.models.session_response import SessionResponse

class SingleWrapperOfSessionResponse(BaseModel):
    """
    SingleWrapperOfSessionResponse
    """
    message: Optional[StrictStr] = None
    result: Optional[SessionResponse] = None
    status: Optional[StrictStr] = None
    __properties = ["message", "result", "status"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('FAILURE', 'REDIRECT', 'SUCCESS'):
            raise ValueError("must be one of enum values ('FAILURE', 'REDIRECT', 'SUCCESS')")
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
    def from_json(cls, json_str: str) -> SingleWrapperOfSessionResponse:
        """Create an instance of SingleWrapperOfSessionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SingleWrapperOfSessionResponse:
        """Create an instance of SingleWrapperOfSessionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SingleWrapperOfSessionResponse.parse_obj(obj)

        _obj = SingleWrapperOfSessionResponse.parse_obj({
            "message": obj.get("message"),
            "result": SessionResponse.from_dict(obj.get("result")) if obj.get("result") is not None else None,
            "status": obj.get("status")
        })
        return _obj


