# SingleWrapperPageOpenPlayEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageOpenPlayEvent**](PageOpenPlayEvent.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_open_play_event import SingleWrapperPageOpenPlayEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageOpenPlayEvent from a JSON string
single_wrapper_page_open_play_event_instance = SingleWrapperPageOpenPlayEvent.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageOpenPlayEvent.to_json())

# convert the object into a dict
single_wrapper_page_open_play_event_dict = single_wrapper_page_open_play_event_instance.to_dict()
# create an instance of SingleWrapperPageOpenPlayEvent from a dict
single_wrapper_page_open_play_event_from_dict = SingleWrapperPageOpenPlayEvent.from_dict(single_wrapper_page_open_play_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


