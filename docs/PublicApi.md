# dupr_backend.PublicApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basic_info**](PublicApi.md#get_basic_info) | **GET** /public/user/info | 


# **get_basic_info**
> ResultBasicInfo get_basic_info()

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.result_basic_info import ResultBasicInfo
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.PublicApi(api_client)

    try:
        api_response = api_instance.get_basic_info()
        print("The response of PublicApi->get_basic_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_basic_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResultBasicInfo**](ResultBasicInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

