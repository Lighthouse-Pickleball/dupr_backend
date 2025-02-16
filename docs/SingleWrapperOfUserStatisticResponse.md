# SingleWrapperOfUserStatisticResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**UserStatisticResponse**](UserStatisticResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_user_statistic_response import SingleWrapperOfUserStatisticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfUserStatisticResponse from a JSON string
single_wrapper_of_user_statistic_response_instance = SingleWrapperOfUserStatisticResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfUserStatisticResponse.to_json()

# convert the object into a dict
single_wrapper_of_user_statistic_response_dict = single_wrapper_of_user_statistic_response_instance.to_dict()
# create an instance of SingleWrapperOfUserStatisticResponse from a dict
single_wrapper_of_user_statistic_response_form_dict = single_wrapper_of_user_statistic_response.from_dict(single_wrapper_of_user_statistic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


