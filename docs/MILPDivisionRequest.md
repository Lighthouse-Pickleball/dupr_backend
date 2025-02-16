# MILPDivisionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day1_start** | **datetime** |  | 
**day2_start** | **datetime** |  | [optional] 
**division_name** | **str** |  | [optional] 
**division_type** | **str** |  | 
**entry_fee** | **float** |  | [optional] 
**max_teams** | **int** |  | [optional] 
**max_waitlist** | **int** |  | [optional] 
**prize** | **float** |  | 
**registration_period** | **List[date]** |  | 

## Example

```python
from dupr_backend.models.milp_division_request import MILPDivisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MILPDivisionRequest from a JSON string
milp_division_request_instance = MILPDivisionRequest.from_json(json)
# print the JSON string representation of the object
print MILPDivisionRequest.to_json()

# convert the object into a dict
milp_division_request_dict = milp_division_request_instance.to_dict()
# create an instance of MILPDivisionRequest from a dict
milp_division_request_form_dict = milp_division_request.from_dict(milp_division_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


