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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ClubRole(BaseModel):
    """
    ClubRole
    """ # noqa: E501
    approval_status: StrictStr = Field(alias="approvalStatus")
    club_id: StrictInt = Field(alias="clubId")
    created: Optional[StrictStr] = None
    join_type: Optional[StrictStr] = Field(default=None, alias="joinType")
    request_by: Optional[StrictInt] = Field(default=None, alias="requestBy")
    role: StrictStr
    role_id: StrictInt = Field(alias="roleId")
    __properties: ClassVar[List[str]] = ["approvalStatus", "clubId", "created", "joinType", "requestBy", "role", "roleId"]

    @field_validator('approval_status')
    def approval_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['APPROVED', 'IN_REVIEW', 'PENDING', 'REJECTED']):
            raise ValueError("must be one of enum values ('APPROVED', 'IN_REVIEW', 'PENDING', 'REJECTED')")
        return value

    @field_validator('join_type')
    def join_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INVITATION', 'INVITATION_CSV', 'PARTNER_INVITE', 'REQUEST']):
            raise ValueError("must be one of enum values ('INVITATION', 'INVITATION_CSV', 'PARTNER_INVITE', 'REQUEST')")
        return value

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
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
        """Create an instance of ClubRole from a JSON string"""
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
        """Create an instance of ClubRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "approvalStatus": obj.get("approvalStatus"),
            "clubId": obj.get("clubId"),
            "created": obj.get("created"),
            "joinType": obj.get("joinType"),
            "requestBy": obj.get("requestBy"),
            "role": obj.get("role"),
            "roleId": obj.get("roleId")
        })
        return _obj


