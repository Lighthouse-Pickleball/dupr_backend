# SingleWrapperPageMiLPEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageMiLPEvent**](PageMiLPEvent.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_mi_lp_event import SingleWrapperPageMiLPEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageMiLPEvent from a JSON string
single_wrapper_page_mi_lp_event_instance = SingleWrapperPageMiLPEvent.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageMiLPEvent.to_json())

# convert the object into a dict
single_wrapper_page_mi_lp_event_dict = single_wrapper_page_mi_lp_event_instance.to_dict()
# create an instance of SingleWrapperPageMiLPEvent from a dict
single_wrapper_page_mi_lp_event_from_dict = SingleWrapperPageMiLPEvent.from_dict(single_wrapper_page_mi_lp_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


