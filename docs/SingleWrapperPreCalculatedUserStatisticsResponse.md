# SingleWrapperPreCalculatedUserStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PreCalculatedUserStatisticsResponse**](PreCalculatedUserStatisticsResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_pre_calculated_user_statistics_response import SingleWrapperPreCalculatedUserStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPreCalculatedUserStatisticsResponse from a JSON string
single_wrapper_pre_calculated_user_statistics_response_instance = SingleWrapperPreCalculatedUserStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPreCalculatedUserStatisticsResponse.to_json())

# convert the object into a dict
single_wrapper_pre_calculated_user_statistics_response_dict = single_wrapper_pre_calculated_user_statistics_response_instance.to_dict()
# create an instance of SingleWrapperPreCalculatedUserStatisticsResponse from a dict
single_wrapper_pre_calculated_user_statistics_response_from_dict = SingleWrapperPreCalculatedUserStatisticsResponse.from_dict(single_wrapper_pre_calculated_user_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


