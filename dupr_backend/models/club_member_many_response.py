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
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ClubMemberManyResponse(BaseModel):
    """
    ClubMemberManyResponse
    """ # noqa: E501
    add_members_action_s3_url: Optional[StrictStr] = Field(default=None, alias="addMembersActionS3Url")
    in_valid_email: Optional[List[StrictStr]] = Field(default=None, alias="inValidEmail")
    invalid_email: StrictInt = Field(alias="invalidEmail")
    players_added: StrictInt = Field(alias="playersAdded")
    players_invited: StrictInt = Field(alias="playersInvited")
    valid_email: Optional[List[StrictStr]] = Field(default=None, alias="validEmail")
    __properties: ClassVar[List[str]] = ["addMembersActionS3Url", "inValidEmail", "invalidEmail", "playersAdded", "playersInvited", "validEmail"]

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
        """Create an instance of ClubMemberManyResponse from a JSON string"""
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
        """Create an instance of ClubMemberManyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addMembersActionS3Url": obj.get("addMembersActionS3Url"),
            "inValidEmail": obj.get("inValidEmail"),
            "invalidEmail": obj.get("invalidEmail"),
            "playersAdded": obj.get("playersAdded"),
            "playersInvited": obj.get("playersInvited"),
            "validEmail": obj.get("validEmail")
        })
        return _obj


