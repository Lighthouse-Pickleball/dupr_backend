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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from dupr_backend.models.basic_user_info import BasicUserInfo
from dupr_backend.models.score_format_response import ScoreFormatResponse
from dupr_backend.models.team_response import TeamResponse
from typing import Optional, Set
from typing_extensions import Self

class MatchResponse(BaseModel):
    """
    MatchResponse
    """ # noqa: E501
    bracket_id: Optional[StrictInt] = Field(default=None, alias="bracketId")
    client_id: Optional[StrictInt] = Field(default=None, alias="clientId")
    club_id: Optional[StrictInt] = Field(default=None, alias="clubId")
    confirmed: StrictBool
    created: Optional[StrictStr] = None
    creator: Optional[BasicUserInfo] = None
    display_identity: StrictStr = Field(alias="displayIdentity")
    elo_calculated: Optional[StrictBool] = Field(default=None, alias="eloCalculated")
    event_date: StrictStr = Field(alias="eventDate")
    event_format: StrictStr = Field(alias="eventFormat")
    event_name: Optional[StrictStr] = Field(default=None, alias="eventName")
    id: Optional[StrictInt] = None
    initialization: Optional[StrictBool] = None
    league: Optional[StrictStr] = None
    league_id: Optional[StrictInt] = Field(default=None, alias="leagueId")
    league_match_id: Optional[StrictInt] = Field(default=None, alias="leagueMatchId")
    location: StrictStr
    match_id: Optional[StrictInt] = Field(default=None, alias="matchId")
    match_score_added: StrictBool = Field(alias="matchScoreAdded")
    match_source: Optional[StrictStr] = Field(default=None, alias="matchSource")
    match_type: Optional[StrictStr] = Field(default=None, alias="matchType")
    modified: Optional[StrictStr] = None
    no_of_games: Optional[StrictInt] = Field(default=None, alias="noOfGames")
    score_format: Optional[ScoreFormatResponse] = Field(default=None, alias="scoreFormat")
    status: Optional[StrictStr] = None
    teams: List[TeamResponse]
    tournament: Optional[StrictStr] = None
    user_id: StrictInt = Field(alias="userId")
    validator: Optional[BasicUserInfo] = None
    venue: StrictStr
    __properties: ClassVar[List[str]] = ["bracketId", "clientId", "clubId", "confirmed", "created", "creator", "displayIdentity", "eloCalculated", "eventDate", "eventFormat", "eventName", "id", "initialization", "league", "leagueId", "leagueMatchId", "location", "matchId", "matchScoreAdded", "matchSource", "matchType", "modified", "noOfGames", "scoreFormat", "status", "teams", "tournament", "userId", "validator", "venue"]

    @field_validator('event_format')
    def event_format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DOUBLES', 'SINGLES']):
            raise ValueError("must be one of enum values ('DOUBLES', 'SINGLES')")
        return value

    @field_validator('match_source')
    def match_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CLUB', 'DUPR', 'EXTERNAL', 'LEAGUE', 'MANUAL', 'PARTNER', 'TOURNAMENT']):
            raise ValueError("must be one of enum values ('CLUB', 'DUPR', 'EXTERNAL', 'LEAGUE', 'MANUAL', 'PARTNER', 'TOURNAMENT')")
        return value

    @field_validator('match_type')
    def match_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RALLY', 'SIDE_ONLY']):
            raise ValueError("must be one of enum values ('RALLY', 'SIDE_ONLY')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING']):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MatchResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score_format
        if self.score_format:
            _dict['scoreFormat'] = self.score_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item_teams in self.teams:
                if _item_teams:
                    _items.append(_item_teams.to_dict())
            _dict['teams'] = _items
        # override the default output from pydantic by calling `to_dict()` of validator
        if self.validator:
            _dict['validator'] = self.validator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bracketId": obj.get("bracketId"),
            "clientId": obj.get("clientId"),
            "clubId": obj.get("clubId"),
            "confirmed": obj.get("confirmed"),
            "created": obj.get("created"),
            "creator": BasicUserInfo.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "displayIdentity": obj.get("displayIdentity"),
            "eloCalculated": obj.get("eloCalculated"),
            "eventDate": obj.get("eventDate"),
            "eventFormat": obj.get("eventFormat"),
            "eventName": obj.get("eventName"),
            "id": obj.get("id"),
            "initialization": obj.get("initialization"),
            "league": obj.get("league"),
            "leagueId": obj.get("leagueId"),
            "leagueMatchId": obj.get("leagueMatchId"),
            "location": obj.get("location"),
            "matchId": obj.get("matchId"),
            "matchScoreAdded": obj.get("matchScoreAdded"),
            "matchSource": obj.get("matchSource"),
            "matchType": obj.get("matchType"),
            "modified": obj.get("modified"),
            "noOfGames": obj.get("noOfGames"),
            "scoreFormat": ScoreFormatResponse.from_dict(obj["scoreFormat"]) if obj.get("scoreFormat") is not None else None,
            "status": obj.get("status"),
            "teams": [TeamResponse.from_dict(_item) for _item in obj["teams"]] if obj.get("teams") is not None else None,
            "tournament": obj.get("tournament"),
            "userId": obj.get("userId"),
            "validator": BasicUserInfo.from_dict(obj["validator"]) if obj.get("validator") is not None else None,
            "venue": obj.get("venue")
        })
        return _obj


