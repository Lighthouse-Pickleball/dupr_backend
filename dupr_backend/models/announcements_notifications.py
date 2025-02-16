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
from pydantic import BaseModel, Field, StrictBool, StrictInt

class AnnouncementsNotifications(BaseModel):
    """
    AnnouncementsNotifications
    """
    announcement_id: Optional[StrictInt] = Field(None, alias="announcementId")
    bracket_id: Optional[StrictInt] = Field(None, alias="bracketId")
    email_sent: Optional[StrictBool] = Field(None, alias="emailSent")
    league_id: Optional[StrictInt] = Field(None, alias="leagueId")
    push_sent: Optional[StrictBool] = Field(None, alias="pushSent")
    sms_sent: Optional[StrictBool] = Field(None, alias="smsSent")
    user_id: Optional[StrictInt] = Field(None, alias="userId")
    __properties = ["announcementId", "bracketId", "emailSent", "leagueId", "pushSent", "smsSent", "userId"]

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
    def from_json(cls, json_str: str) -> AnnouncementsNotifications:
        """Create an instance of AnnouncementsNotifications from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnnouncementsNotifications:
        """Create an instance of AnnouncementsNotifications from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AnnouncementsNotifications.parse_obj(obj)

        _obj = AnnouncementsNotifications.parse_obj({
            "announcement_id": obj.get("announcementId"),
            "bracket_id": obj.get("bracketId"),
            "email_sent": obj.get("emailSent"),
            "league_id": obj.get("leagueId"),
            "push_sent": obj.get("pushSent"),
            "sms_sent": obj.get("smsSent"),
            "user_id": obj.get("userId")
        })
        return _obj


