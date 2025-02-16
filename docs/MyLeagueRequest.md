# MyLeagueRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.my_league_request import MyLeagueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MyLeagueRequest from a JSON string
my_league_request_instance = MyLeagueRequest.from_json(json)
# print the JSON string representation of the object
print MyLeagueRequest.to_json()

# convert the object into a dict
my_league_request_dict = my_league_request_instance.to_dict()
# create an instance of MyLeagueRequest from a dict
my_league_request_form_dict = my_league_request.from_dict(my_league_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


