# RegisteredEventAdminRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_ids** | **Dict[str, str]** |  | [optional] 
**emails** | **Dict[str, str]** |  | [optional] 
**user_ids** | **Dict[str, int]** |  | [optional] 

## Example

```python
from dupr_backend.models.registered_event_admin_request import RegisteredEventAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredEventAdminRequest from a JSON string
registered_event_admin_request_instance = RegisteredEventAdminRequest.from_json(json)
# print the JSON string representation of the object
print RegisteredEventAdminRequest.to_json()

# convert the object into a dict
registered_event_admin_request_dict = registered_event_admin_request_instance.to_dict()
# create an instance of RegisteredEventAdminRequest from a dict
registered_event_admin_request_form_dict = registered_event_admin_request.from_dict(registered_event_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


