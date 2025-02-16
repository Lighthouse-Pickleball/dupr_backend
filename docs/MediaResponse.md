# MediaResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from dupr_backend.models.media_response import MediaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MediaResponse from a JSON string
media_response_instance = MediaResponse.from_json(json)
# print the JSON string representation of the object
print MediaResponse.to_json()

# convert the object into a dict
media_response_dict = media_response_instance.to_dict()
# create an instance of MediaResponse from a dict
media_response_form_dict = media_response.from_dict(media_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


