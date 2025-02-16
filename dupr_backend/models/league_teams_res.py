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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from dupr_backend.models.player_res import PlayerRes

class LeagueTeamsRes(BaseModel):
    """
    LeagueTeamsRes
    """
    partner_status: Optional[StrictStr] = Field(None, alias="partnerStatus")
    payment_status: Optional[StrictStr] = Field(None, alias="paymentStatus")
    player1: Optional[PlayerRes] = None
    player2: Optional[PlayerRes] = None
    registration_id: StrictInt = Field(..., alias="registrationId")
    team_status: Optional[StrictStr] = Field(None, alias="teamStatus")
    __properties = ["partnerStatus", "paymentStatus", "player1", "player2", "registrationId", "teamStatus"]

    @validator('partner_status')
    def partner_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING'):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
        return value

    @validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING'):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
        return value

    @validator('team_status')
    def team_status_validate_enum(cls, value):
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
    def from_json(cls, json_str: str) -> LeagueTeamsRes:
        """Create an instance of LeagueTeamsRes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of player1
        if self.player1:
            _dict['player1'] = self.player1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of player2
        if self.player2:
            _dict['player2'] = self.player2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LeagueTeamsRes:
        """Create an instance of LeagueTeamsRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LeagueTeamsRes.parse_obj(obj)

        _obj = LeagueTeamsRes.parse_obj({
            "partner_status": obj.get("partnerStatus"),
            "payment_status": obj.get("paymentStatus"),
            "player1": PlayerRes.from_dict(obj.get("player1")) if obj.get("player1") is not None else None,
            "player2": PlayerRes.from_dict(obj.get("player2")) if obj.get("player2") is not None else None,
            "registration_id": obj.get("registrationId"),
            "team_status": obj.get("teamStatus")
        })
        return _obj


