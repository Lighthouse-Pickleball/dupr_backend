# Division


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** |  | 
**division_id** | **int** |  | 
**division_name** | **str** |  | 
**division_code** | **str** |  | 
**registration_period** | **List[str]** |  | [optional] 
**registration_start** | **date** |  | [optional] 
**registration_end** | **date** |  | [optional] 
**day1_start** | **date** |  | [optional] 
**day2_start** | **date** |  | [optional] 
**max_teams** | **int** |  | [optional] 
**max_waitlist** | **int** |  | [optional] 
**entry_fee** | **float** |  | [optional] 
**prize** | **float** |  | 
**division_type** | **str** |  | 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.division import Division

# TODO update the JSON string below
json = "{}"
# create an instance of Division from a JSON string
division_instance = Division.from_json(json)
# print the JSON string representation of the object
print(Division.to_json())

# convert the object into a dict
division_dict = division_instance.to_dict()
# create an instance of Division from a dict
division_from_dict = Division.from_dict(division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


