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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from dupr_backend.models.seed_match_res import SeedMatchRes

class MatchRoundRes(BaseModel):
    """
    MatchRoundRes
    """
    end_date: Optional[date] = Field(None, alias="endDate")
    matches: conlist(SeedMatchRes) = Field(...)
    serial: StrictInt = Field(...)
    start_date: date = Field(..., alias="startDate")
    team_ids: Optional[conlist(StrictInt)] = Field(None, alias="teamIds")
    __properties = ["endDate", "matches", "serial", "startDate", "teamIds"]

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
    def from_json(cls, json_str: str) -> MatchRoundRes:
        """Create an instance of MatchRoundRes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in matches (list)
        _items = []
        if self.matches:
            for _item in self.matches:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matches'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MatchRoundRes:
        """Create an instance of MatchRoundRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MatchRoundRes.parse_obj(obj)

        _obj = MatchRoundRes.parse_obj({
            "end_date": obj.get("endDate"),
            "matches": [SeedMatchRes.from_dict(_item) for _item in obj.get("matches")] if obj.get("matches") is not None else None,
            "serial": obj.get("serial"),
            "start_date": obj.get("startDate"),
            "team_ids": obj.get("teamIds")
        })
        return _obj


