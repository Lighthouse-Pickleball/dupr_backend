# SingleWrapperOfPageOfMiLPEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfMiLPEvent**](PageOfMiLPEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_mi_lp_event import SingleWrapperOfPageOfMiLPEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfMiLPEvent from a JSON string
single_wrapper_of_page_of_mi_lp_event_instance = SingleWrapperOfPageOfMiLPEvent.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfPageOfMiLPEvent.to_json()

# convert the object into a dict
single_wrapper_of_page_of_mi_lp_event_dict = single_wrapper_of_page_of_mi_lp_event_instance.to_dict()
# create an instance of SingleWrapperOfPageOfMiLPEvent from a dict
single_wrapper_of_page_of_mi_lp_event_form_dict = single_wrapper_of_page_of_mi_lp_event.from_dict(single_wrapper_of_page_of_mi_lp_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


