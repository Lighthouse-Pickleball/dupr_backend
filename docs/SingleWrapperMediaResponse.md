# SingleWrapperMediaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**MediaResponse**](MediaResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_media_response import SingleWrapperMediaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperMediaResponse from a JSON string
single_wrapper_media_response_instance = SingleWrapperMediaResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperMediaResponse.to_json())

# convert the object into a dict
single_wrapper_media_response_dict = single_wrapper_media_response_instance.to_dict()
# create an instance of SingleWrapperMediaResponse from a dict
single_wrapper_media_response_from_dict = SingleWrapperMediaResponse.from_dict(single_wrapper_media_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


