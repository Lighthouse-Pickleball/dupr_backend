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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dupr_backend.models.bracket_refund_request import BracketRefundRequest
from typing import Optional, Set
from typing_extensions import Self

class EventRefundRequest(BaseModel):
    """
    EventRefundRequest
    """ # noqa: E501
    brackets: Optional[List[BracketRefundRequest]] = None
    club_id: StrictInt = Field(alias="clubId")
    event_id: StrictInt = Field(alias="eventId")
    event_name: StrictStr = Field(alias="eventName")
    player_id: StrictInt = Field(alias="playerId")
    process_refund: StrictBool = Field(alias="processRefund")
    refund_amount: Union[StrictFloat, StrictInt] = Field(alias="refundAmount")
    __properties: ClassVar[List[str]] = ["brackets", "clubId", "eventId", "eventName", "playerId", "processRefund", "refundAmount"]

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
        """Create an instance of EventRefundRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in brackets (list)
        _items = []
        if self.brackets:
            for _item_brackets in self.brackets:
                if _item_brackets:
                    _items.append(_item_brackets.to_dict())
            _dict['brackets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventRefundRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "brackets": [BracketRefundRequest.from_dict(_item) for _item in obj["brackets"]] if obj.get("brackets") is not None else None,
            "clubId": obj.get("clubId"),
            "eventId": obj.get("eventId"),
            "eventName": obj.get("eventName"),
            "playerId": obj.get("playerId"),
            "processRefund": obj.get("processRefund"),
            "refundAmount": obj.get("refundAmount")
        })
        return _obj


