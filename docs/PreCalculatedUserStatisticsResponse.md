# PreCalculatedUserStatisticsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doubles** | [**MatchRatings**](MatchRatings.md) |  | 
**resul_overview** | [**RatingsOverviewResponse**](RatingsOverviewResponse.md) |  | 
**singles** | [**MatchRatings**](MatchRatings.md) |  | 

## Example

```python
from dupr_backend.models.pre_calculated_user_statistics_response import PreCalculatedUserStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PreCalculatedUserStatisticsResponse from a JSON string
pre_calculated_user_statistics_response_instance = PreCalculatedUserStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print PreCalculatedUserStatisticsResponse.to_json()

# convert the object into a dict
pre_calculated_user_statistics_response_dict = pre_calculated_user_statistics_response_instance.to_dict()
# create an instance of PreCalculatedUserStatisticsResponse from a dict
pre_calculated_user_statistics_response_form_dict = pre_calculated_user_statistics_response.from_dict(pre_calculated_user_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


