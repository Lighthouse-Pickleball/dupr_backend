# ArrayWrapperScoreFormatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[ScoreFormatResponse]**](ScoreFormatResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_score_format_response import ArrayWrapperScoreFormatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperScoreFormatResponse from a JSON string
array_wrapper_score_format_response_instance = ArrayWrapperScoreFormatResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperScoreFormatResponse.to_json())

# convert the object into a dict
array_wrapper_score_format_response_dict = array_wrapper_score_format_response_instance.to_dict()
# create an instance of ArrayWrapperScoreFormatResponse from a dict
array_wrapper_score_format_response_from_dict = ArrayWrapperScoreFormatResponse.from_dict(array_wrapper_score_format_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


