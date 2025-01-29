# dupr_backend.RootPathControllerApi

All URIs are relative to *https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_ads_using_get**](RootPathControllerApi.md#app_ads_using_get) | **GET** /app-ads.txt | appAds

# **app_ads_using_get**
> object app_ads_using_get(entries=entries)

appAds

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.RootPathControllerApi()
entries = 'entries_example' # str | entries (optional)

try:
    # appAds
    api_response = api_instance.app_ads_using_get(entries=entries)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

