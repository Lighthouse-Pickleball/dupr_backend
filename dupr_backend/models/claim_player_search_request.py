# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dupr_backend.models.claim_player_search_filter import ClaimPlayerSearchFilter
from dupr_backend.models.claim_player_search_sort import ClaimPlayerSearchSort
from typing import Optional, Set
from typing_extensions import Self

class ClaimPlayerSearchRequest(BaseModel):
    """
    ClaimPlayerSearchRequest
    """ # noqa: E501
    offset: StrictInt
    limit: Annotated[int, Field(le=25, strict=True)]
    query: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    filter: Optional[ClaimPlayerSearchFilter] = None
    sort: Optional[ClaimPlayerSearchSort] = None
    __properties: ClassVar[List[str]] = ["offset", "limit", "query", "filter", "sort"]

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
        """Create an instance of ClaimPlayerSearchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sort
        if self.sort:
            _dict['sort'] = self.sort.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClaimPlayerSearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offset": obj.get("offset"),
            "limit": obj.get("limit"),
            "query": obj.get("query"),
            "filter": ClaimPlayerSearchFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "sort": ClaimPlayerSearchSort.from_dict(obj["sort"]) if obj.get("sort") is not None else None
        })
        return _obj


