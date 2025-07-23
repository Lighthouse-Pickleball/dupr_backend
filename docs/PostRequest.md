# PostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | **int** |  | 
**feed** | [**Feed**](Feed.md) |  | 
**verb** | **str** |  | 
**content** | **str** |  | 
**tags** | **List[int]** |  | 
**hashtags** | **List[str]** |  | 
**images** | **List[str]** |  | 
**matches** | **List[int]** |  | 
**checkin** | [**CheckInLocation**](CheckInLocation.md) |  | 

## Example

```python
from dupr_backend.models.post_request import PostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRequest from a JSON string
post_request_instance = PostRequest.from_json(json)
# print the JSON string representation of the object
print(PostRequest.to_json())

# convert the object into a dict
post_request_dict = post_request_instance.to_dict()
# create an instance of PostRequest from a dict
post_request_from_dict = PostRequest.from_dict(post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


