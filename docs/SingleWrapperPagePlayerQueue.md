# SingleWrapperPagePlayerQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PagePlayerQueue**](PagePlayerQueue.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_player_queue import SingleWrapperPagePlayerQueue

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPagePlayerQueue from a JSON string
single_wrapper_page_player_queue_instance = SingleWrapperPagePlayerQueue.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPagePlayerQueue.to_json())

# convert the object into a dict
single_wrapper_page_player_queue_dict = single_wrapper_page_player_queue_instance.to_dict()
# create an instance of SingleWrapperPagePlayerQueue from a dict
single_wrapper_page_player_queue_from_dict = SingleWrapperPagePlayerQueue.from_dict(single_wrapper_page_player_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


