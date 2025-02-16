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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictStr, confloat, conint, validator

class ClaimPlayerRatingFilter(BaseModel):
    """
    ClaimPlayerRatingFilter
    """
    max_rating: Optional[Union[confloat(le=8, ge=2, strict=True), conint(le=8, ge=2, strict=True)]] = Field(None, alias="maxRating")
    min_rating: Optional[Union[confloat(le=8, ge=2, strict=True), conint(le=8, ge=2, strict=True)]] = Field(None, alias="minRating")
    type: Optional[StrictStr] = None
    __properties = ["maxRating", "minRating", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DOUBLES', 'SINGLES'):
            raise ValueError("must be one of enum values ('DOUBLES', 'SINGLES')")
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
    def from_json(cls, json_str: str) -> ClaimPlayerRatingFilter:
        """Create an instance of ClaimPlayerRatingFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClaimPlayerRatingFilter:
        """Create an instance of ClaimPlayerRatingFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClaimPlayerRatingFilter.parse_obj(obj)

        _obj = ClaimPlayerRatingFilter.parse_obj({
            "max_rating": obj.get("maxRating"),
            "min_rating": obj.get("minRating"),
            "type": obj.get("type")
        })
        return _obj


