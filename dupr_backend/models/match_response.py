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
from dupr_backend.models.basic_user_info import BasicUserInfo
from dupr_backend.models.score_format_response import ScoreFormatResponse
from dupr_backend.models.team_response import TeamResponse

class MatchResponse(BaseModel):
    """
    MatchResponse
    """
    bracket_id: Optional[StrictInt] = Field(None, alias="bracketId")
    client_id: Optional[StrictInt] = Field(None, alias="clientId")
    club_id: Optional[StrictInt] = Field(None, alias="clubId")
    confirmed: StrictBool = Field(...)
    created: Optional[StrictStr] = None
    creator: Optional[BasicUserInfo] = None
    display_identity: StrictStr = Field(..., alias="displayIdentity")
    elo_calculated: Optional[StrictBool] = Field(None, alias="eloCalculated")
    event_date: StrictStr = Field(..., alias="eventDate")
    event_format: StrictStr = Field(..., alias="eventFormat")
    event_name: Optional[StrictStr] = Field(None, alias="eventName")
    id: Optional[StrictInt] = None
    initialization: Optional[StrictBool] = None
    league: Optional[StrictStr] = None
    league_id: Optional[StrictInt] = Field(None, alias="leagueId")
    league_match_id: Optional[StrictInt] = Field(None, alias="leagueMatchId")
    location: StrictStr = Field(...)
    match_id: Optional[StrictInt] = Field(None, alias="matchId")
    match_score_added: StrictBool = Field(..., alias="matchScoreAdded")
    match_source: Optional[StrictStr] = Field(None, alias="matchSource")
    match_type: Optional[StrictStr] = Field(None, alias="matchType")
    modified: Optional[StrictStr] = None
    no_of_games: Optional[StrictInt] = Field(None, alias="noOfGames")
    score_format: Optional[ScoreFormatResponse] = Field(None, alias="scoreFormat")
    status: Optional[StrictStr] = None
    teams: conlist(TeamResponse) = Field(...)
    tournament: StrictStr = Field(...)
    user_id: StrictInt = Field(..., alias="userId")
    validator: Optional[BasicUserInfo] = None
    venue: StrictStr = Field(...)
    __properties = ["bracketId", "clientId", "clubId", "confirmed", "created", "creator", "displayIdentity", "eloCalculated", "eventDate", "eventFormat", "eventName", "id", "initialization", "league", "leagueId", "leagueMatchId", "location", "matchId", "matchScoreAdded", "matchSource", "matchType", "modified", "noOfGames", "scoreFormat", "status", "teams", "tournament", "userId", "validator", "venue"]

    @validator('event_format')
    def event_format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DOUBLES', 'SINGLES'):
            raise ValueError("must be one of enum values ('DOUBLES', 'SINGLES')")
        return value

    @validator('match_source')
    def match_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CLUB', 'DUPR', 'EXTERNAL', 'LEAGUE', 'MANUAL', 'PARTNER', 'TOURNAMENT'):
            raise ValueError("must be one of enum values ('CLUB', 'DUPR', 'EXTERNAL', 'LEAGUE', 'MANUAL', 'PARTNER', 'TOURNAMENT')")
        return value

    @validator('match_type')
    def match_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('RALLY', 'SIDE_ONLY'):
            raise ValueError("must be one of enum values ('RALLY', 'SIDE_ONLY')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING'):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
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
    def from_json(cls, json_str: str) -> MatchResponse:
        """Create an instance of MatchResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score_format
        if self.score_format:
            _dict['scoreFormat'] = self.score_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item in self.teams:
                if _item:
                    _items.append(_item.to_dict())
            _dict['teams'] = _items
        # override the default output from pydantic by calling `to_dict()` of validator
        if self.validator:
            _dict['validator'] = self.validator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MatchResponse:
        """Create an instance of MatchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MatchResponse.parse_obj(obj)

        _obj = MatchResponse.parse_obj({
            "bracket_id": obj.get("bracketId"),
            "client_id": obj.get("clientId"),
            "club_id": obj.get("clubId"),
            "confirmed": obj.get("confirmed"),
            "created": obj.get("created"),
            "creator": BasicUserInfo.from_dict(obj.get("creator")) if obj.get("creator") is not None else None,
            "display_identity": obj.get("displayIdentity"),
            "elo_calculated": obj.get("eloCalculated"),
            "event_date": obj.get("eventDate"),
            "event_format": obj.get("eventFormat"),
            "event_name": obj.get("eventName"),
            "id": obj.get("id"),
            "initialization": obj.get("initialization"),
            "league": obj.get("league"),
            "league_id": obj.get("leagueId"),
            "league_match_id": obj.get("leagueMatchId"),
            "location": obj.get("location"),
            "match_id": obj.get("matchId"),
            "match_score_added": obj.get("matchScoreAdded"),
            "match_source": obj.get("matchSource"),
            "match_type": obj.get("matchType"),
            "modified": obj.get("modified"),
            "no_of_games": obj.get("noOfGames"),
            "score_format": ScoreFormatResponse.from_dict(obj.get("scoreFormat")) if obj.get("scoreFormat") is not None else None,
            "status": obj.get("status"),
            "teams": [TeamResponse.from_dict(_item) for _item in obj.get("teams")] if obj.get("teams") is not None else None,
            "tournament": obj.get("tournament"),
            "user_id": obj.get("userId"),
            "validator": BasicUserInfo.from_dict(obj.get("validator")) if obj.get("validator") is not None else None,
            "venue": obj.get("venue")
        })
        return _obj


