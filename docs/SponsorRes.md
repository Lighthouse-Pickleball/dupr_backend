# SponsorRes


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
from dupr_backend.models.sponsor_res import SponsorRes

# TODO update the JSON string below
json = "{}"
# create an instance of SponsorRes from a JSON string
sponsor_res_instance = SponsorRes.from_json(json)
# print the JSON string representation of the object
print(SponsorRes.to_json())

# convert the object into a dict
sponsor_res_dict = sponsor_res_instance.to_dict()
# create an instance of SponsorRes from a dict
sponsor_res_from_dict = SponsorRes.from_dict(sponsor_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


