# MatchRatingSimulatorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match** | [**MatchInfo**](MatchInfo.md) |  | 
**team1** | [**TeamInfo**](TeamInfo.md) |  | 
**team2** | [**TeamInfo**](TeamInfo.md) |  | 

## Example

```python
from dupr_backend.models.match_rating_simulator_request import MatchRatingSimulatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRatingSimulatorRequest from a JSON string
match_rating_simulator_request_instance = MatchRatingSimulatorRequest.from_json(json)
# print the JSON string representation of the object
print MatchRatingSimulatorRequest.to_json()

# convert the object into a dict
match_rating_simulator_request_dict = match_rating_simulator_request_instance.to_dict()
# create an instance of MatchRatingSimulatorRequest from a dict
match_rating_simulator_request_form_dict = match_rating_simulator_request.from_dict(match_rating_simulator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


