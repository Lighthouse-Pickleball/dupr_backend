# CreateClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | 
**client_key** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.create_client_response import CreateClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientResponse from a JSON string
create_client_response_instance = CreateClientResponse.from_json(json)
# print the JSON string representation of the object
print(CreateClientResponse.to_json())

# convert the object into a dict
create_client_response_dict = create_client_response_instance.to_dict()
# create an instance of CreateClientResponse from a dict
create_client_response_from_dict = CreateClientResponse.from_dict(create_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


