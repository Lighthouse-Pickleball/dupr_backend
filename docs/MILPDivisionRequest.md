# MILPDivisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**division_type** | **str** |  | 
**division_name** | **str** |  | [optional] 
**max_teams** | **int** |  | [optional] 
**max_waitlist** | **int** |  | [optional] 
**day1_start** | **datetime** |  | 
**day2_start** | **datetime** |  | [optional] 
**registration_period** | **List[date]** |  | 
**entry_fee** | **float** |  | [optional] 
**prize** | **float** |  | 

## Example

```python
from dupr_backend.models.milp_division_request import MILPDivisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MILPDivisionRequest from a JSON string
milp_division_request_instance = MILPDivisionRequest.from_json(json)
# print the JSON string representation of the object
print(MILPDivisionRequest.to_json())

# convert the object into a dict
milp_division_request_dict = milp_division_request_instance.to_dict()
# create an instance of MILPDivisionRequest from a dict
milp_division_request_from_dict = MILPDivisionRequest.from_dict(milp_division_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


