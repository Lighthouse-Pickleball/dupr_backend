# LeagueContactDetailResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.league_contact_detail_response import LeagueContactDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueContactDetailResponse from a JSON string
league_contact_detail_response_instance = LeagueContactDetailResponse.from_json(json)
# print the JSON string representation of the object
print LeagueContactDetailResponse.to_json()

# convert the object into a dict
league_contact_detail_response_dict = league_contact_detail_response_instance.to_dict()
# create an instance of LeagueContactDetailResponse from a dict
league_contact_detail_response_form_dict = league_contact_detail_response.from_dict(league_contact_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


