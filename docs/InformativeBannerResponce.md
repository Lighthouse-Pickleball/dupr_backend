# InformativeBannerResponce


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **int** |  | [optional] 
**description** | [**BannerContentResponce**](BannerContentResponce.md) |  | [optional] 
**end_date_time** | **str** |  | [optional] 
**start_date_time** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.informative_banner_responce import InformativeBannerResponce

# TODO update the JSON string below
json = "{}"
# create an instance of InformativeBannerResponce from a JSON string
informative_banner_responce_instance = InformativeBannerResponce.from_json(json)
# print the JSON string representation of the object
print InformativeBannerResponce.to_json()

# convert the object into a dict
informative_banner_responce_dict = informative_banner_responce_instance.to_dict()
# create an instance of InformativeBannerResponce from a dict
informative_banner_responce_form_dict = informative_banner_responce.from_dict(informative_banner_responce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


