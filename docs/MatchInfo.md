# MatchInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_format** | **str** |  | 
**match_source** | **str** |  | 
**event_name** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.match_info import MatchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MatchInfo from a JSON string
match_info_instance = MatchInfo.from_json(json)
# print the JSON string representation of the object
print(MatchInfo.to_json())

# convert the object into a dict
match_info_dict = match_info_instance.to_dict()
# create an instance of MatchInfo from a dict
match_info_from_dict = MatchInfo.from_dict(match_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


