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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class OpenPlayEventWaitlist(BaseModel):
    """
    OpenPlayEventWaitlist
    """
    event_id: StrictInt = Field(..., alias="eventId")
    message: Optional[StrictStr] = None
    waitlist_position: StrictInt = Field(..., alias="waitlistPosition")
    __properties = ["eventId", "message", "waitlistPosition"]

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
    def from_json(cls, json_str: str) -> OpenPlayEventWaitlist:
        """Create an instance of OpenPlayEventWaitlist from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OpenPlayEventWaitlist:
        """Create an instance of OpenPlayEventWaitlist from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OpenPlayEventWaitlist.parse_obj(obj)

        _obj = OpenPlayEventWaitlist.parse_obj({
            "event_id": obj.get("eventId"),
            "message": obj.get("message"),
            "waitlist_position": obj.get("waitlistPosition")
        })
        return _obj


