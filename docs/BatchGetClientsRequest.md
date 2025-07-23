# BatchGetClientsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from dupr_backend.models.batch_get_clients_request import BatchGetClientsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchGetClientsRequest from a JSON string
batch_get_clients_request_instance = BatchGetClientsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchGetClientsRequest.to_json())

# convert the object into a dict
batch_get_clients_request_dict = batch_get_clients_request_instance.to_dict()
# create an instance of BatchGetClientsRequest from a dict
batch_get_clients_request_from_dict = BatchGetClientsRequest.from_dict(batch_get_clients_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


