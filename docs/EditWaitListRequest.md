# EditWaitListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**bracket_id** | **int** |  | 
**registration_id** | **int** |  | [optional] 
**club_id** | **int** |  | 
**is_wait_listed** | **bool** |  | 

## Example

```python
from dupr_backend.models.edit_wait_list_request import EditWaitListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditWaitListRequest from a JSON string
edit_wait_list_request_instance = EditWaitListRequest.from_json(json)
# print the JSON string representation of the object
print(EditWaitListRequest.to_json())

# convert the object into a dict
edit_wait_list_request_dict = edit_wait_list_request_instance.to_dict()
# create an instance of EditWaitListRequest from a dict
edit_wait_list_request_from_dict = EditWaitListRequest.from_dict(edit_wait_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


