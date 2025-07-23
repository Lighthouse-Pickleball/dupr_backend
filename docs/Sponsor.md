# Sponsor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**sponsor_redirect_url** | **str** |  | [optional] 
**sponsor_popup_heading** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**button_text** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.sponsor import Sponsor

# TODO update the JSON string below
json = "{}"
# create an instance of Sponsor from a JSON string
sponsor_instance = Sponsor.from_json(json)
# print the JSON string representation of the object
print(Sponsor.to_json())

# convert the object into a dict
sponsor_dict = sponsor_instance.to_dict()
# create an instance of Sponsor from a dict
sponsor_from_dict = Sponsor.from_dict(sponsor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


