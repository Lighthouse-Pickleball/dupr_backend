# PostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**activity_id** | **str** |  | 
**actor** | [**ActivityUser**](ActivityUser.md) |  | 
**verb** | **str** |  | 
**content** | **str** |  | 
**reaction_counts** | **Dict[str, float]** |  | 
**own_reactions** | **Dict[str, List[PostReactionResponse]]** |  | 
**tags** | [**List[ActivityUser]**](ActivityUser.md) |  | 
**hashtags** | **List[str]** |  | 
**images** | **List[str]** |  | 
**matches** | [**List[Match]**](Match.md) |  | 
**location** | **Dict[str, object]** |  | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from dupr_backend.models.post_response import PostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostResponse from a JSON string
post_response_instance = PostResponse.from_json(json)
# print the JSON string representation of the object
print(PostResponse.to_json())

# convert the object into a dict
post_response_dict = post_response_instance.to_dict()
# create an instance of PostResponse from a dict
post_response_from_dict = PostResponse.from_dict(post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


