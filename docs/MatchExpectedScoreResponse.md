# MatchExpectedScoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[TeamsResponse]**](TeamsResponse.md) |  | 

## Example

```python
from dupr_backend.models.match_expected_score_response import MatchExpectedScoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchExpectedScoreResponse from a JSON string
match_expected_score_response_instance = MatchExpectedScoreResponse.from_json(json)
# print the JSON string representation of the object
print(MatchExpectedScoreResponse.to_json())

# convert the object into a dict
match_expected_score_response_dict = match_expected_score_response_instance.to_dict()
# create an instance of MatchExpectedScoreResponse from a dict
match_expected_score_response_from_dict = MatchExpectedScoreResponse.from_dict(match_expected_score_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


