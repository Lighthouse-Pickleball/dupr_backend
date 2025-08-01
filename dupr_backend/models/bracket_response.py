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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from dupr_backend.models.address_response import AddressResponse
from dupr_backend.models.currency_details_response import CurrencyDetailsResponse
from dupr_backend.models.league_contact_detail_response import LeagueContactDetailResponse
from dupr_backend.models.league_content_response import LeagueContentResponse
from dupr_backend.models.payment_details_response import PaymentDetailsResponse
from dupr_backend.models.registration_response import RegistrationResponse
from typing import Optional, Set
from typing_extensions import Self

class BracketResponse(BaseModel):
    """
    BracketResponse
    """ # noqa: E501
    bracket_id: StrictInt = Field(alias="bracketId")
    league_id: StrictInt = Field(alias="leagueId")
    name: Optional[StrictStr] = None
    custom_code: Optional[StrictStr] = Field(default=None, alias="customCode")
    duration: List[StrictStr]
    format: Optional[StrictStr] = None
    elimination: Optional[StrictStr] = None
    player_group: Optional[StrictStr] = Field(default=None, alias="playerGroup")
    rating_bracket: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="ratingBracket")
    age_bracket: Optional[List[StrictInt]] = Field(default=None, alias="ageBracket")
    description: Optional[LeagueContentResponse] = None
    match_bonus_points: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="matchBonusPoints")
    registration_date: Optional[List[StrictStr]] = Field(default=None, alias="registrationDate")
    score_format: StrictStr = Field(alias="scoreFormat")
    member_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="memberFee")
    non_member_fee: Union[StrictFloat, StrictInt] = Field(alias="nonMemberFee")
    max_team: Optional[StrictInt] = Field(default=None, alias="maxTeam")
    wait_list: StrictInt = Field(alias="waitList")
    status: Optional[StrictStr] = None
    score_format_id: StrictInt = Field(alias="scoreFormatId")
    registration_status: Optional[StrictStr] = Field(default=None, alias="registrationStatus")
    duration_status: Optional[StrictStr] = Field(default=None, alias="durationStatus")
    registration_details: Optional[RegistrationResponse] = Field(default=None, alias="registrationDetails")
    league_name: StrictStr = Field(alias="leagueName")
    league_address: Optional[AddressResponse] = Field(default=None, alias="leagueAddress")
    media_url: Optional[StrictStr] = Field(default=None, alias="mediaUrl")
    total_rounds: Optional[StrictInt] = Field(default=None, alias="totalRounds")
    contact_details: Optional[List[LeagueContactDetailResponse]] = Field(default=None, alias="contactDetails")
    is_registered: StrictBool = Field(alias="isRegistered")
    club_name: StrictStr = Field(alias="clubName")
    registered_members: Optional[StrictInt] = Field(default=None, alias="registeredMembers")
    is_match_seeded: Optional[StrictBool] = Field(default=None, alias="isMatchSeeded")
    club_id: StrictInt = Field(alias="clubId")
    is_wait_list_full: StrictBool = Field(alias="isWaitListFull")
    display_status: Optional[StrictStr] = Field(default=None, alias="displayStatus")
    has_confirm_match: Optional[StrictBool] = Field(default=None, alias="hasConfirmMatch")
    has_queue: Optional[StrictBool] = Field(default=None, alias="hasQueue")
    is_queue_complete: Optional[StrictBool] = Field(default=None, alias="isQueueComplete")
    can_show_standings: Optional[StrictBool] = Field(default=None, alias="canShowStandings")
    courts: Optional[StrictInt] = None
    registration_date_time: Optional[List[StrictStr]] = Field(default=None, alias="registrationDateTime")
    duration_date_time: Optional[List[StrictStr]] = Field(default=None, alias="durationDateTime")
    time_zone: Optional[StrictStr] = Field(default=None, alias="timeZone")
    zone_name: Optional[StrictStr] = Field(default=None, alias="zoneName")
    is_player_eligible: Optional[StrictBool] = Field(default=None, alias="isPlayerEligible")
    draw_impacted: Optional[StrictBool] = Field(default=None, alias="drawImpacted")
    payment_details: Optional[PaymentDetailsResponse] = Field(default=None, alias="paymentDetails")
    reg_user_id: Optional[StrictInt] = Field(default=None, alias="regUserId")
    payment_status: StrictStr = Field(alias="paymentStatus")
    currency_details: Optional[CurrencyDetailsResponse] = Field(default=None, alias="currencyDetails")
    wait_list_full: Optional[StrictBool] = Field(default=None, alias="waitListFull")
    queue_complete: Optional[StrictBool] = Field(default=None, alias="queueComplete")
    player_eligible: Optional[StrictBool] = Field(default=None, alias="playerEligible")
    match_seeded: Optional[StrictBool] = Field(default=None, alias="matchSeeded")
    registered: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["bracketId", "leagueId", "name", "customCode", "duration", "format", "elimination", "playerGroup", "ratingBracket", "ageBracket", "description", "matchBonusPoints", "registrationDate", "scoreFormat", "memberFee", "nonMemberFee", "maxTeam", "waitList", "status", "scoreFormatId", "registrationStatus", "durationStatus", "registrationDetails", "leagueName", "leagueAddress", "mediaUrl", "totalRounds", "contactDetails", "isRegistered", "clubName", "registeredMembers", "isMatchSeeded", "clubId", "isWaitListFull", "displayStatus", "hasConfirmMatch", "hasQueue", "isQueueComplete", "canShowStandings", "courts", "registrationDateTime", "durationDateTime", "timeZone", "zoneName", "isPlayerEligible", "drawImpacted", "paymentDetails", "regUserId", "paymentStatus", "currencyDetails", "waitListFull", "queueComplete", "playerEligible", "matchSeeded", "registered"]

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SINGLES', 'DOUBLES']):
            raise ValueError("must be one of enum values ('SINGLES', 'DOUBLES')")
        return value

    @field_validator('elimination')
    def elimination_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SINGLE', 'DOUBLE', 'DOUBLE_PREVENTED', 'ROUND_ROBIN', 'COMPASS', 'FLEX']):
            raise ValueError("must be one of enum values ('SINGLE', 'DOUBLE', 'DOUBLE_PREVENTED', 'ROUND_ROBIN', 'COMPASS', 'FLEX')")
        return value

    @field_validator('player_group')
    def player_group_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MEN', 'WOMEN', 'MIXED', 'COED', 'OPEN']):
            raise ValueError("must be one of enum values ('MEN', 'WOMEN', 'MIXED', 'COED', 'OPEN')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'INACTIVE', 'UPCOMING', 'IN_PROGRESS', 'COMPLETE', 'CANCELLED', 'NOT_CONFIRMED', 'INVITED', 'CONFIRMED', 'MATCH_BYE', 'PENDING', 'FORFEITED', 'DELETED', 'ONGOING', 'SUSPENDED_TOS_13']):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE', 'UPCOMING', 'IN_PROGRESS', 'COMPLETE', 'CANCELLED', 'NOT_CONFIRMED', 'INVITED', 'CONFIRMED', 'MATCH_BYE', 'PENDING', 'FORFEITED', 'DELETED', 'ONGOING', 'SUSPENDED_TOS_13')")
        return value

    @field_validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACTIVE', 'INACTIVE', 'UPCOMING', 'IN_PROGRESS', 'COMPLETE', 'CANCELLED', 'NOT_CONFIRMED', 'INVITED', 'CONFIRMED', 'MATCH_BYE', 'PENDING', 'FORFEITED', 'DELETED', 'ONGOING', 'SUSPENDED_TOS_13']):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE', 'UPCOMING', 'IN_PROGRESS', 'COMPLETE', 'CANCELLED', 'NOT_CONFIRMED', 'INVITED', 'CONFIRMED', 'MATCH_BYE', 'PENDING', 'FORFEITED', 'DELETED', 'ONGOING', 'SUSPENDED_TOS_13')")
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
        """Create an instance of BracketResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of registration_details
        if self.registration_details:
            _dict['registrationDetails'] = self.registration_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of league_address
        if self.league_address:
            _dict['leagueAddress'] = self.league_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in contact_details (list)
        _items = []
        if self.contact_details:
            for _item_contact_details in self.contact_details:
                if _item_contact_details:
                    _items.append(_item_contact_details.to_dict())
            _dict['contactDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of payment_details
        if self.payment_details:
            _dict['paymentDetails'] = self.payment_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_details
        if self.currency_details:
            _dict['currencyDetails'] = self.currency_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BracketResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bracketId": obj.get("bracketId"),
            "leagueId": obj.get("leagueId"),
            "name": obj.get("name"),
            "customCode": obj.get("customCode"),
            "duration": obj.get("duration"),
            "format": obj.get("format"),
            "elimination": obj.get("elimination"),
            "playerGroup": obj.get("playerGroup"),
            "ratingBracket": obj.get("ratingBracket"),
            "ageBracket": obj.get("ageBracket"),
            "description": LeagueContentResponse.from_dict(obj["description"]) if obj.get("description") is not None else None,
            "matchBonusPoints": obj.get("matchBonusPoints"),
            "registrationDate": obj.get("registrationDate"),
            "scoreFormat": obj.get("scoreFormat"),
            "memberFee": obj.get("memberFee"),
            "nonMemberFee": obj.get("nonMemberFee"),
            "maxTeam": obj.get("maxTeam"),
            "waitList": obj.get("waitList"),
            "status": obj.get("status"),
            "scoreFormatId": obj.get("scoreFormatId"),
            "registrationStatus": obj.get("registrationStatus"),
            "durationStatus": obj.get("durationStatus"),
            "registrationDetails": RegistrationResponse.from_dict(obj["registrationDetails"]) if obj.get("registrationDetails") is not None else None,
            "leagueName": obj.get("leagueName"),
            "leagueAddress": AddressResponse.from_dict(obj["leagueAddress"]) if obj.get("leagueAddress") is not None else None,
            "mediaUrl": obj.get("mediaUrl"),
            "totalRounds": obj.get("totalRounds"),
            "contactDetails": [LeagueContactDetailResponse.from_dict(_item) for _item in obj["contactDetails"]] if obj.get("contactDetails") is not None else None,
            "isRegistered": obj.get("isRegistered"),
            "clubName": obj.get("clubName"),
            "registeredMembers": obj.get("registeredMembers"),
            "isMatchSeeded": obj.get("isMatchSeeded"),
            "clubId": obj.get("clubId"),
            "isWaitListFull": obj.get("isWaitListFull"),
            "displayStatus": obj.get("displayStatus"),
            "hasConfirmMatch": obj.get("hasConfirmMatch"),
            "hasQueue": obj.get("hasQueue"),
            "isQueueComplete": obj.get("isQueueComplete"),
            "canShowStandings": obj.get("canShowStandings"),
            "courts": obj.get("courts"),
            "registrationDateTime": obj.get("registrationDateTime"),
            "durationDateTime": obj.get("durationDateTime"),
            "timeZone": obj.get("timeZone"),
            "zoneName": obj.get("zoneName"),
            "isPlayerEligible": obj.get("isPlayerEligible"),
            "drawImpacted": obj.get("drawImpacted"),
            "paymentDetails": PaymentDetailsResponse.from_dict(obj["paymentDetails"]) if obj.get("paymentDetails") is not None else None,
            "regUserId": obj.get("regUserId"),
            "paymentStatus": obj.get("paymentStatus"),
            "currencyDetails": CurrencyDetailsResponse.from_dict(obj["currencyDetails"]) if obj.get("currencyDetails") is not None else None,
            "waitListFull": obj.get("waitListFull"),
            "queueComplete": obj.get("queueComplete"),
            "playerEligible": obj.get("playerEligible"),
            "matchSeeded": obj.get("matchSeeded"),
            "registered": obj.get("registered")
        })
        return _obj


