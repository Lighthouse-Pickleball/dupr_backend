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



from pydantic import BaseModel, Field, StrictInt
from dupr_backend.models.forfeit_team_request import ForfeitTeamRequest

class ForfeitMatchRequest(BaseModel):
    """
    ForfeitMatchRequest
    """
    bracket_id: StrictInt = Field(..., alias="bracketId")
    club_id: StrictInt = Field(..., alias="clubId")
    league_match_id: StrictInt = Field(..., alias="leagueMatchId")
    match_id: StrictInt = Field(..., alias="matchId")
    team1: ForfeitTeamRequest = Field(...)
    team2: ForfeitTeamRequest = Field(...)
    __properties = ["bracketId", "clubId", "leagueMatchId", "matchId", "team1", "team2"]

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
    def from_json(cls, json_str: str) -> ForfeitMatchRequest:
        """Create an instance of ForfeitMatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of team1
        if self.team1:
            _dict['team1'] = self.team1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team2
        if self.team2:
            _dict['team2'] = self.team2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ForfeitMatchRequest:
        """Create an instance of ForfeitMatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ForfeitMatchRequest.parse_obj(obj)

        _obj = ForfeitMatchRequest.parse_obj({
            "bracket_id": obj.get("bracketId"),
            "club_id": obj.get("clubId"),
            "league_match_id": obj.get("leagueMatchId"),
            "match_id": obj.get("matchId"),
            "team1": ForfeitTeamRequest.from_dict(obj.get("team1")) if obj.get("team1") is not None else None,
            "team2": ForfeitTeamRequest.from_dict(obj.get("team2")) if obj.get("team2") is not None else None
        })
        return _obj


