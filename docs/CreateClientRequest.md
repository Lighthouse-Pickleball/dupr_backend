# CreateClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**permissions** | [**List[Permission]**](Permission.md) | An optional list of permissions to assign to the client key | 

## Example

```python
from dupr_backend.models.create_client_request import CreateClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientRequest from a JSON string
create_client_request_instance = CreateClientRequest.from_json(json)
# print the JSON string representation of the object
print(CreateClientRequest.to_json())

# convert the object into a dict
create_client_request_dict = create_client_request_instance.to_dict()
# create an instance of CreateClientRequest from a dict
create_client_request_from_dict = CreateClientRequest.from_dict(create_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


