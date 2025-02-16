# SingleWrapperOfPageOfPlayerQueue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfPlayerQueue**](PageOfPlayerQueue.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_player_queue import SingleWrapperOfPageOfPlayerQueue

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfPlayerQueue from a JSON string
single_wrapper_of_page_of_player_queue_instance = SingleWrapperOfPageOfPlayerQueue.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfPageOfPlayerQueue.to_json()

# convert the object into a dict
single_wrapper_of_page_of_player_queue_dict = single_wrapper_of_page_of_player_queue_instance.to_dict()
# create an instance of SingleWrapperOfPageOfPlayerQueue from a dict
single_wrapper_of_page_of_player_queue_form_dict = single_wrapper_of_page_of_player_queue.from_dict(single_wrapper_of_page_of_player_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


