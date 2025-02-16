# DeleteMatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_id** | **str** |  | 
**match_id_type** | **str** |  | 
**notify** | **bool** |  | [optional] 
**reason** | **str** |  | [optional] 
**requested_by_dupr_id** | **str** |  | 

## Example

```python
from dupr_backend.models.delete_match_request import DeleteMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMatchRequest from a JSON string
delete_match_request_instance = DeleteMatchRequest.from_json(json)
# print the JSON string representation of the object
print DeleteMatchRequest.to_json()

# convert the object into a dict
delete_match_request_dict = delete_match_request_instance.to_dict()
# create an instance of DeleteMatchRequest from a dict
delete_match_request_form_dict = delete_match_request.from_dict(delete_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


