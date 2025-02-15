# SingleWrapperOfMatchRatingSimulatorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**MatchRatingSimulatorResponse**](MatchRatingSimulatorResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_match_rating_simulator_response import SingleWrapperOfMatchRatingSimulatorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfMatchRatingSimulatorResponse from a JSON string
single_wrapper_of_match_rating_simulator_response_instance = SingleWrapperOfMatchRatingSimulatorResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfMatchRatingSimulatorResponse.to_json())

# convert the object into a dict
single_wrapper_of_match_rating_simulator_response_dict = single_wrapper_of_match_rating_simulator_response_instance.to_dict()
# create an instance of SingleWrapperOfMatchRatingSimulatorResponse from a dict
single_wrapper_of_match_rating_simulator_response_from_dict = SingleWrapperOfMatchRatingSimulatorResponse.from_dict(single_wrapper_of_match_rating_simulator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


