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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BracketClubRoleResponse(BaseModel):
    """
    BracketClubRoleResponse
    """ # noqa: E501
    is_club_member: StrictBool = Field(alias="isClubMember")
    role_id: StrictInt = Field(alias="roleId")
    role_name: Optional[StrictStr] = Field(default=None, alias="roleName")
    __properties: ClassVar[List[str]] = ["isClubMember", "roleId", "roleName"]

    @field_validator('role_name')
    def role_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ADMIN', 'CAPTAIN', 'DIRECTOR', 'MANAGER', 'MARKETING_EXECUTIVE', 'ORGANIZER', 'PENDING_PLAYER', 'PLAYER', 'SUPPORT_EXECUTIVE']):
            raise ValueError("must be one of enum values ('ADMIN', 'CAPTAIN', 'DIRECTOR', 'MANAGER', 'MARKETING_EXECUTIVE', 'ORGANIZER', 'PENDING_PLAYER', 'PLAYER', 'SUPPORT_EXECUTIVE')")
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
        """Create an instance of BracketClubRoleResponse from a JSON string"""
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
        """Create an instance of BracketClubRoleResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isClubMember": obj.get("isClubMember"),
            "roleId": obj.get("roleId"),
            "roleName": obj.get("roleName")
        })
        return _obj


