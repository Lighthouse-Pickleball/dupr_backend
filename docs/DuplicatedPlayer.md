# DuplicatedPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**full_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**dupr_id** | **str** |  | [optional] 
**birthday** | **str** |  | [optional] 
**verified_email** | **bool** |  | 
**email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.duplicated_player import DuplicatedPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicatedPlayer from a JSON string
duplicated_player_instance = DuplicatedPlayer.from_json(json)
# print the JSON string representation of the object
print(DuplicatedPlayer.to_json())

# convert the object into a dict
duplicated_player_dict = duplicated_player_instance.to_dict()
# create an instance of DuplicatedPlayer from a dict
duplicated_player_from_dict = DuplicatedPlayer.from_dict(duplicated_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


