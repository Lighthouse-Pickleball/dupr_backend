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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from dupr_backend.models.post_report import PostReport

class PageOfPostReport(BaseModel):
    """
    PageOfPostReport
    """
    empty: StrictBool = Field(..., description="Are results empty")
    has_more: StrictBool = Field(..., alias="hasMore", description="Are there any more results to fetch")
    has_previous: StrictBool = Field(..., alias="hasPrevious", description="Is there any previous page")
    hits: Optional[conlist(PostReport)] = Field(None, description="Array of results, can be empty.")
    limit: StrictInt = Field(..., description="Limit value you sent in the request")
    offset: StrictInt = Field(..., description="Offset value you sent in the request")
    total: StrictInt = Field(..., description="Total number of results available in database")
    total_value_relation: StrictStr = Field(..., alias="totalValueRelation", description="Relation to total results available.")
    __properties = ["empty", "hasMore", "hasPrevious", "hits", "limit", "offset", "total", "totalValueRelation"]

    @validator('total_value_relation')
    def total_value_relation_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('EQUAL_TO', 'GREATER_THAN_OR_EQUAL_TO'):
            raise ValueError("must be one of enum values ('EQUAL_TO', 'GREATER_THAN_OR_EQUAL_TO')")
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
    def from_json(cls, json_str: str) -> PageOfPostReport:
        """Create an instance of PageOfPostReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in hits (list)
        _items = []
        if self.hits:
            for _item in self.hits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PageOfPostReport:
        """Create an instance of PageOfPostReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PageOfPostReport.parse_obj(obj)

        _obj = PageOfPostReport.parse_obj({
            "empty": obj.get("empty"),
            "has_more": obj.get("hasMore"),
            "has_previous": obj.get("hasPrevious"),
            "hits": [PostReport.from_dict(_item) for _item in obj.get("hits")] if obj.get("hits") is not None else None,
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "total": obj.get("total"),
            "total_value_relation": obj.get("totalValueRelation")
        })
        return _obj


