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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class SwitchTeamRequest(BaseModel):
    """
    SwitchTeamRequest
    """ # noqa: E501
    registration_id: StrictInt = Field(alias="registrationId")
    player1: StrictInt
    player2: StrictInt
    source_bracket_id: StrictInt = Field(alias="sourceBracketId")
    target_bracket_id: StrictInt = Field(alias="targetBracketId")
    club_id: StrictInt = Field(alias="clubId")
    source_bracket_name: StrictStr = Field(alias="sourceBracketName")
    target_bracket_name: StrictStr = Field(alias="targetBracketName")
    event_name: StrictStr = Field(alias="eventName")
    event_id: StrictInt = Field(alias="eventId")
    re_seed_bracket: StrictBool = Field(alias="reSeedBracket")
    __properties: ClassVar[List[str]] = ["registrationId", "player1", "player2", "sourceBracketId", "targetBracketId", "clubId", "sourceBracketName", "targetBracketName", "eventName", "eventId", "reSeedBracket"]

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
        """Create an instance of SwitchTeamRequest from a JSON string"""
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
        """Create an instance of SwitchTeamRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "registrationId": obj.get("registrationId"),
            "player1": obj.get("player1"),
            "player2": obj.get("player2"),
            "sourceBracketId": obj.get("sourceBracketId"),
            "targetBracketId": obj.get("targetBracketId"),
            "clubId": obj.get("clubId"),
            "sourceBracketName": obj.get("sourceBracketName"),
            "targetBracketName": obj.get("targetBracketName"),
            "eventName": obj.get("eventName"),
            "eventId": obj.get("eventId"),
            "reSeedBracket": obj.get("reSeedBracket")
        })
        return _obj


