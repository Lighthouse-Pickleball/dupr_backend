# UserByDuprIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.user_by_dupr_id_response import UserByDuprIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserByDuprIdResponse from a JSON string
user_by_dupr_id_response_instance = UserByDuprIdResponse.from_json(json)
# print the JSON string representation of the object
print(UserByDuprIdResponse.to_json())

# convert the object into a dict
user_by_dupr_id_response_dict = user_by_dupr_id_response_instance.to_dict()
# create an instance of UserByDuprIdResponse from a dict
user_by_dupr_id_response_from_dict = UserByDuprIdResponse.from_dict(user_by_dupr_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


