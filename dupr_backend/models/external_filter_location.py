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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, confloat, conint

class ExternalFilterLocation(BaseModel):
    """
    ExternalFilterLocation
    """
    address: StrictStr = Field(..., description="Street level address in format county / city, state / region, country")
    lat: Union[confloat(le=9E+1, ge=-9E+1, strict=True), conint(le=90, ge=-90, strict=True)] = Field(..., description="Earth's latitude value")
    lng: Union[confloat(le=1.8E+2, ge=-1.8E+2, strict=True), conint(le=180, ge=-180, strict=True)] = Field(..., description="Earth's longitude value")
    radius_in_meters: Union[StrictFloat, StrictInt] = Field(..., alias="radiusInMeters", description="Radius distance in meters from the point of provided latitude and longitude, default is 40233.6 meters (25 miles)")
    __properties = ["address", "lat", "lng", "radiusInMeters"]

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
    def from_json(cls, json_str: str) -> ExternalFilterLocation:
        """Create an instance of ExternalFilterLocation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalFilterLocation:
        """Create an instance of ExternalFilterLocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExternalFilterLocation.parse_obj(obj)

        _obj = ExternalFilterLocation.parse_obj({
            "address": obj.get("address"),
            "lat": obj.get("lat"),
            "lng": obj.get("lng"),
            "radius_in_meters": obj.get("radiusInMeters")
        })
        return _obj


