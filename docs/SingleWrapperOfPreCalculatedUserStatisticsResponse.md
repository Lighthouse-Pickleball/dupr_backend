# SingleWrapperOfPreCalculatedUserStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PreCalculatedUserStatisticsResponse**](PreCalculatedUserStatisticsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_pre_calculated_user_statistics_response import SingleWrapperOfPreCalculatedUserStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPreCalculatedUserStatisticsResponse from a JSON string
single_wrapper_of_pre_calculated_user_statistics_response_instance = SingleWrapperOfPreCalculatedUserStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPreCalculatedUserStatisticsResponse.to_json())

# convert the object into a dict
single_wrapper_of_pre_calculated_user_statistics_response_dict = single_wrapper_of_pre_calculated_user_statistics_response_instance.to_dict()
# create an instance of SingleWrapperOfPreCalculatedUserStatisticsResponse from a dict
single_wrapper_of_pre_calculated_user_statistics_response_from_dict = SingleWrapperOfPreCalculatedUserStatisticsResponse.from_dict(single_wrapper_of_pre_calculated_user_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


