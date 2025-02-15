# AddPartnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **int** |  | 
**partner_status** | **str** |  | 

## Example

```python
from dupr_backend.models.add_partner_request import AddPartnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPartnerRequest from a JSON string
add_partner_request_instance = AddPartnerRequest.from_json(json)
# print the JSON string representation of the object
print(AddPartnerRequest.to_json())

# convert the object into a dict
add_partner_request_dict = add_partner_request_instance.to_dict()
# create an instance of AddPartnerRequest from a dict
add_partner_request_from_dict = AddPartnerRequest.from_dict(add_partner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


