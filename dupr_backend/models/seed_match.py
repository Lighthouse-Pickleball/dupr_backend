# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from dupr_backend.models.league_teams import LeagueTeams
from typing import Optional, Set
from typing_extensions import Self

class SeedMatch(BaseModel):
    """
    SeedMatch
    """ # noqa: E501
    serial: StrictInt
    team1: Optional[LeagueTeams] = None
    team2: Optional[LeagueTeams] = None
    bye: StrictBool
    match_serial: StrictInt = Field(alias="matchSerial")
    __properties: ClassVar[List[str]] = ["serial", "team1", "team2", "bye", "matchSerial"]

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
        """Create an instance of SeedMatch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of team1
        if self.team1:
            _dict['team1'] = self.team1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team2
        if self.team2:
            _dict['team2'] = self.team2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeedMatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "serial": obj.get("serial"),
            "team1": LeagueTeams.from_dict(obj["team1"]) if obj.get("team1") is not None else None,
            "team2": LeagueTeams.from_dict(obj["team2"]) if obj.get("team2") is not None else None,
            "bye": obj.get("bye"),
            "matchSerial": obj.get("matchSerial")
        })
        return _obj


