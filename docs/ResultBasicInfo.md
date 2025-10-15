# ResultBasicInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**results** | [**List[BasicInfo]**](BasicInfo.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from dupr_backend.models.result_basic_info import ResultBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResultBasicInfo from a JSON string
result_basic_info_instance = ResultBasicInfo.from_json(json)
# print the JSON string representation of the object
print(ResultBasicInfo.to_json())

# convert the object into a dict
result_basic_info_dict = result_basic_info_instance.to_dict()
# create an instance of ResultBasicInfo from a dict
result_basic_info_from_dict = ResultBasicInfo.from_dict(result_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


