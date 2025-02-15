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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from dupr_backend.models.player_response import PlayerResponse
from typing import Optional, Set
from typing_extensions import Self

class LeagueStandingResponse(BaseModel):
    """
    LeagueStandingResponse
    """ # noqa: E501
    bracket_id: StrictInt = Field(alias="bracketId")
    game_lost: Optional[StrictInt] = Field(default=None, alias="gameLost")
    game_won: Optional[StrictInt] = Field(default=None, alias="gameWon")
    match_lost: Optional[StrictInt] = Field(default=None, alias="matchLost")
    match_won: Optional[StrictInt] = Field(default=None, alias="matchWon")
    player1: Optional[PlayerResponse] = None
    player2: Optional[PlayerResponse] = None
    point_diff_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pointDiffPercentage")
    point_difference: Optional[StrictInt] = Field(default=None, alias="pointDifference")
    points_conceded: Optional[StrictInt] = Field(default=None, alias="pointsConceded")
    points_scored: Optional[StrictInt] = Field(default=None, alias="pointsScored")
    rank: Optional[StrictInt] = None
    registration_id: StrictInt = Field(alias="registrationId")
    round: StrictInt
    __properties: ClassVar[List[str]] = ["bracketId", "gameLost", "gameWon", "matchLost", "matchWon", "player1", "player2", "pointDiffPercentage", "pointDifference", "pointsConceded", "pointsScored", "rank", "registrationId", "round"]

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
        """Create an instance of LeagueStandingResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of player1
        if self.player1:
            _dict['player1'] = self.player1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of player2
        if self.player2:
            _dict['player2'] = self.player2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LeagueStandingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bracketId": obj.get("bracketId"),
            "gameLost": obj.get("gameLost"),
            "gameWon": obj.get("gameWon"),
            "matchLost": obj.get("matchLost"),
            "matchWon": obj.get("matchWon"),
            "player1": PlayerResponse.from_dict(obj["player1"]) if obj.get("player1") is not None else None,
            "player2": PlayerResponse.from_dict(obj["player2"]) if obj.get("player2") is not None else None,
            "pointDiffPercentage": obj.get("pointDiffPercentage"),
            "pointDifference": obj.get("pointDifference"),
            "pointsConceded": obj.get("pointsConceded"),
            "pointsScored": obj.get("pointsScored"),
            "rank": obj.get("rank"),
            "registrationId": obj.get("registrationId"),
            "round": obj.get("round")
        })
        return _obj


