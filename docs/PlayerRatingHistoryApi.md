# dupr_backend.PlayerRatingHistoryApi

All URIs are relative to *https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_player_rating_history_using_get**](PlayerRatingHistoryApi.md#get_all_player_rating_history_using_get) | **GET** /player-rating-history/{version}/all | getAllPlayerRatingHistory
[**get_player_rating_history_by_user_using_get**](PlayerRatingHistoryApi.md#get_player_rating_history_by_user_using_get) | **GET** /player-rating-history/{version} | getPlayerRatingHistoryByUser

# **get_all_player_rating_history_using_get**
> SingleWrapperOfPageOfPlayerRatingHistory get_all_player_rating_history_using_get(authorization, limit, offset, version)

getAllPlayerRatingHistory

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayerRatingHistoryApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getAllPlayerRatingHistory
    api_response = api_instance.get_all_player_rating_history_using_get(authorization, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerRatingHistoryApi->get_all_player_rating_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerRatingHistory**](SingleWrapperOfPageOfPlayerRatingHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_rating_history_by_user_using_get**
> SingleWrapperOfPageOfPlayerRatingHistory get_player_rating_history_by_user_using_get(authorization, limit, obfuscated_user_id, offset, version)

getPlayerRatingHistoryByUser

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayerRatingHistoryApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
obfuscated_user_id = 789 # int | obfuscatedUserId
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getPlayerRatingHistoryByUser
    api_response = api_instance.get_player_rating_history_by_user_using_get(authorization, limit, obfuscated_user_id, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayerRatingHistoryApi->get_player_rating_history_by_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **obfuscated_user_id** | **int**| obfuscatedUserId | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerRatingHistory**](SingleWrapperOfPageOfPlayerRatingHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

