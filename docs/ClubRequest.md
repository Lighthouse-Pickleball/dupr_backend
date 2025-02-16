# ClubRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **int** |  | [optional] 
**attributes** | [**Dict[str, Attribute]**](Attribute.md) |  | [optional] 
**club_id** | **int** |  | 
**club_name** | **str** |  | 
**club_type_id** | **int** |  | 
**currency_code** | **str** |  | 
**long_description** | [**ContentRequest**](ContentRequest.md) |  | [optional] 
**manifest** | [**ContentRequest**](ContentRequest.md) |  | [optional] 
**media_id** | **int** |  | [optional] 
**model_type** | **str** |  | 
**model_value** | **float** |  | 
**short_description** | [**ContentRequest**](ContentRequest.md) |  | [optional] 

## Example

```python
from dupr_backend.models.club_request import ClubRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClubRequest from a JSON string
club_request_instance = ClubRequest.from_json(json)
# print the JSON string representation of the object
print ClubRequest.to_json()

# convert the object into a dict
club_request_dict = club_request_instance.to_dict()
# create an instance of ClubRequest from a dict
club_request_form_dict = club_request.from_dict(club_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


