# MiLPEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **int** |  | 
**club_id** | **int** |  | 
**default_entry_fee** | **float** |  | 
**default_max_teams** | **int** |  | 
**default_max_waitlist** | **int** |  | 
**description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**divisions** | [**List[MILPDivisionRequest]**](MILPDivisionRequest.md) |  | 
**duration** | **List[date]** |  | 
**event_name** | **str** |  | 
**event_type** | **str** |  | 
**organizers** | [**List[MILPEventOrganizerRequest]**](MILPEventOrganizerRequest.md) |  | 
**status** | **str** |  | [optional] 
**time_zone** | **str** |  | 

## Example

```python
from dupr_backend.models.mi_lp_event_request import MiLPEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MiLPEventRequest from a JSON string
mi_lp_event_request_instance = MiLPEventRequest.from_json(json)
# print the JSON string representation of the object
print(MiLPEventRequest.to_json())

# convert the object into a dict
mi_lp_event_request_dict = mi_lp_event_request_instance.to_dict()
# create an instance of MiLPEventRequest from a dict
mi_lp_event_request_from_dict = MiLPEventRequest.from_dict(mi_lp_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


