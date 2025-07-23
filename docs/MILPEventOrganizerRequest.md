# MILPEventOrganizerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.milp_event_organizer_request import MILPEventOrganizerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MILPEventOrganizerRequest from a JSON string
milp_event_organizer_request_instance = MILPEventOrganizerRequest.from_json(json)
# print the JSON string representation of the object
print(MILPEventOrganizerRequest.to_json())

# convert the object into a dict
milp_event_organizer_request_dict = milp_event_organizer_request_instance.to_dict()
# create an instance of MILPEventOrganizerRequest from a dict
milp_event_organizer_request_from_dict = MILPEventOrganizerRequest.from_dict(milp_event_organizer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


