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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from dupr_backend.models.team_update_request import TeamUpdateRequest

class MatchUpdateRequest(BaseModel):
    """
    MatchUpdateRequest
    """
    bracket_id: Optional[StrictInt] = Field(None, alias="bracketId")
    confirmed: Optional[StrictBool] = None
    created: Optional[StrictStr] = None
    event_date: Optional[StrictStr] = Field(None, alias="eventDate")
    event_name: Optional[StrictStr] = Field(None, alias="eventName")
    league: Optional[StrictStr] = None
    league_id: Optional[StrictInt] = Field(None, alias="leagueId")
    league_match_id: Optional[StrictInt] = Field(None, alias="leagueMatchId")
    location: Optional[StrictStr] = None
    match_id: Optional[StrictInt] = Field(None, alias="matchId")
    match_source: Optional[StrictStr] = Field(None, alias="matchSource")
    reason: Optional[StrictStr] = None
    requested_by: Optional[StrictStr] = Field(None, alias="requestedBy")
    teams: conlist(TeamUpdateRequest) = Field(...)
    venue: Optional[StrictStr] = None
    __properties = ["bracketId", "confirmed", "created", "eventDate", "eventName", "league", "leagueId", "leagueMatchId", "location", "matchId", "matchSource", "reason", "requestedBy", "teams", "venue"]

    @validator('match_source')
    def match_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CLUB', 'DUPR', 'EXTERNAL', 'LEAGUE', 'MANUAL', 'PARTNER', 'TOURNAMENT'):
            raise ValueError("must be one of enum values ('CLUB', 'DUPR', 'EXTERNAL', 'LEAGUE', 'MANUAL', 'PARTNER', 'TOURNAMENT')")
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
    def from_json(cls, json_str: str) -> MatchUpdateRequest:
        """Create an instance of MatchUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item in self.teams:
                if _item:
                    _items.append(_item.to_dict())
            _dict['teams'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MatchUpdateRequest:
        """Create an instance of MatchUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MatchUpdateRequest.parse_obj(obj)

        _obj = MatchUpdateRequest.parse_obj({
            "bracket_id": obj.get("bracketId"),
            "confirmed": obj.get("confirmed"),
            "created": obj.get("created"),
            "event_date": obj.get("eventDate"),
            "event_name": obj.get("eventName"),
            "league": obj.get("league"),
            "league_id": obj.get("leagueId"),
            "league_match_id": obj.get("leagueMatchId"),
            "location": obj.get("location"),
            "match_id": obj.get("matchId"),
            "match_source": obj.get("matchSource"),
            "reason": obj.get("reason"),
            "requested_by": obj.get("requestedBy"),
            "teams": [TeamUpdateRequest.from_dict(_item) for _item in obj.get("teams")] if obj.get("teams") is not None else None,
            "venue": obj.get("venue")
        })
        return _obj


