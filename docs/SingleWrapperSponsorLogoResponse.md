# SingleWrapperSponsorLogoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**SponsorLogoResponse**](SponsorLogoResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_sponsor_logo_response import SingleWrapperSponsorLogoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperSponsorLogoResponse from a JSON string
single_wrapper_sponsor_logo_response_instance = SingleWrapperSponsorLogoResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperSponsorLogoResponse.to_json())

# convert the object into a dict
single_wrapper_sponsor_logo_response_dict = single_wrapper_sponsor_logo_response_instance.to_dict()
# create an instance of SingleWrapperSponsorLogoResponse from a dict
single_wrapper_sponsor_logo_response_from_dict = SingleWrapperSponsorLogoResponse.from_dict(single_wrapper_sponsor_logo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


