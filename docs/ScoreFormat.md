# ScoreFormat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**games** | **int** |  | 
**id** | **int** |  | [optional] 
**priority** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**variant** | **str** |  | [optional] 
**winning_score** | **int** |  | 

## Example

```python
from dupr_backend.models.score_format import ScoreFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreFormat from a JSON string
score_format_instance = ScoreFormat.from_json(json)
# print the JSON string representation of the object
print ScoreFormat.to_json()

# convert the object into a dict
score_format_dict = score_format_instance.to_dict()
# create an instance of ScoreFormat from a dict
score_format_form_dict = score_format.from_dict(score_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


