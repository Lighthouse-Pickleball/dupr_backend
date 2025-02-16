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

class ContentResponse(BaseModel):
    """
    ContentResponse
    """
    content: StrictStr = Field(...)
    content_id: StrictInt = Field(..., alias="contentId")
    content_type: StrictStr = Field(..., alias="contentType")
    footer: Optional[StrictStr] = None
    footer_type: Optional[StrictStr] = Field(None, alias="footerType")
    header: Optional[StrictStr] = None
    header_type: Optional[StrictStr] = Field(None, alias="headerType")
    __properties = ["content", "contentId", "contentType", "footer", "footerType", "header", "headerType"]

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
    def from_json(cls, json_str: str) -> ContentResponse:
        """Create an instance of ContentResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ContentResponse:
        """Create an instance of ContentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ContentResponse.parse_obj(obj)

        _obj = ContentResponse.parse_obj({
            "content": obj.get("content"),
            "content_id": obj.get("contentId"),
            "content_type": obj.get("contentType"),
            "footer": obj.get("footer"),
            "footer_type": obj.get("footerType"),
            "header": obj.get("header"),
            "header_type": obj.get("headerType")
        })
        return _obj


