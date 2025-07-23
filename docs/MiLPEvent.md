# MiLPEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** |  | 
**event_name** | **str** |  | 
**club_id** | **int** |  | 
**club_name** | **str** |  | [optional] 
**creator_id** | **int** |  | 
**creator_name** | **str** |  | [optional] 
**creator_email** | **str** |  | [optional] 
**event_type** | **str** |  | 
**default_max_teams** | **int** |  | 
**default_max_waitlist** | **int** |  | 
**default_entry_fee** | **float** |  | 
**status** | **str** |  | 
**duration** | **List[str]** |  | [optional] 
**address_str** | **str** |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**divisions** | [**List[Division]**](Division.md) |  | 

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


