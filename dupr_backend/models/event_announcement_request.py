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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from dupr_backend.models.announcement_content import AnnouncementContent
from typing import Optional, Set
from typing_extensions import Self

class EventAnnouncementRequest(BaseModel):
    """
    EventAnnouncementRequest
    """ # noqa: E501
    announcement_id: StrictInt = Field(alias="announcementId")
    bracket_id: StrictInt = Field(alias="bracketId")
    club_id: StrictInt = Field(alias="clubId")
    description: AnnouncementContent
    league_id: StrictInt = Field(alias="leagueId")
    title: StrictStr
    __properties: ClassVar[List[str]] = ["announcementId", "bracketId", "clubId", "description", "leagueId", "title"]

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
        """Create an instance of EventAnnouncementRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventAnnouncementRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "announcementId": obj.get("announcementId"),
            "bracketId": obj.get("bracketId"),
            "clubId": obj.get("clubId"),
            "description": AnnouncementContent.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "leagueId": obj.get("leagueId"),
            "title": obj.get("title")
        })
        return _obj


