# WithdrawPlayerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**player_id** | **int** |  | 
**registration_id** | **int** |  | 

## Example

```python
from dupr_backend.models.withdraw_player_request import WithdrawPlayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawPlayerRequest from a JSON string
withdraw_player_request_instance = WithdrawPlayerRequest.from_json(json)
# print the JSON string representation of the object
print WithdrawPlayerRequest.to_json()

# convert the object into a dict
withdraw_player_request_dict = withdraw_player_request_instance.to_dict()
# create an instance of WithdrawPlayerRequest from a dict
withdraw_player_request_form_dict = withdraw_player_request.from_dict(withdraw_player_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


