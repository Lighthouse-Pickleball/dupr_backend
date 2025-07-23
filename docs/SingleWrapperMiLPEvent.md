# SingleWrapperMiLPEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**MiLPEvent**](MiLPEvent.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_mi_lp_event import SingleWrapperMiLPEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperMiLPEvent from a JSON string
single_wrapper_mi_lp_event_instance = SingleWrapperMiLPEvent.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperMiLPEvent.to_json())

# convert the object into a dict
single_wrapper_mi_lp_event_dict = single_wrapper_mi_lp_event_instance.to_dict()
# create an instance of SingleWrapperMiLPEvent from a dict
single_wrapper_mi_lp_event_from_dict = SingleWrapperMiLPEvent.from_dict(single_wrapper_mi_lp_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


