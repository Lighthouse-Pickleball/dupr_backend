# BannerContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** |  | [optional] 
**header_type** | **str** |  | [optional] 
**content** | **str** |  | 
**content_type** | **str** |  | 
**footer** | **str** |  | [optional] 
**footer_type** | **str** |  | [optional] 
**content_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.banner_content import BannerContent

# TODO update the JSON string below
json = "{}"
# create an instance of BannerContent from a JSON string
banner_content_instance = BannerContent.from_json(json)
# print the JSON string representation of the object
print(BannerContent.to_json())

# convert the object into a dict
banner_content_dict = banner_content_instance.to_dict()
# create an instance of BannerContent from a dict
banner_content_from_dict = BannerContent.from_dict(banner_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


