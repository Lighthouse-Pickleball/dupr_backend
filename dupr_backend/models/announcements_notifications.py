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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AnnouncementsNotifications(BaseModel):
    """
    AnnouncementsNotifications
    """ # noqa: E501
    announcement_id: Optional[StrictInt] = Field(default=None, alias="announcementId")
    bracket_id: Optional[StrictInt] = Field(default=None, alias="bracketId")
    email_sent: Optional[StrictBool] = Field(default=None, alias="emailSent")
    league_id: Optional[StrictInt] = Field(default=None, alias="leagueId")
    push_sent: Optional[StrictBool] = Field(default=None, alias="pushSent")
    sms_sent: Optional[StrictBool] = Field(default=None, alias="smsSent")
    user_id: Optional[StrictInt] = Field(default=None, alias="userId")
    __properties: ClassVar[List[str]] = ["announcementId", "bracketId", "emailSent", "leagueId", "pushSent", "smsSent", "userId"]

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
        """Create an instance of AnnouncementsNotifications from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnnouncementsNotifications from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "announcementId": obj.get("announcementId"),
            "bracketId": obj.get("bracketId"),
            "emailSent": obj.get("emailSent"),
            "leagueId": obj.get("leagueId"),
            "pushSent": obj.get("pushSent"),
            "smsSent": obj.get("smsSent"),
            "userId": obj.get("userId")
        })
        return _obj


