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



from pydantic import BaseModel, Field
from dupr_backend.models.match_info import MatchInfo
from dupr_backend.models.team_info import TeamInfo

class MatchRatingSimulatorRequest(BaseModel):
    """
    MatchRatingSimulatorRequest
    """
    match: MatchInfo = Field(...)
    team1: TeamInfo = Field(...)
    team2: TeamInfo = Field(...)
    __properties = ["match", "team1", "team2"]

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
    def from_json(cls, json_str: str) -> MatchRatingSimulatorRequest:
        """Create an instance of MatchRatingSimulatorRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of match
        if self.match:
            _dict['match'] = self.match.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team1
        if self.team1:
            _dict['team1'] = self.team1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team2
        if self.team2:
            _dict['team2'] = self.team2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MatchRatingSimulatorRequest:
        """Create an instance of MatchRatingSimulatorRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MatchRatingSimulatorRequest.parse_obj(obj)

        _obj = MatchRatingSimulatorRequest.parse_obj({
            "match": MatchInfo.from_dict(obj.get("match")) if obj.get("match") is not None else None,
            "team1": TeamInfo.from_dict(obj.get("team1")) if obj.get("team1") is not None else None,
            "team2": TeamInfo.from_dict(obj.get("team2")) if obj.get("team2") is not None else None
        })
        return _obj


