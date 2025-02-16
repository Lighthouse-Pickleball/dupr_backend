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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from dupr_backend.models.address_component import AddressComponent
from dupr_backend.models.geometry import Geometry
from dupr_backend.models.plus_code import PlusCode

class GeocodingResult(BaseModel):
    """
    GeocodingResult
    """
    address_components: Optional[conlist(AddressComponent)] = Field(None, alias="addressComponents")
    formatted_address: Optional[StrictStr] = Field(None, alias="formattedAddress")
    geometry: Optional[Geometry] = None
    partial_match: Optional[StrictBool] = Field(None, alias="partialMatch")
    place_id: Optional[StrictStr] = Field(None, alias="placeId")
    plus_code: Optional[PlusCode] = Field(None, alias="plusCode")
    postcode_localities: Optional[conlist(StrictStr)] = Field(None, alias="postcodeLocalities")
    types: Optional[conlist(StrictStr)] = None
    __properties = ["addressComponents", "formattedAddress", "geometry", "partialMatch", "placeId", "plusCode", "postcodeLocalities", "types"]

    @validator('types')
    def types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('ACCOUNTING', 'ADMINISTRATIVE_AREA_LEVEL_1', 'ADMINISTRATIVE_AREA_LEVEL_2', 'ADMINISTRATIVE_AREA_LEVEL_3', 'ADMINISTRATIVE_AREA_LEVEL_4', 'ADMINISTRATIVE_AREA_LEVEL_5', 'AIRPORT', 'AMUSEMENT_PARK', 'AQUARIUM', 'ARCHIPELAGO', 'ART_GALLERY', 'ATM', 'BAKERY', 'BANK', 'BAR', 'BEAUTY_SALON', 'BICYCLE_STORE', 'BOOK_STORE', 'BOWLING_ALLEY', 'BUS_STATION', 'CAFE', 'CAMPGROUND', 'CAR_DEALER', 'CAR_RENTAL', 'CAR_REPAIR', 'CAR_WASH', 'CASINO', 'CEMETERY', 'CHURCH', 'CITY_HALL', 'CLOTHING_STORE', 'COLLOQUIAL_AREA', 'CONTINENT', 'CONVENIENCE_STORE', 'COUNTRY', 'COURTHOUSE', 'DENTIST', 'DEPARTMENT_STORE', 'DOCTOR', 'DRUGSTORE', 'ELECTRICIAN', 'ELECTRONICS_STORE', 'EMBASSY', 'ESTABLISHMENT', 'FINANCE', 'FIRE_STATION', 'FLOOR', 'FLORIST', 'FOOD', 'FUNERAL_HOME', 'FURNITURE_STORE', 'GAS_STATION', 'GENERAL_CONTRACTOR', 'GROCERY_OR_SUPERMARKET', 'GYM', 'HAIR_CARE', 'HARDWARE_STORE', 'HEALTH', 'HINDU_TEMPLE', 'HOME_GOODS_STORE', 'HOSPITAL', 'INSURANCE_AGENCY', 'INTERSECTION', 'JEWELRY_STORE', 'LAUNDRY', 'LAWYER', 'LIBRARY', 'LIGHT_RAIL_STATION', 'LIQUOR_STORE', 'LOCALITY', 'LOCAL_GOVERNMENT_OFFICE', 'LOCKSMITH', 'LODGING', 'MEAL_DELIVERY', 'MEAL_TAKEAWAY', 'MOSQUE', 'MOVIE_RENTAL', 'MOVIE_THEATER', 'MOVING_COMPANY', 'MUSEUM', 'NATURAL_FEATURE', 'NEIGHBORHOOD', 'NIGHT_CLUB', 'PAINTER', 'PARK', 'PARKING', 'PET_STORE', 'PHARMACY', 'PHYSIOTHERAPIST', 'PLACE_OF_WORSHIP', 'PLUMBER', 'PLUS_CODE', 'POINT_OF_INTEREST', 'POLICE', 'POLITICAL', 'POSTAL_CODE', 'POSTAL_CODE_PREFIX', 'POSTAL_CODE_SUFFIX', 'POSTAL_TOWN', 'POST_BOX', 'POST_OFFICE', 'PREMISE', 'PRIMARY_SCHOOL', 'REAL_ESTATE_AGENCY', 'RESTAURANT', 'ROOFING_CONTRACTOR', 'ROOM', 'ROUTE', 'RV_PARK', 'SCHOOL', 'SECONDARY_SCHOOL', 'SHOE_STORE', 'SHOPPING_MALL', 'SPA', 'STADIUM', 'STORAGE', 'STORE', 'STREET_ADDRESS', 'STREET_NUMBER', 'SUBLOCALITY', 'SUBLOCALITY_LEVEL_1', 'SUBLOCALITY_LEVEL_2', 'SUBLOCALITY_LEVEL_3', 'SUBLOCALITY_LEVEL_4', 'SUBLOCALITY_LEVEL_5', 'SUBPREMISE', 'SUBWAY_STATION', 'SUPERMARKET', 'SYNAGOGUE', 'TAXI_STAND', 'TOURIST_ATTRACTION', 'TOWN_SQUARE', 'TRAIN_STATION', 'TRANSIT_STATION', 'TRAVEL_AGENCY', 'UNIVERSITY', 'UNKNOWN', 'VETERINARY_CARE', 'WARD', 'ZOO'):
                raise ValueError("each list item must be one of ('ACCOUNTING', 'ADMINISTRATIVE_AREA_LEVEL_1', 'ADMINISTRATIVE_AREA_LEVEL_2', 'ADMINISTRATIVE_AREA_LEVEL_3', 'ADMINISTRATIVE_AREA_LEVEL_4', 'ADMINISTRATIVE_AREA_LEVEL_5', 'AIRPORT', 'AMUSEMENT_PARK', 'AQUARIUM', 'ARCHIPELAGO', 'ART_GALLERY', 'ATM', 'BAKERY', 'BANK', 'BAR', 'BEAUTY_SALON', 'BICYCLE_STORE', 'BOOK_STORE', 'BOWLING_ALLEY', 'BUS_STATION', 'CAFE', 'CAMPGROUND', 'CAR_DEALER', 'CAR_RENTAL', 'CAR_REPAIR', 'CAR_WASH', 'CASINO', 'CEMETERY', 'CHURCH', 'CITY_HALL', 'CLOTHING_STORE', 'COLLOQUIAL_AREA', 'CONTINENT', 'CONVENIENCE_STORE', 'COUNTRY', 'COURTHOUSE', 'DENTIST', 'DEPARTMENT_STORE', 'DOCTOR', 'DRUGSTORE', 'ELECTRICIAN', 'ELECTRONICS_STORE', 'EMBASSY', 'ESTABLISHMENT', 'FINANCE', 'FIRE_STATION', 'FLOOR', 'FLORIST', 'FOOD', 'FUNERAL_HOME', 'FURNITURE_STORE', 'GAS_STATION', 'GENERAL_CONTRACTOR', 'GROCERY_OR_SUPERMARKET', 'GYM', 'HAIR_CARE', 'HARDWARE_STORE', 'HEALTH', 'HINDU_TEMPLE', 'HOME_GOODS_STORE', 'HOSPITAL', 'INSURANCE_AGENCY', 'INTERSECTION', 'JEWELRY_STORE', 'LAUNDRY', 'LAWYER', 'LIBRARY', 'LIGHT_RAIL_STATION', 'LIQUOR_STORE', 'LOCALITY', 'LOCAL_GOVERNMENT_OFFICE', 'LOCKSMITH', 'LODGING', 'MEAL_DELIVERY', 'MEAL_TAKEAWAY', 'MOSQUE', 'MOVIE_RENTAL', 'MOVIE_THEATER', 'MOVING_COMPANY', 'MUSEUM', 'NATURAL_FEATURE', 'NEIGHBORHOOD', 'NIGHT_CLUB', 'PAINTER', 'PARK', 'PARKING', 'PET_STORE', 'PHARMACY', 'PHYSIOTHERAPIST', 'PLACE_OF_WORSHIP', 'PLUMBER', 'PLUS_CODE', 'POINT_OF_INTEREST', 'POLICE', 'POLITICAL', 'POSTAL_CODE', 'POSTAL_CODE_PREFIX', 'POSTAL_CODE_SUFFIX', 'POSTAL_TOWN', 'POST_BOX', 'POST_OFFICE', 'PREMISE', 'PRIMARY_SCHOOL', 'REAL_ESTATE_AGENCY', 'RESTAURANT', 'ROOFING_CONTRACTOR', 'ROOM', 'ROUTE', 'RV_PARK', 'SCHOOL', 'SECONDARY_SCHOOL', 'SHOE_STORE', 'SHOPPING_MALL', 'SPA', 'STADIUM', 'STORAGE', 'STORE', 'STREET_ADDRESS', 'STREET_NUMBER', 'SUBLOCALITY', 'SUBLOCALITY_LEVEL_1', 'SUBLOCALITY_LEVEL_2', 'SUBLOCALITY_LEVEL_3', 'SUBLOCALITY_LEVEL_4', 'SUBLOCALITY_LEVEL_5', 'SUBPREMISE', 'SUBWAY_STATION', 'SUPERMARKET', 'SYNAGOGUE', 'TAXI_STAND', 'TOURIST_ATTRACTION', 'TOWN_SQUARE', 'TRAIN_STATION', 'TRANSIT_STATION', 'TRAVEL_AGENCY', 'UNIVERSITY', 'UNKNOWN', 'VETERINARY_CARE', 'WARD', 'ZOO')")
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
    def from_json(cls, json_str: str) -> GeocodingResult:
        """Create an instance of GeocodingResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in address_components (list)
        _items = []
        if self.address_components:
            for _item in self.address_components:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addressComponents'] = _items
        # override the default output from pydantic by calling `to_dict()` of geometry
        if self.geometry:
            _dict['geometry'] = self.geometry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plus_code
        if self.plus_code:
            _dict['plusCode'] = self.plus_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeocodingResult:
        """Create an instance of GeocodingResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GeocodingResult.parse_obj(obj)

        _obj = GeocodingResult.parse_obj({
            "address_components": [AddressComponent.from_dict(_item) for _item in obj.get("addressComponents")] if obj.get("addressComponents") is not None else None,
            "formatted_address": obj.get("formattedAddress"),
            "geometry": Geometry.from_dict(obj.get("geometry")) if obj.get("geometry") is not None else None,
            "partial_match": obj.get("partialMatch"),
            "place_id": obj.get("placeId"),
            "plus_code": PlusCode.from_dict(obj.get("plusCode")) if obj.get("plusCode") is not None else None,
            "postcode_localities": obj.get("postcodeLocalities"),
            "types": obj.get("types")
        })
        return _obj


