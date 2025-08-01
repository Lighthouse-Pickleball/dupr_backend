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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from dupr_backend.models.activity_user import ActivityUser
from dupr_backend.models.match import Match
from typing import Optional, Set
from typing_extensions import Self

class PostReactionResponse(BaseModel):
    """
    PostReactionResponse
    """ # noqa: E501
    id: StrictStr
    post_id: StrictStr = Field(alias="postId")
    actor: ActivityUser
    react: StrictStr
    comment: StrictStr
    created_at: StrictInt = Field(alias="createdAt")
    updated_at: StrictInt = Field(alias="updatedAt")
    getstream_id: StrictStr = Field(alias="getstreamId")
    activity_id: StrictStr = Field(alias="activityId")
    parent_id: StrictStr = Field(alias="parentId")
    reaction_counts: Dict[str, Union[StrictFloat, StrictInt]] = Field(alias="reactionCounts")
    tags: List[ActivityUser]
    images: List[StrictStr]
    matches: List[Match]
    __properties: ClassVar[List[str]] = ["id", "postId", "actor", "react", "comment", "createdAt", "updatedAt", "getstreamId", "activityId", "parentId", "reactionCounts", "tags", "images", "matches"]

    @field_validator('react')
    def react_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['LIKE', 'COMMENT']):
            raise ValueError("must be one of enum values ('LIKE', 'COMMENT')")
        return value

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
        """Create an instance of PostReactionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in matches (list)
        _items = []
        if self.matches:
            for _item_matches in self.matches:
                if _item_matches:
                    _items.append(_item_matches.to_dict())
            _dict['matches'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostReactionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "postId": obj.get("postId"),
            "actor": ActivityUser.from_dict(obj["actor"]) if obj.get("actor") is not None else None,
            "react": obj.get("react"),
            "comment": obj.get("comment"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "getstreamId": obj.get("getstreamId"),
            "activityId": obj.get("activityId"),
            "parentId": obj.get("parentId"),
            "reactionCounts": obj.get("reactionCounts"),
            "tags": [ActivityUser.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "images": obj.get("images"),
            "matches": [Match.from_dict(_item) for _item in obj["matches"]] if obj.get("matches") is not None else None
        })
        return _obj


