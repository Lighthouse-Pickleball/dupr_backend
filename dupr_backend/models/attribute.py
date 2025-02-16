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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class Attribute(BaseModel):
    """
    Attribute
    """
    children: Optional[Dict[str, Attribute]] = Field(None, alias="_children")
    comment: StrictStr = Field(..., alias="_comment")
    value: StrictStr = Field(...)
    __properties = ["_children", "_comment", "value"]

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
    def from_json(cls, json_str: str) -> Attribute:
        """Create an instance of Attribute from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in children (dict)
        _field_dict = {}
        if self.children:
            for _key in self.children:
                if self.children[_key]:
                    _field_dict[_key] = self.children[_key].to_dict()
            _dict['_children'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Attribute:
        """Create an instance of Attribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Attribute.parse_obj(obj)

        _obj = Attribute.parse_obj({
            "children": dict(
                (_k, Attribute.from_dict(_v))
                for _k, _v in obj.get("_children").items()
            )
            if obj.get("_children") is not None
            else None,
            "comment": obj.get("_comment"),
            "value": obj.get("value")
        })
        return _obj

Attribute.update_forward_refs()

