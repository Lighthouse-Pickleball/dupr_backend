# PolicyDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_policy** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**safety_policy** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.policy_details_response import PolicyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyDetailsResponse from a JSON string
policy_details_response_instance = PolicyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PolicyDetailsResponse.to_json())

# convert the object into a dict
policy_details_response_dict = policy_details_response_instance.to_dict()
# create an instance of PolicyDetailsResponse from a dict
policy_details_response_from_dict = PolicyDetailsResponse.from_dict(policy_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


