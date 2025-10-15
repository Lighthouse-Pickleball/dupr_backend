# MatchExpectedScoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[TeamIds]**](TeamIds.md) |  | 
**event_format** | **str** |  | 
**match_source** | **str** |  | 
**game_count** | **int** |  | 
**winning_score** | **int** |  | 
**match_type** | **str** |  | 

## Example

```python
from dupr_backend.models.match_expected_score_request import MatchExpectedScoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchExpectedScoreRequest from a JSON string
match_expected_score_request_instance = MatchExpectedScoreRequest.from_json(json)
# print the JSON string representation of the object
print(MatchExpectedScoreRequest.to_json())

# convert the object into a dict
match_expected_score_request_dict = match_expected_score_request_instance.to_dict()
# create an instance of MatchExpectedScoreRequest from a dict
match_expected_score_request_from_dict = MatchExpectedScoreRequest.from_dict(match_expected_score_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


