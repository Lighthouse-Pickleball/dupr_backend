# ArrayWrapperOfDuplicatedAccountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[DuplicatedAccountResponse]**](DuplicatedAccountResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_duplicated_account_response import ArrayWrapperOfDuplicatedAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfDuplicatedAccountResponse from a JSON string
array_wrapper_of_duplicated_account_response_instance = ArrayWrapperOfDuplicatedAccountResponse.from_json(json)
# print the JSON string representation of the object
print ArrayWrapperOfDuplicatedAccountResponse.to_json()

# convert the object into a dict
array_wrapper_of_duplicated_account_response_dict = array_wrapper_of_duplicated_account_response_instance.to_dict()
# create an instance of ArrayWrapperOfDuplicatedAccountResponse from a dict
array_wrapper_of_duplicated_account_response_form_dict = array_wrapper_of_duplicated_account_response.from_dict(array_wrapper_of_duplicated_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


