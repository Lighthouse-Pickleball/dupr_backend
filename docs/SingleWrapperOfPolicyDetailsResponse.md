# SingleWrapperOfPolicyDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PolicyDetailsResponse**](PolicyDetailsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_policy_details_response import SingleWrapperOfPolicyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPolicyDetailsResponse from a JSON string
single_wrapper_of_policy_details_response_instance = SingleWrapperOfPolicyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPolicyDetailsResponse.to_json())

# convert the object into a dict
single_wrapper_of_policy_details_response_dict = single_wrapper_of_policy_details_response_instance.to_dict()
# create an instance of SingleWrapperOfPolicyDetailsResponse from a dict
single_wrapper_of_policy_details_response_from_dict = SingleWrapperOfPolicyDetailsResponse.from_dict(single_wrapper_of_policy_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


