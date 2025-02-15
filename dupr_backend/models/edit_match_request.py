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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from dupr_backend.models.edit_score_request import EditScoreRequest
from typing import Optional, Set
from typing_extensions import Self

class EditMatchRequest(BaseModel):
    """
    EditMatchRequest
    """ # noqa: E501
    bracket_id: Optional[StrictInt] = Field(default=None, alias="bracketId")
    is_forfeited: Optional[StrictBool] = Field(default=None, alias="isForfeited")
    league_match_id: Optional[StrictInt] = Field(default=None, alias="leagueMatchId")
    match_date: date = Field(alias="matchDate")
    match_id: StrictInt = Field(alias="matchId")
    team1_score: EditScoreRequest = Field(alias="team1Score")
    team2_score: EditScoreRequest = Field(alias="team2Score")
    __properties: ClassVar[List[str]] = ["bracketId", "isForfeited", "leagueMatchId", "matchDate", "matchId", "team1Score", "team2Score"]

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
        """Create an instance of EditMatchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of team1_score
        if self.team1_score:
            _dict['team1Score'] = self.team1_score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team2_score
        if self.team2_score:
            _dict['team2Score'] = self.team2_score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EditMatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bracketId": obj.get("bracketId"),
            "isForfeited": obj.get("isForfeited"),
            "leagueMatchId": obj.get("leagueMatchId"),
            "matchDate": obj.get("matchDate"),
            "matchId": obj.get("matchId"),
            "team1Score": EditScoreRequest.from_dict(obj["team1Score"]) if obj.get("team1Score") is not None else None,
            "team2Score": EditScoreRequest.from_dict(obj["team2Score"]) if obj.get("team2Score") is not None else None
        })
        return _obj


