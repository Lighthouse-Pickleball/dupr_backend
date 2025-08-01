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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from dupr_backend.models.member_ranking import MemberRanking
from dupr_backend.models.page_member_ranking import PageMemberRanking
from typing import Optional, Set
from typing_extensions import Self

class ClubMemberRankingResponse(BaseModel):
    """
    ClubMemberRankingResponse
    """ # noqa: E501
    my_ranking: Optional[MemberRanking] = Field(default=None, alias="myRanking")
    member_ranking: PageMemberRanking = Field(alias="memberRanking")
    __properties: ClassVar[List[str]] = ["myRanking", "memberRanking"]

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
        """Create an instance of ClubMemberRankingResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of my_ranking
        if self.my_ranking:
            _dict['myRanking'] = self.my_ranking.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member_ranking
        if self.member_ranking:
            _dict['memberRanking'] = self.member_ranking.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClubMemberRankingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "myRanking": MemberRanking.from_dict(obj["myRanking"]) if obj.get("myRanking") is not None else None,
            "memberRanking": PageMemberRanking.from_dict(obj["memberRanking"]) if obj.get("memberRanking") is not None else None
        })
        return _obj


