# PostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | **int** |  | [optional] 
**checkin** | [**CheckInLocation**](CheckInLocation.md) |  | [optional] 
**content** | **str** |  | [optional] 
**feed** | [**Feed**](Feed.md) |  | [optional] 
**hashtags** | **List[str]** |  | [optional] 
**images** | **List[str]** |  | [optional] 
**matches** | **List[int]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**verb** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.post_request import PostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRequest from a JSON string
post_request_instance = PostRequest.from_json(json)
# print the JSON string representation of the object
print PostRequest.to_json()

# convert the object into a dict
post_request_dict = post_request_instance.to_dict()
# create an instance of PostRequest from a dict
post_request_form_dict = post_request.from_dict(post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


