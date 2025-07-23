# UserByDuprIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_id** | **str** |  | 

## Example

```python
from dupr_backend.models.user_by_dupr_id_request import UserByDuprIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserByDuprIdRequest from a JSON string
user_by_dupr_id_request_instance = UserByDuprIdRequest.from_json(json)
# print the JSON string representation of the object
print(UserByDuprIdRequest.to_json())

# convert the object into a dict
user_by_dupr_id_request_dict = user_by_dupr_id_request_instance.to_dict()
# create an instance of UserByDuprIdRequest from a dict
user_by_dupr_id_request_from_dict = UserByDuprIdRequest.from_dict(user_by_dupr_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


