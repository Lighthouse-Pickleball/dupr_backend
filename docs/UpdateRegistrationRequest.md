# UpdateRegistrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**bracket_id** | **int** |  | 
**league_id** | **int** |  | 
**payment_status** | **str** |  | 
**registration_status** | **str** |  | 
**bracket_fees_paid** | **float** |  | [optional] 
**event_fees_paid** | **float** |  | [optional] 
**is_registered** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.update_registration_request import UpdateRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRegistrationRequest from a JSON string
update_registration_request_instance = UpdateRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRegistrationRequest.to_json())

# convert the object into a dict
update_registration_request_dict = update_registration_request_instance.to_dict()
# create an instance of UpdateRegistrationRequest from a dict
update_registration_request_from_dict = UpdateRegistrationRequest.from_dict(update_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


