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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from dupr_backend.models.address import Address
from dupr_backend.models.club_type import ClubType
from dupr_backend.models.currency_details import CurrencyDetails
from dupr_backend.models.revenue_model import RevenueModel
from dupr_backend.models.text_content import TextContent
from typing import Optional, Set
from typing_extensions import Self

class Club(BaseModel):
    """
    Club
    """ # noqa: E501
    club_id: StrictInt = Field(alias="clubId")
    club_name: StrictStr = Field(alias="clubName")
    club_code: StrictStr = Field(alias="clubCode")
    club_type: Optional[ClubType] = Field(default=None, alias="clubType")
    media_url: Optional[StrictStr] = Field(default=None, alias="mediaUrl")
    manifest: Optional[TextContent] = None
    short_description: Optional[TextContent] = Field(default=None, alias="shortDescription")
    long_description: Optional[TextContent] = Field(default=None, alias="longDescription")
    approval_status: StrictStr = Field(alias="approvalStatus")
    status: StrictStr
    attributes: Optional[Dict[str, Any]] = None
    address: Optional[Address] = None
    short_address: Optional[StrictStr] = Field(default=None, alias="shortAddress")
    revenue_model: Optional[RevenueModel] = Field(default=None, alias="revenueModel")
    currency_details: Optional[CurrencyDetails] = Field(default=None, alias="currencyDetails")
    created: Optional[datetime] = None
    club_join_type: Optional[StrictStr] = Field(default=None, alias="clubJoinType")
    location: Optional[StrictStr] = None
    distance_in_miles: Union[StrictFloat, StrictInt] = Field(alias="distanceInMiles")
    __properties: ClassVar[List[str]] = ["clubId", "clubName", "clubCode", "clubType", "mediaUrl", "manifest", "shortDescription", "longDescription", "approvalStatus", "status", "attributes", "address", "shortAddress", "revenueModel", "currencyDetails", "created", "clubJoinType", "location", "distanceInMiles"]

    @field_validator('approval_status')
    def approval_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PENDING', 'IN_REVIEW', 'APPROVED', 'REJECTED']):
            raise ValueError("must be one of enum values ('PENDING', 'IN_REVIEW', 'APPROVED', 'REJECTED')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACTIVE', 'INACTIVE', 'UPCOMING', 'IN_PROGRESS', 'COMPLETE', 'CANCELLED', 'NOT_CONFIRMED', 'INVITED', 'CONFIRMED', 'MATCH_BYE', 'PENDING', 'FORFEITED', 'DELETED', 'ONGOING', 'SUSPENDED_TOS_13']):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE', 'UPCOMING', 'IN_PROGRESS', 'COMPLETE', 'CANCELLED', 'NOT_CONFIRMED', 'INVITED', 'CONFIRMED', 'MATCH_BYE', 'PENDING', 'FORFEITED', 'DELETED', 'ONGOING', 'SUSPENDED_TOS_13')")
        return value

    @field_validator('club_join_type')
    def club_join_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INVITATION', 'REQUEST', 'INVITATION_CSV', 'PARTNER_INVITE']):
            raise ValueError("must be one of enum values ('INVITATION', 'REQUEST', 'INVITATION_CSV', 'PARTNER_INVITE')")
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
        """Create an instance of Club from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of club_type
        if self.club_type:
            _dict['clubType'] = self.club_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manifest
        if self.manifest:
            _dict['manifest'] = self.manifest.to_dict()
        # override the default output from pydantic by calling `to_dict()` of short_description
        if self.short_description:
            _dict['shortDescription'] = self.short_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of long_description
        if self.long_description:
            _dict['longDescription'] = self.long_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of revenue_model
        if self.revenue_model:
            _dict['revenueModel'] = self.revenue_model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_details
        if self.currency_details:
            _dict['currencyDetails'] = self.currency_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Club from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clubId": obj.get("clubId"),
            "clubName": obj.get("clubName"),
            "clubCode": obj.get("clubCode"),
            "clubType": ClubType.from_dict(obj["clubType"]) if obj.get("clubType") is not None else None,
            "mediaUrl": obj.get("mediaUrl"),
            "manifest": TextContent.from_dict(obj["manifest"]) if obj.get("manifest") is not None else None,
            "shortDescription": TextContent.from_dict(obj["shortDescription"]) if obj.get("shortDescription") is not None else None,
            "longDescription": TextContent.from_dict(obj["longDescription"]) if obj.get("longDescription") is not None else None,
            "approvalStatus": obj.get("approvalStatus"),
            "status": obj.get("status"),
            "attributes": obj.get("attributes"),
            "address": Address.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "shortAddress": obj.get("shortAddress"),
            "revenueModel": RevenueModel.from_dict(obj["revenueModel"]) if obj.get("revenueModel") is not None else None,
            "currencyDetails": CurrencyDetails.from_dict(obj["currencyDetails"]) if obj.get("currencyDetails") is not None else None,
            "created": obj.get("created"),
            "clubJoinType": obj.get("clubJoinType"),
            "location": obj.get("location"),
            "distanceInMiles": obj.get("distanceInMiles")
        })
        return _obj


