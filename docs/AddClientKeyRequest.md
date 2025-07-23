# AddClientKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | 
**permissions** | [**List[Permission]**](Permission.md) | An optional list of permissions to assign to the new client key | 

## Example

```python
from dupr_backend.models.add_client_key_request import AddClientKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddClientKeyRequest from a JSON string
add_client_key_request_instance = AddClientKeyRequest.from_json(json)
# print the JSON string representation of the object
print(AddClientKeyRequest.to_json())

# convert the object into a dict
add_client_key_request_dict = add_client_key_request_instance.to_dict()
# create an instance of AddClientKeyRequest from a dict
add_client_key_request_from_dict = AddClientKeyRequest.from_dict(add_client_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


