# MiLPEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_str** | **str** |  | 
**club_id** | **int** |  | 
**club_name** | **str** |  | [optional] 
**creator_email** | **str** |  | [optional] 
**creator_id** | **int** |  | 
**creator_name** | **str** |  | [optional] 
**default_entry_fee** | **float** |  | 
**default_max_teams** | **int** |  | 
**default_max_waitlist** | **int** |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**divisions** | [**List[Division]**](Division.md) |  | 
**duration** | **List[str]** |  | [optional] 
**event_id** | **int** |  | 
**event_name** | **str** |  | 
**event_type** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from dupr_backend.models.mi_lp_event import MiLPEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MiLPEvent from a JSON string
mi_lp_event_instance = MiLPEvent.from_json(json)
# print the JSON string representation of the object
print(MiLPEvent.to_json())

# convert the object into a dict
mi_lp_event_dict = mi_lp_event_instance.to_dict()
# create an instance of MiLPEvent from a dict
mi_lp_event_from_dict = MiLPEvent.from_dict(mi_lp_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


