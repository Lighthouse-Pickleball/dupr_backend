# MiLPEventSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**filters** | [**EventFilter**](EventFilter.md) |  | [optional] 

## Example

```python
from dupr_backend.models.mi_lp_event_search_request import MiLPEventSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MiLPEventSearchRequest from a JSON string
mi_lp_event_search_request_instance = MiLPEventSearchRequest.from_json(json)
# print the JSON string representation of the object
print(MiLPEventSearchRequest.to_json())

# convert the object into a dict
mi_lp_event_search_request_dict = mi_lp_event_search_request_instance.to_dict()
# create an instance of MiLPEventSearchRequest from a dict
mi_lp_event_search_request_from_dict = MiLPEventSearchRequest.from_dict(mi_lp_event_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


