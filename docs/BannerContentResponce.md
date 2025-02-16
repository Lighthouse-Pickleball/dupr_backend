# BannerContentResponce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**content_id** | **int** |  | 
**content_type** | **str** |  | [optional] 
**footer** | **str** |  | [optional] 
**footer_type** | **str** |  | [optional] 
**header** | **str** |  | [optional] 
**header_type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.banner_content_responce import BannerContentResponce

# TODO update the JSON string below
json = "{}"
# create an instance of BannerContentResponce from a JSON string
banner_content_responce_instance = BannerContentResponce.from_json(json)
# print the JSON string representation of the object
print(BannerContentResponce.to_json())

# convert the object into a dict
banner_content_responce_dict = banner_content_responce_instance.to_dict()
# create an instance of BannerContentResponce from a dict
banner_content_responce_from_dict = BannerContentResponce.from_dict(banner_content_responce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


