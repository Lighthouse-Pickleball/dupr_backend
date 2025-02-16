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



from pydantic import BaseModel, Field, StrictStr

class DownloadS3Response(BaseModel):
    """
    DownloadS3Response
    """
    s3_url: StrictStr = Field(..., alias="s3Url")
    __properties = ["s3Url"]

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
    def from_json(cls, json_str: str) -> DownloadS3Response:
        """Create an instance of DownloadS3Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DownloadS3Response:
        """Create an instance of DownloadS3Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DownloadS3Response.parse_obj(obj)

        _obj = DownloadS3Response.parse_obj({
            "s3_url": obj.get("s3Url")
        })
        return _obj


