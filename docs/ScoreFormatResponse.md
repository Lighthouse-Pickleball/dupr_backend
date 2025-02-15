# ScoreFormatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 
**games** | **int** |  | 
**id** | **int** |  | 
**priority** | **int** |  | [optional] 
**variant** | **str** |  | 
**winning_score** | **int** |  | 

## Example

```python
from dupr_backend.models.score_format_response import ScoreFormatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreFormatResponse from a JSON string
score_format_response_instance = ScoreFormatResponse.from_json(json)
# print the JSON string representation of the object
print(ScoreFormatResponse.to_json())

# convert the object into a dict
score_format_response_dict = score_format_response_instance.to_dict()
# create an instance of ScoreFormatResponse from a dict
score_format_response_from_dict = ScoreFormatResponse.from_dict(score_format_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


