# AccountLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**created** | **int** |  | 
**expires_at** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.account_link_response import AccountLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLinkResponse from a JSON string
account_link_response_instance = AccountLinkResponse.from_json(json)
# print the JSON string representation of the object
print(AccountLinkResponse.to_json())

# convert the object into a dict
account_link_response_dict = account_link_response_instance.to_dict()
# create an instance of AccountLinkResponse from a dict
account_link_response_from_dict = AccountLinkResponse.from_dict(account_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


