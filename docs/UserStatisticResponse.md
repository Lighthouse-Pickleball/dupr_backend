# UserStatisticResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overview** | [**RatingOverviewResponse**](RatingOverviewResponse.md) |  | 
**trends** | [**TrendResponse**](TrendResponse.md) |  | 

## Example

```python
from dupr_backend.models.user_statistic_response import UserStatisticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserStatisticResponse from a JSON string
user_statistic_response_instance = UserStatisticResponse.from_json(json)
# print the JSON string representation of the object
print(UserStatisticResponse.to_json())

# convert the object into a dict
user_statistic_response_dict = user_statistic_response_instance.to_dict()
# create an instance of UserStatisticResponse from a dict
user_statistic_response_from_dict = UserStatisticResponse.from_dict(user_statistic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


