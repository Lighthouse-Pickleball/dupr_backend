# SingleWrapperOfMiLPEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**MiLPEvent**](MiLPEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_mi_lp_event import SingleWrapperOfMiLPEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfMiLPEvent from a JSON string
single_wrapper_of_mi_lp_event_instance = SingleWrapperOfMiLPEvent.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfMiLPEvent.to_json())

# convert the object into a dict
single_wrapper_of_mi_lp_event_dict = single_wrapper_of_mi_lp_event_instance.to_dict()
# create an instance of SingleWrapperOfMiLPEvent from a dict
single_wrapper_of_mi_lp_event_from_dict = SingleWrapperOfMiLPEvent.from_dict(single_wrapper_of_mi_lp_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


