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
from pydantic import BaseModel, Field, StrictInt

class MiLPRegisterTeamRequest(BaseModel):
    """
    MiLPRegisterTeamRequest
    """
    division_id: Optional[StrictInt] = Field(None, alias="divisionId")
    event_id: Optional[StrictInt] = Field(None, alias="eventId")
    team_id: Optional[StrictInt] = Field(None, alias="teamId")
    __properties = ["divisionId", "eventId", "teamId"]

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
    def from_json(cls, json_str: str) -> MiLPRegisterTeamRequest:
        """Create an instance of MiLPRegisterTeamRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MiLPRegisterTeamRequest:
        """Create an instance of MiLPRegisterTeamRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MiLPRegisterTeamRequest.parse_obj(obj)

        _obj = MiLPRegisterTeamRequest.parse_obj({
            "division_id": obj.get("divisionId"),
            "event_id": obj.get("eventId"),
            "team_id": obj.get("teamId")
        })
        return _obj


