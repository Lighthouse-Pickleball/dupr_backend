# ArrayWrapperDuplicatedAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[DuplicatedAccountResponse]**](DuplicatedAccountResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_duplicated_account_response import ArrayWrapperDuplicatedAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperDuplicatedAccountResponse from a JSON string
array_wrapper_duplicated_account_response_instance = ArrayWrapperDuplicatedAccountResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperDuplicatedAccountResponse.to_json())

# convert the object into a dict
array_wrapper_duplicated_account_response_dict = array_wrapper_duplicated_account_response_instance.to_dict()
# create an instance of ArrayWrapperDuplicatedAccountResponse from a dict
array_wrapper_duplicated_account_response_from_dict = ArrayWrapperDuplicatedAccountResponse.from_dict(array_wrapper_duplicated_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


