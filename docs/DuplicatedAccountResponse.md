# DuplicatedAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player1** | [**DuplicatedPlayer**](DuplicatedPlayer.md) |  | 
**player2** | [**DuplicatedPlayer**](DuplicatedPlayer.md) |  | 
**probability** | **str** |  | 

## Example

```python
from dupr_backend.models.duplicated_account_response import DuplicatedAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicatedAccountResponse from a JSON string
duplicated_account_response_instance = DuplicatedAccountResponse.from_json(json)
# print the JSON string representation of the object
print(DuplicatedAccountResponse.to_json())

# convert the object into a dict
duplicated_account_response_dict = duplicated_account_response_instance.to_dict()
# create an instance of DuplicatedAccountResponse from a dict
duplicated_account_response_from_dict = DuplicatedAccountResponse.from_dict(duplicated_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


