# ArrayWrapperOfScoreFormatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[ScoreFormatResponse]**](ScoreFormatResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_score_format_response import ArrayWrapperOfScoreFormatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfScoreFormatResponse from a JSON string
array_wrapper_of_score_format_response_instance = ArrayWrapperOfScoreFormatResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfScoreFormatResponse.to_json())

# convert the object into a dict
array_wrapper_of_score_format_response_dict = array_wrapper_of_score_format_response_instance.to_dict()
# create an instance of ArrayWrapperOfScoreFormatResponse from a dict
array_wrapper_of_score_format_response_from_dict = ArrayWrapperOfScoreFormatResponse.from_dict(array_wrapper_of_score_format_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


