# PreMatchRatingAndImpact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_double_rating_impact_player1** | **float** |  | [optional] 
**match_double_rating_impact_player2** | **float** |  | [optional] 
**match_single_rating_impact_player1** | **float** |  | [optional] 
**match_single_rating_impact_player2** | **float** |  | [optional] 
**pre_match_double_rating_player1** | **float** |  | [optional] 
**pre_match_double_rating_player2** | **float** |  | [optional] 
**pre_match_single_rating_player1** | **float** |  | [optional] 
**pre_match_single_rating_player2** | **float** |  | [optional] 

## Example

```python
from dupr_backend.models.pre_match_rating_and_impact import PreMatchRatingAndImpact

# TODO update the JSON string below
json = "{}"
# create an instance of PreMatchRatingAndImpact from a JSON string
pre_match_rating_and_impact_instance = PreMatchRatingAndImpact.from_json(json)
# print the JSON string representation of the object
print(PreMatchRatingAndImpact.to_json())

# convert the object into a dict
pre_match_rating_and_impact_dict = pre_match_rating_and_impact_instance.to_dict()
# create an instance of PreMatchRatingAndImpact from a dict
pre_match_rating_and_impact_from_dict = PreMatchRatingAndImpact.from_dict(pre_match_rating_and_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


