# ContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** |  | 
**header_type** | **str** |  | 
**content** | **str** |  | 
**content_type** | **str** |  | 
**footer** | **str** |  | 
**footer_type** | **str** |  | 
**content_id** | **int** |  | 

## Example

```python
from dupr_backend.models.content_request import ContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentRequest from a JSON string
content_request_instance = ContentRequest.from_json(json)
# print the JSON string representation of the object
print(ContentRequest.to_json())

# convert the object into a dict
content_request_dict = content_request_instance.to_dict()
# create an instance of ContentRequest from a dict
content_request_from_dict = ContentRequest.from_dict(content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


