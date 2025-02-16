# UserSuggestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**brief_followers** | [**List[UserFollow]**](UserFollow.md) |  | [optional] 
**dupr_id** | **str** |  | 
**follower_count** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**name** | **str** |  | 
**status** | **str** |  | 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.user_suggestion import UserSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of UserSuggestion from a JSON string
user_suggestion_instance = UserSuggestion.from_json(json)
# print the JSON string representation of the object
print(UserSuggestion.to_json())

# convert the object into a dict
user_suggestion_dict = user_suggestion_instance.to_dict()
# create an instance of UserSuggestion from a dict
user_suggestion_from_dict = UserSuggestion.from_dict(user_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


