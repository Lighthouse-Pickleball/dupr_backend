# dupr_backend.ClientApi

All URIs are relative to *https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_name_by_key_using_get**](ClientApi.md#get_client_name_by_key_using_get) | **GET** /client/{version}/{clientKey}/name | getClientNameByKey

# **get_client_name_by_key_using_get**
> SingleWrapperOfstring get_client_name_by_key_using_get(authorization, client_key, version)

getClientNameByKey

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClientApi()
authorization = 'Bearer ' # str |  (default to Bearer )
client_key = 'client_key_example' # str | clientKey
version = 'version_example' # str | version

try:
    # getClientNameByKey
    api_response = api_instance.get_client_name_by_key_using_get(authorization, client_key, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->get_client_name_by_key_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **client_key** | **str**| clientKey | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

