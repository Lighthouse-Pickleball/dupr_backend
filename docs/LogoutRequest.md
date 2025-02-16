# LogoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | 
**uuid** | **str** |  | 

## Example

```python
from dupr_backend.models.logout_request import LogoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutRequest from a JSON string
logout_request_instance = LogoutRequest.from_json(json)
# print the JSON string representation of the object
print(LogoutRequest.to_json())

# convert the object into a dict
logout_request_dict = logout_request_instance.to_dict()
# create an instance of LogoutRequest from a dict
logout_request_from_dict = LogoutRequest.from_dict(logout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


