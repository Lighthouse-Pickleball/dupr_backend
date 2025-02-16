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


from typing import Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator

class PaymentDetailsResponse(BaseModel):
    """
    PaymentDetailsResponse
    """
    amount_paid: Union[StrictFloat, StrictInt] = Field(..., alias="amountPaid")
    event_fee: Union[StrictFloat, StrictInt] = Field(..., alias="eventFee")
    is_club_member: StrictBool = Field(..., alias="isClubMember")
    is_registered: StrictBool = Field(..., alias="isRegistered")
    is_wait_listed: StrictBool = Field(..., alias="isWaitListed")
    payment_capture: StrictBool = Field(..., alias="paymentCapture")
    payment_status: StrictStr = Field(..., alias="paymentStatus")
    player_status: StrictStr = Field(..., alias="playerStatus")
    refunded_amount: Union[StrictFloat, StrictInt] = Field(..., alias="refundedAmount")
    __properties = ["amountPaid", "eventFee", "isClubMember", "isRegistered", "isWaitListed", "paymentCapture", "paymentStatus", "playerStatus", "refundedAmount"]

    @validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING'):
            raise ValueError("must be one of enum values ('ACTIVE', 'CANCELLED', 'COMPLETE', 'CONFIRMED', 'DELETED', 'FORFEITED', 'INACTIVE', 'INVITED', 'IN_PROGRESS', 'MATCH_BYE', 'NOT_CONFIRMED', 'ONGOING', 'PENDING', 'SUSPENDED_TOS_13', 'UPCOMING')")
        return value

    @validator('player_status')
    def player_status_validate_enum(cls, value):
        """Validates the enum"""
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
    def from_json(cls, json_str: str) -> PaymentDetailsResponse:
        """Create an instance of PaymentDetailsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentDetailsResponse:
        """Create an instance of PaymentDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentDetailsResponse.parse_obj(obj)

        _obj = PaymentDetailsResponse.parse_obj({
            "amount_paid": obj.get("amountPaid"),
            "event_fee": obj.get("eventFee"),
            "is_club_member": obj.get("isClubMember"),
            "is_registered": obj.get("isRegistered"),
            "is_wait_listed": obj.get("isWaitListed"),
            "payment_capture": obj.get("paymentCapture"),
            "payment_status": obj.get("paymentStatus"),
            "player_status": obj.get("playerStatus"),
            "refunded_amount": obj.get("refundedAmount")
        })
        return _obj


