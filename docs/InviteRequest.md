# InviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**email** | **str** |  | 
**iso_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**identifier** | **str** | An unique identifier of this user from your platform | [optional] 

## Example

```python
from dupr_backend.models.invite_request import InviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InviteRequest from a JSON string
invite_request_instance = InviteRequest.from_json(json)
# print the JSON string representation of the object
print(InviteRequest.to_json())

# convert the object into a dict
invite_request_dict = invite_request_instance.to_dict()
# create an instance of InviteRequest from a dict
invite_request_from_dict = InviteRequest.from_dict(invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


