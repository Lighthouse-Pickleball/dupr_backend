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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Participant(BaseModel):
    """
    Participant
    """ # noqa: E501
    club_member: StrictBool = Field(alias="clubMember")
    display_username: Optional[StrictBool] = Field(default=None, alias="displayUsername")
    full_name: StrictStr = Field(alias="fullName")
    id: Optional[StrictInt] = None
    is_registered: Optional[StrictBool] = Field(default=None, alias="isRegistered")
    is_substitute: StrictBool = Field(alias="isSubstitute")
    is_wait_listed: StrictBool = Field(alias="isWaitListed")
    partner_status: Optional[StrictStr] = Field(default=None, alias="partnerStatus")
    payment_due: Optional[StrictStr] = Field(default=None, alias="paymentDue")
    payment_refunded: StrictBool = Field(alias="paymentRefunded")
    payment_status: Optional[StrictStr] = Field(default=None, alias="paymentStatus")
    refund_amount: Union[StrictFloat, StrictInt] = Field(alias="refundAmount")
    status: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["clubMember", "displayUsername", "fullName", "id", "isRegistered", "isSubstitute", "isWaitListed", "partnerStatus", "paymentDue", "paymentRefunded", "paymentStatus", "refundAmount", "status", "username"]

    @field_validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING']):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING']):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
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
        """Create an instance of Participant from a JSON string"""
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
        """Create an instance of Participant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clubMember": obj.get("clubMember"),
            "displayUsername": obj.get("displayUsername"),
            "fullName": obj.get("fullName"),
            "id": obj.get("id"),
            "isRegistered": obj.get("isRegistered"),
            "isSubstitute": obj.get("isSubstitute"),
            "isWaitListed": obj.get("isWaitListed"),
            "partnerStatus": obj.get("partnerStatus"),
            "paymentDue": obj.get("paymentDue"),
            "paymentRefunded": obj.get("paymentRefunded"),
            "paymentStatus": obj.get("paymentStatus"),
            "refundAmount": obj.get("refundAmount"),
            "status": obj.get("status"),
            "username": obj.get("username")
        })
        return _obj


