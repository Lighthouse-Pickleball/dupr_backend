# SingleWrapperMiLPTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**MiLPTeam**](MiLPTeam.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_mi_lp_team import SingleWrapperMiLPTeam

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperMiLPTeam from a JSON string
single_wrapper_mi_lp_team_instance = SingleWrapperMiLPTeam.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperMiLPTeam.to_json())

# convert the object into a dict
single_wrapper_mi_lp_team_dict = single_wrapper_mi_lp_team_instance.to_dict()
# create an instance of SingleWrapperMiLPTeam from a dict
single_wrapper_mi_lp_team_from_dict = SingleWrapperMiLPTeam.from_dict(single_wrapper_mi_lp_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


