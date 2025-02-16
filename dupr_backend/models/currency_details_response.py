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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class CurrencyDetailsResponse(BaseModel):
    """
    CurrencyDetailsResponse
    """
    currency_code: StrictStr = Field(..., alias="currencyCode")
    currency_name: StrictStr = Field(..., alias="currencyName")
    currency_symbol: StrictStr = Field(..., alias="currencySymbol")
    min_limit: Union[StrictFloat, StrictInt] = Field(..., alias="minLimit")
    __properties = ["currencyCode", "currencyName", "currencySymbol", "minLimit"]

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
    def from_json(cls, json_str: str) -> CurrencyDetailsResponse:
        """Create an instance of CurrencyDetailsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CurrencyDetailsResponse:
        """Create an instance of CurrencyDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurrencyDetailsResponse.parse_obj(obj)

        _obj = CurrencyDetailsResponse.parse_obj({
            "currency_code": obj.get("currencyCode"),
            "currency_name": obj.get("currencyName"),
            "currency_symbol": obj.get("currencySymbol"),
            "min_limit": obj.get("minLimit")
        })
        return _obj


