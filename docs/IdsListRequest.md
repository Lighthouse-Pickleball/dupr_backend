# IdsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | 

## Example

```python
from dupr_backend.models.ids_list_request import IdsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdsListRequest from a JSON string
ids_list_request_instance = IdsListRequest.from_json(json)
# print the JSON string representation of the object
print(IdsListRequest.to_json())

# convert the object into a dict
ids_list_request_dict = ids_list_request_instance.to_dict()
# create an instance of IdsListRequest from a dict
ids_list_request_from_dict = IdsListRequest.from_dict(ids_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


