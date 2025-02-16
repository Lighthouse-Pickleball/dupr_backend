# EditPartnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**partner_id** | **int** |  | 
**partner_status** | **str** |  | 
**registration_id** | **int** |  | 

## Example

```python
from dupr_backend.models.edit_partner_request import EditPartnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditPartnerRequest from a JSON string
edit_partner_request_instance = EditPartnerRequest.from_json(json)
# print the JSON string representation of the object
print(EditPartnerRequest.to_json())

# convert the object into a dict
edit_partner_request_dict = edit_partner_request_instance.to_dict()
# create an instance of EditPartnerRequest from a dict
edit_partner_request_from_dict = EditPartnerRequest.from_dict(edit_partner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


