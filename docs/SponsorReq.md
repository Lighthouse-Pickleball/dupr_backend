# SponsorReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_text** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**sponsor_popup_heading** | **str** |  | [optional] 
**sponsor_redirect_url** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.sponsor_req import SponsorReq

# TODO update the JSON string below
json = "{}"
# create an instance of SponsorReq from a JSON string
sponsor_req_instance = SponsorReq.from_json(json)
# print the JSON string representation of the object
print(SponsorReq.to_json())

# convert the object into a dict
sponsor_req_dict = sponsor_req_instance.to_dict()
# create an instance of SponsorReq from a dict
sponsor_req_from_dict = SponsorReq.from_dict(sponsor_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


