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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from dupr_backend.models.team_info0 import TeamInfo0
from typing import Optional, Set
from typing_extensions import Self

class MatchRatingSimulatorResponse(BaseModel):
    """
    MatchRatingSimulatorResponse
    """ # noqa: E501
    event_format: StrictStr = Field(alias="eventFormat")
    match_source: StrictStr = Field(alias="matchSource")
    teams: List[TeamInfo0]
    __properties: ClassVar[List[str]] = ["eventFormat", "matchSource", "teams"]

    @field_validator('event_format')
    def event_format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DOUBLES', 'SINGLES']):
            raise ValueError("must be one of enum values ('DOUBLES', 'SINGLES')")
        return value

    @field_validator('match_source')
    def match_source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CLUB', 'DUPR', 'EXTERNAL', 'LEAGUE', 'MANUAL', 'PARTNER', 'TOURNAMENT']):
            raise ValueError("must be one of enum values ('CLUB', 'DUPR', 'EXTERNAL', 'LEAGUE', 'MANUAL', 'PARTNER', 'TOURNAMENT')")
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
        """Create an instance of MatchRatingSimulatorResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item_teams in self.teams:
                if _item_teams:
                    _items.append(_item_teams.to_dict())
            _dict['teams'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchRatingSimulatorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventFormat": obj.get("eventFormat"),
            "matchSource": obj.get("matchSource"),
            "teams": [TeamInfo0.from_dict(_item) for _item in obj["teams"]] if obj.get("teams") is not None else None
        })
        return _obj


