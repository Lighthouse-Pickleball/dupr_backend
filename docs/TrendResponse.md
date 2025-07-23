# TrendResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games_trend** | [**List[GameTrendResponse]**](GameTrendResponse.md) |  | 

## Example

```python
from dupr_backend.models.trend_response import TrendResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrendResponse from a JSON string
trend_response_instance = TrendResponse.from_json(json)
# print the JSON string representation of the object
print(TrendResponse.to_json())

# convert the object into a dict
trend_response_dict = trend_response_instance.to_dict()
# create an instance of TrendResponse from a dict
trend_response_from_dict = TrendResponse.from_dict(trend_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


