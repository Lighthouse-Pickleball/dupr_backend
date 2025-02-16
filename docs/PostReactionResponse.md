# PostReactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** |  | 
**actor** | [**ActivityUser**](ActivityUser.md) |  | 
**children** | **Dict[str, List[PostReactionResponse]]** |  | 
**comment** | **str** |  | 
**created_at** | **int** |  | 
**getstream_id** | **str** |  | 
**id** | **str** |  | 
**images** | **List[str]** |  | 
**matches** | [**List[Match]**](Match.md) |  | 
**parent_id** | **str** |  | 
**post_id** | **str** |  | 
**react** | **str** |  | 
**reaction_counts** | **Dict[str, object]** |  | 
**tags** | [**List[ActivityUser]**](ActivityUser.md) |  | 
**updated_at** | **int** |  | 

## Example

```python
from dupr_backend.models.post_reaction_response import PostReactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostReactionResponse from a JSON string
post_reaction_response_instance = PostReactionResponse.from_json(json)
# print the JSON string representation of the object
print PostReactionResponse.to_json()

# convert the object into a dict
post_reaction_response_dict = post_reaction_response_instance.to_dict()
# create an instance of PostReactionResponse from a dict
post_reaction_response_form_dict = post_reaction_response.from_dict(post_reaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


