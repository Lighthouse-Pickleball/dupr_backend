# CreateClubsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**place_id** | **str** |  | 
**club_name** | **str** |  | 
**phone_number** | **str** |  | [optional] 
**director_name** | **str** |  | 
**director_email** | **str** |  | 
**director_phone** | **str** |  | [optional] 
**dupr_id** | **str** |  | 
**revenue_type** | **str** |  | 
**revenue_value** | **float** |  | 
**currency_code** | **str** |  | 
**iso_code_club** | **str** |  | 
**iso_code_director** | **str** |  | 

## Example

```python
from dupr_backend.models.create_clubs_request import CreateClubsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClubsRequest from a JSON string
create_clubs_request_instance = CreateClubsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateClubsRequest.to_json())

# convert the object into a dict
create_clubs_request_dict = create_clubs_request_instance.to_dict()
# create an instance of CreateClubsRequest from a dict
create_clubs_request_from_dict = CreateClubsRequest.from_dict(create_clubs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


