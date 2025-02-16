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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist, validator
from dupr_backend.models.currency_details_response import CurrencyDetailsResponse

class ArrayWrapperOfCurrencyDetailsResponse(BaseModel):
    """
    ArrayWrapperOfCurrencyDetailsResponse
    """
    message: Optional[StrictStr] = None
    results: Optional[conlist(CurrencyDetailsResponse)] = None
    status: Optional[StrictStr] = None
    __properties = ["message", "results", "status"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('FAILURE', 'REDIRECT', 'SUCCESS'):
            raise ValueError("must be one of enum values ('FAILURE', 'REDIRECT', 'SUCCESS')")
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
    def from_json(cls, json_str: str) -> ArrayWrapperOfCurrencyDetailsResponse:
        """Create an instance of ArrayWrapperOfCurrencyDetailsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ArrayWrapperOfCurrencyDetailsResponse:
        """Create an instance of ArrayWrapperOfCurrencyDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ArrayWrapperOfCurrencyDetailsResponse.parse_obj(obj)

        _obj = ArrayWrapperOfCurrencyDetailsResponse.parse_obj({
            "message": obj.get("message"),
            "results": [CurrencyDetailsResponse.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None,
            "status": obj.get("status")
        })
        return _obj


