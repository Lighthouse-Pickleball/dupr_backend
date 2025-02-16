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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from dupr_backend.models.autocomplete_structured_formatting import AutocompleteStructuredFormatting
from dupr_backend.models.matched_substring import MatchedSubstring
from dupr_backend.models.term import Term

class AutocompletePrediction(BaseModel):
    """
    AutocompletePrediction
    """
    description: Optional[StrictStr] = None
    distance_meters: Optional[StrictInt] = Field(None, alias="distanceMeters")
    matched_substrings: Optional[conlist(MatchedSubstring)] = Field(None, alias="matchedSubstrings")
    place_id: Optional[StrictStr] = Field(None, alias="placeId")
    structured_formatting: Optional[AutocompleteStructuredFormatting] = Field(None, alias="structuredFormatting")
    terms: Optional[conlist(Term)] = None
    types: Optional[conlist(StrictStr)] = None
    __properties = ["description", "distanceMeters", "matchedSubstrings", "placeId", "structuredFormatting", "terms", "types"]

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
    def from_json(cls, json_str: str) -> AutocompletePrediction:
        """Create an instance of AutocompletePrediction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in matched_substrings (list)
        _items = []
        if self.matched_substrings:
            for _item in self.matched_substrings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchedSubstrings'] = _items
        # override the default output from pydantic by calling `to_dict()` of structured_formatting
        if self.structured_formatting:
            _dict['structuredFormatting'] = self.structured_formatting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in terms (list)
        _items = []
        if self.terms:
            for _item in self.terms:
                if _item:
                    _items.append(_item.to_dict())
            _dict['terms'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AutocompletePrediction:
        """Create an instance of AutocompletePrediction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AutocompletePrediction.parse_obj(obj)

        _obj = AutocompletePrediction.parse_obj({
            "description": obj.get("description"),
            "distance_meters": obj.get("distanceMeters"),
            "matched_substrings": [MatchedSubstring.from_dict(_item) for _item in obj.get("matchedSubstrings")] if obj.get("matchedSubstrings") is not None else None,
            "place_id": obj.get("placeId"),
            "structured_formatting": AutocompleteStructuredFormatting.from_dict(obj.get("structuredFormatting")) if obj.get("structuredFormatting") is not None else None,
            "terms": [Term.from_dict(_item) for _item in obj.get("terms")] if obj.get("terms") is not None else None,
            "types": obj.get("types")
        })
        return _obj


