# ContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_id** | **int** |  | 
**header** | **str** |  | [optional] 
**header_type** | **str** |  | [optional] 
**content** | **str** |  | 
**content_type** | **str** |  | 
**footer** | **str** |  | [optional] 
**footer_type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.content_response import ContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentResponse from a JSON string
content_response_instance = ContentResponse.from_json(json)
# print the JSON string representation of the object
print(ContentResponse.to_json())

# convert the object into a dict
content_response_dict = content_response_instance.to_dict()
# create an instance of ContentResponse from a dict
content_response_from_dict = ContentResponse.from_dict(content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


