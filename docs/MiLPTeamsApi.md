# dupr_backend.MiLPTeamsApi

All URIs are relative to *https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_using_post3**](MiLPTeamsApi.md#save_using_post3) | **POST** /milp/teams/{version}/save | save

# **save_using_post3**
> SingleWrapperOfMiLPTeam save_using_post3(body, authorization, version)

save

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MiLPTeamsApi()
body = dupr_backend.MiLPTeamRequest() # MiLPTeamRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # save
    api_response = api_instance.save_using_post3(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiLPTeamsApi->save_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MiLPTeamRequest**](MiLPTeamRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMiLPTeam**](SingleWrapperOfMiLPTeam.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

