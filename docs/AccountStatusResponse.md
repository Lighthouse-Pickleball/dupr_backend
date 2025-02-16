# AccountStatusResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**details_submitted** | **bool** |  | 
**errors** | **List[object]** |  | 
**pending_requirement** | **bool** |  | 

## Example

```python
from dupr_backend.models.account_status_response import AccountStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatusResponse from a JSON string
account_status_response_instance = AccountStatusResponse.from_json(json)
# print the JSON string representation of the object
print AccountStatusResponse.to_json()

# convert the object into a dict
account_status_response_dict = account_status_response_instance.to_dict()
# create an instance of AccountStatusResponse from a dict
account_status_response_form_dict = account_status_response.from_dict(account_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


