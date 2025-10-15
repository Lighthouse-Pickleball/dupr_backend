# dupr_backend.ClientApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_name_by_key**](ClientApi.md#get_client_name_by_key) | **GET** /client/{version}/{clientKey}/name | 


# **get_client_name_by_key**
> SingleWrapperString get_client_name_by_key(version, client_key)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_string import SingleWrapperString
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
    api_instance = dupr_backend.ClientApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    client_key = 'client_key_example' # str | 

    try:
        api_response = api_instance.get_client_name_by_key(version, client_key)
        print("The response of ClientApi->get_client_name_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientApi->get_client_name_by_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **client_key** | **str**|  | 

### Return type

[**SingleWrapperString**](SingleWrapperString.md)

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

