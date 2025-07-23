# SignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**player_name** | **str** |  | 
**external_id** | **str** |  | [optional] 
**birthdate** | **date** |  | [optional] 
**singles_rating** | **float** |  | [optional] 
**doubles_rating** | **float** |  | [optional] 
**gender** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**dupr_id** | **str** |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.sign_up_request import SignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignUpRequest from a JSON string
sign_up_request_instance = SignUpRequest.from_json(json)
# print the JSON string representation of the object
print(SignUpRequest.to_json())

# convert the object into a dict
sign_up_request_dict = sign_up_request_instance.to_dict()
# create an instance of SignUpRequest from a dict
sign_up_request_from_dict = SignUpRequest.from_dict(sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


