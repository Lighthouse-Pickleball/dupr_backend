# MiLPEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** |  | 
**organizers** | [**List[MILPEventOrganizerRequest]**](MILPEventOrganizerRequest.md) |  | 
**default_entry_fee** | **float** |  | 
**default_max_teams** | **int** |  | 
**default_max_waitlist** | **int** |  | 
**description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**address_id** | **int** |  | 
**event_type** | **str** |  | 
**time_zone** | **str** |  | 
**duration** | **List[date]** |  | 
**divisions** | [**List[MILPDivisionRequest]**](MILPDivisionRequest.md) |  | 
**club_id** | **int** |  | 
**status** | **str** |  | [optional] 

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


