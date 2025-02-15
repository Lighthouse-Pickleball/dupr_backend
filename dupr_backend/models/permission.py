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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Permission(BaseModel):
    """
    Permission
    """ # noqa: E501
    operations: Optional[List[StrictStr]] = None
    resource: StrictStr
    __properties: ClassVar[List[str]] = ["operations", "resource"]

    @field_validator('operations')
    def operations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ADD', 'ALL', 'BULK_ADD', 'DELETE', 'DETAIL', 'DOWNLOAD', 'INVITE', 'MERGE', 'MODIFY', 'NONE', 'REACTIVATE', 'REASSIGN', 'REPLACE', 'SEARCH', 'VERIFY', 'VIEW']):
                raise ValueError("each list item must be one of ('ADD', 'ALL', 'BULK_ADD', 'DELETE', 'DETAIL', 'DOWNLOAD', 'INVITE', 'MERGE', 'MODIFY', 'NONE', 'REACTIVATE', 'REASSIGN', 'REPLACE', 'SEARCH', 'VERIFY', 'VIEW')")
        return value

    @field_validator('resource')
    def resource_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['BRACKET', 'CLUB', 'CLUB_ASSISTANT_DIRECTOR', 'CLUB_CONTACT_INFO', 'CLUB_DIRECTOR_CONTACT_INFO', 'CLUB_LOGO', 'CLUB_MATCH', 'CLUB_MEMBERS', 'CLUB_MEMBER_INFO', 'CLUB_NAME', 'CLUB_ORGANIZER', 'CLUB_ORGANIZER_CONTACT_INFO', 'EVENT', 'INFORMATIVE_BANNER', 'MATCH', 'NONE', 'RATING', 'SUPER', 'USER', 'USER_ACCOUNT', 'USER_EMAIL', 'USER_ROLE', 'VERIFIED_MATCH']):
            raise ValueError("must be one of enum values ('BRACKET', 'CLUB', 'CLUB_ASSISTANT_DIRECTOR', 'CLUB_CONTACT_INFO', 'CLUB_DIRECTOR_CONTACT_INFO', 'CLUB_LOGO', 'CLUB_MATCH', 'CLUB_MEMBERS', 'CLUB_MEMBER_INFO', 'CLUB_NAME', 'CLUB_ORGANIZER', 'CLUB_ORGANIZER_CONTACT_INFO', 'EVENT', 'INFORMATIVE_BANNER', 'MATCH', 'NONE', 'RATING', 'SUPER', 'USER', 'USER_ACCOUNT', 'USER_EMAIL', 'USER_ROLE', 'VERIFIED_MATCH')")
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
        """Create an instance of Permission from a JSON string"""
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
        """Create an instance of Permission from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operations": obj.get("operations"),
            "resource": obj.get("resource")
        })
        return _obj


