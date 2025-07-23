# ArrayWrapperInformativeBannerResponce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[InformativeBannerResponce]**](InformativeBannerResponce.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_informative_banner_responce import ArrayWrapperInformativeBannerResponce

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperInformativeBannerResponce from a JSON string
array_wrapper_informative_banner_responce_instance = ArrayWrapperInformativeBannerResponce.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperInformativeBannerResponce.to_json())

# convert the object into a dict
array_wrapper_informative_banner_responce_dict = array_wrapper_informative_banner_responce_instance.to_dict()
# create an instance of ArrayWrapperInformativeBannerResponce from a dict
array_wrapper_informative_banner_responce_from_dict = ArrayWrapperInformativeBannerResponce.from_dict(array_wrapper_informative_banner_responce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


