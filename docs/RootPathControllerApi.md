# dupr_backend.RootPathControllerApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_ads_using_get**](RootPathControllerApi.md#app_ads_using_get) | **GET** /app-ads.txt | appAds


# **app_ads_using_get**
> object app_ads_using_get(entries=entries)

appAds

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://backend.mydupr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "http://https://backend.mydupr.com"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.RootPathControllerApi(api_client)
    entries = 'entries_example' # str | entries (optional)

    try:
        # appAds
        api_response = api_instance.app_ads_using_get(entries=entries)
        print("The response of RootPathControllerApi->app_ads_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RootPathControllerApi->app_ads_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entries** | **str**| entries | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

