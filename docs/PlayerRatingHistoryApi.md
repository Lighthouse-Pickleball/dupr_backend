# dupr_backend.PlayerRatingHistoryApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_player_rating_history_using_get**](PlayerRatingHistoryApi.md#get_all_player_rating_history_using_get) | **GET** /player-rating-history/{version}/all | getAllPlayerRatingHistory
[**get_player_rating_history_by_user_using_get**](PlayerRatingHistoryApi.md#get_player_rating_history_by_user_using_get) | **GET** /player-rating-history/{version} | getPlayerRatingHistoryByUser


# **get_all_player_rating_history_using_get**
> SingleWrapperOfPageOfPlayerRatingHistory get_all_player_rating_history_using_get(authorization, limit, offset, version)

getAllPlayerRatingHistory

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_player_rating_history import SingleWrapperOfPageOfPlayerRatingHistory
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
    api_instance = dupr_backend.PlayerRatingHistoryApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllPlayerRatingHistory
        api_response = api_instance.get_all_player_rating_history_using_get(authorization, limit, offset, version)
        print("The response of PlayerRatingHistoryApi->get_all_player_rating_history_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRatingHistoryApi->get_all_player_rating_history_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfPlayerRatingHistory**](SingleWrapperOfPageOfPlayerRatingHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_rating_history_by_user_using_get**
> SingleWrapperOfPageOfPlayerRatingHistory get_player_rating_history_by_user_using_get(authorization, limit, obfuscated_user_id, offset, version)

getPlayerRatingHistoryByUser

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_player_rating_history import SingleWrapperOfPageOfPlayerRatingHistory
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
    api_instance = dupr_backend.PlayerRatingHistoryApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    obfuscated_user_id = 56 # int | obfuscatedUserId
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getPlayerRatingHistoryByUser
        api_response = api_instance.get_player_rating_history_by_user_using_get(authorization, limit, obfuscated_user_id, offset, version)
        print("The response of PlayerRatingHistoryApi->get_player_rating_history_by_user_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRatingHistoryApi->get_player_rating_history_by_user_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **obfuscated_user_id** | **int**| obfuscatedUserId | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfPlayerRatingHistory**](SingleWrapperOfPageOfPlayerRatingHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

