# SingleWrapperUserStatisticResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**UserStatisticResponse**](UserStatisticResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_user_statistic_response import SingleWrapperUserStatisticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperUserStatisticResponse from a JSON string
single_wrapper_user_statistic_response_instance = SingleWrapperUserStatisticResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperUserStatisticResponse.to_json())

# convert the object into a dict
single_wrapper_user_statistic_response_dict = single_wrapper_user_statistic_response_instance.to_dict()
# create an instance of SingleWrapperUserStatisticResponse from a dict
single_wrapper_user_statistic_response_from_dict = SingleWrapperUserStatisticResponse.from_dict(single_wrapper_user_statistic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


