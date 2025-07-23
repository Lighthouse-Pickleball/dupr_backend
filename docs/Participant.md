# Participant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**full_name** | **str** |  | 
**username** | **str** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**partner_status** | **str** |  | 
**status** | **str** |  | [optional] 
**payment_due** | **str** |  | [optional] 
**payment_status** | **str** |  | [optional] 
**is_registered** | **bool** |  | 
**is_wait_listed** | **bool** |  | 
**is_c_lub_member** | **bool** |  | 
**payment_refunded** | **bool** |  | 
**refund_amount** | **float** |  | 
**is_substitute** | **bool** |  | 
**substitute** | **bool** |  | [optional] 
**club_member** | **bool** |  | [optional] 
**registered** | **bool** |  | [optional] 
**wait_listed** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.participant import Participant

# TODO update the JSON string below
json = "{}"
# create an instance of Participant from a JSON string
participant_instance = Participant.from_json(json)
# print the JSON string representation of the object
print(Participant.to_json())

# convert the object into a dict
participant_dict = participant_instance.to_dict()
# create an instance of Participant from a dict
participant_from_dict = Participant.from_dict(participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


