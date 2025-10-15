# SetDuprIdsInactiveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_ids** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.set_dupr_ids_inactive_request import SetDuprIdsInactiveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDuprIdsInactiveRequest from a JSON string
set_dupr_ids_inactive_request_instance = SetDuprIdsInactiveRequest.from_json(json)
# print the JSON string representation of the object
print(SetDuprIdsInactiveRequest.to_json())

# convert the object into a dict
set_dupr_ids_inactive_request_dict = set_dupr_ids_inactive_request_instance.to_dict()
# create an instance of SetDuprIdsInactiveRequest from a dict
set_dupr_ids_inactive_request_from_dict = SetDuprIdsInactiveRequest.from_dict(set_dupr_ids_inactive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


