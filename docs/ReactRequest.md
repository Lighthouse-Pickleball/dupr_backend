# ReactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | **int** | Obfuscated Id of user do the reaction | 
**id** | **str** | The post&#39;s id | 
**react** | **str** | type of reaction, if COMMENT then add the contain in the &#39;comment&#39;, else let it empty | 
**comment** | **str** | If the react type is comment, then put the contain here | 
**tags** | **List[int]** |  | 
**images** | **List[str]** |  | 
**matches** | **List[int]** |  | 
**react_on** | **str** | if react on comment, add this comment getstreamId here, if not lets empty | 

## Example

```python
from dupr_backend.models.react_request import ReactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReactRequest from a JSON string
react_request_instance = ReactRequest.from_json(json)
# print the JSON string representation of the object
print(ReactRequest.to_json())

# convert the object into a dict
react_request_dict = react_request_instance.to_dict()
# create an instance of ReactRequest from a dict
react_request_from_dict = ReactRequest.from_dict(react_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


