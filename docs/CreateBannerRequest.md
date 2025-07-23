# CreateBannerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **int** |  | 
**content_id** | **int** |  | 
**description** | [**BannerContent**](BannerContent.md) |  | 
**title** | **str** |  | 
**status** | **str** |  | 
**start_date_time** | **datetime** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 

## Example

```python
from dupr_backend.models.create_banner_request import CreateBannerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBannerRequest from a JSON string
create_banner_request_instance = CreateBannerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBannerRequest.to_json())

# convert the object into a dict
create_banner_request_dict = create_banner_request_instance.to_dict()
# create an instance of CreateBannerRequest from a dict
create_banner_request_from_dict = CreateBannerRequest.from_dict(create_banner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


