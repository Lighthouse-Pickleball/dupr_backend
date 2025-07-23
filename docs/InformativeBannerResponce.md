# InformativeBannerResponce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **int** |  | [optional] 
**description** | [**BannerContentResponce**](BannerContentResponce.md) |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**start_date_time** | **datetime** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 

## Example

```python
from dupr_backend.models.informative_banner_responce import InformativeBannerResponce

# TODO update the JSON string below
json = "{}"
# create an instance of InformativeBannerResponce from a JSON string
informative_banner_responce_instance = InformativeBannerResponce.from_json(json)
# print the JSON string representation of the object
print(InformativeBannerResponce.to_json())

# convert the object into a dict
informative_banner_responce_dict = informative_banner_responce_instance.to_dict()
# create an instance of InformativeBannerResponce from a dict
informative_banner_responce_from_dict = InformativeBannerResponce.from_dict(informative_banner_responce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


