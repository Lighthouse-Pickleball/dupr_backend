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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator

class Participant(BaseModel):
    """
    Participant
    """
    club_member: StrictBool = Field(..., alias="clubMember")
    display_username: Optional[StrictBool] = Field(None, alias="displayUsername")
    full_name: StrictStr = Field(..., alias="fullName")
    id: Optional[StrictInt] = None
    is_registered: Optional[StrictBool] = Field(None, alias="isRegistered")
    is_substitute: StrictBool = Field(..., alias="isSubstitute")
    is_wait_listed: StrictBool = Field(..., alias="isWaitListed")
    partner_status: Optional[StrictStr] = Field(None, alias="partnerStatus")
    payment_due: Optional[StrictStr] = Field(None, alias="paymentDue")
    payment_refunded: StrictBool = Field(..., alias="paymentRefunded")
    payment_status: Optional[StrictStr] = Field(None, alias="paymentStatus")
    refund_amount: Union[StrictFloat, StrictInt] = Field(..., alias="refundAmount")
    status: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    __properties = ["clubMember", "displayUsername", "fullName", "id", "isRegistered", "isSubstitute", "isWaitListed", "partnerStatus", "paymentDue", "paymentRefunded", "paymentStatus", "refundAmount", "status", "username"]

    @validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING'):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
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
    def from_json(cls, json_str: str) -> Participant:
        """Create an instance of Participant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Participant:
        """Create an instance of Participant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Participant.parse_obj(obj)

        _obj = Participant.parse_obj({
            "club_member": obj.get("clubMember"),
            "display_username": obj.get("displayUsername"),
            "full_name": obj.get("fullName"),
            "id": obj.get("id"),
            "is_registered": obj.get("isRegistered"),
            "is_substitute": obj.get("isSubstitute"),
            "is_wait_listed": obj.get("isWaitListed"),
            "partner_status": obj.get("partnerStatus"),
            "payment_due": obj.get("paymentDue"),
            "payment_refunded": obj.get("paymentRefunded"),
            "payment_status": obj.get("paymentStatus"),
            "refund_amount": obj.get("refundAmount"),
            "status": obj.get("status"),
            "username": obj.get("username")
        })
        return _obj


