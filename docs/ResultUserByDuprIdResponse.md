# ResultUserByDuprIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**results** | [**List[UserByDuprIdResponse]**](UserByDuprIdResponse.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from dupr_backend.models.result_user_by_dupr_id_response import ResultUserByDuprIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResultUserByDuprIdResponse from a JSON string
result_user_by_dupr_id_response_instance = ResultUserByDuprIdResponse.from_json(json)
# print the JSON string representation of the object
print(ResultUserByDuprIdResponse.to_json())

# convert the object into a dict
result_user_by_dupr_id_response_dict = result_user_by_dupr_id_response_instance.to_dict()
# create an instance of ResultUserByDuprIdResponse from a dict
result_user_by_dupr_id_response_from_dict = ResultUserByDuprIdResponse.from_dict(result_user_by_dupr_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


