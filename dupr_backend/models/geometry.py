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
from pydantic import BaseModel, Field, StrictStr, validator
from dupr_backend.models.bounds import Bounds
from dupr_backend.models.lat_lng import LatLng

class Geometry(BaseModel):
    """
    Geometry
    """
    bounds: Optional[Bounds] = None
    location: Optional[LatLng] = None
    location_type: Optional[StrictStr] = Field(None, alias="locationType")
    viewport: Optional[Bounds] = None
    __properties = ["bounds", "location", "locationType", "viewport"]

    @validator('location_type')
    def location_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('APPROXIMATE', 'GEOMETRIC_CENTER', 'RANGE_INTERPOLATED', 'ROOFTOP', 'UNKNOWN'):
            raise ValueError("must be one of enum values ('APPROXIMATE', 'GEOMETRIC_CENTER', 'RANGE_INTERPOLATED', 'ROOFTOP', 'UNKNOWN')")
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
    def from_json(cls, json_str: str) -> Geometry:
        """Create an instance of Geometry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bounds
        if self.bounds:
            _dict['bounds'] = self.bounds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of viewport
        if self.viewport:
            _dict['viewport'] = self.viewport.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Geometry:
        """Create an instance of Geometry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Geometry.parse_obj(obj)

        _obj = Geometry.parse_obj({
            "bounds": Bounds.from_dict(obj.get("bounds")) if obj.get("bounds") is not None else None,
            "location": LatLng.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "location_type": obj.get("locationType"),
            "viewport": Bounds.from_dict(obj.get("viewport")) if obj.get("viewport") is not None else None
        })
        return _obj


