# MatchRatingSimulatorResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_format** | **str** |  | 
**match_source** | **str** |  | 
**teams** | [**List[TeamInfo0]**](TeamInfo0.md) |  | 

## Example

```python
from dupr_backend.models.match_rating_simulator_response import MatchRatingSimulatorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRatingSimulatorResponse from a JSON string
match_rating_simulator_response_instance = MatchRatingSimulatorResponse.from_json(json)
# print the JSON string representation of the object
print MatchRatingSimulatorResponse.to_json()

# convert the object into a dict
match_rating_simulator_response_dict = match_rating_simulator_response_instance.to_dict()
# create an instance of MatchRatingSimulatorResponse from a dict
match_rating_simulator_response_form_dict = match_rating_simulator_response.from_dict(match_rating_simulator_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


