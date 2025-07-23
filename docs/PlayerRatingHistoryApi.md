# dupr_backend.PlayerRatingHistoryApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_player_rating_history**](PlayerRatingHistoryApi.md#get_all_player_rating_history) | **GET** /player-rating-history/{version}/all | 
[**get_player_rating_history_by_user**](PlayerRatingHistoryApi.md#get_player_rating_history_by_user) | **GET** /player-rating-history/{version} | 


# **get_all_player_rating_history**
> SingleWrapperPagePlayerRatingHistory get_all_player_rating_history(version, offset, limit)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_player_rating_history import SingleWrapperPagePlayerRatingHistory
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.PlayerRatingHistoryApi(api_client)
    version = 'version_example' # str | 
    offset = 56 # int | 
    limit = 56 # int | 

    try:
        api_response = api_instance.get_all_player_rating_history(version, offset, limit)
        print("The response of PlayerRatingHistoryApi->get_all_player_rating_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRatingHistoryApi->get_all_player_rating_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 

### Return type

[**SingleWrapperPagePlayerRatingHistory**](SingleWrapperPagePlayerRatingHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_rating_history_by_user**
> SingleWrapperPagePlayerRatingHistory get_player_rating_history_by_user(version, obfuscated_user_id, offset, limit)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_player_rating_history import SingleWrapperPagePlayerRatingHistory
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.PlayerRatingHistoryApi(api_client)
    version = 'version_example' # str | 
    obfuscated_user_id = 56 # int | 
    offset = 56 # int | 
    limit = 56 # int | 

    try:
        api_response = api_instance.get_player_rating_history_by_user(version, obfuscated_user_id, offset, limit)
        print("The response of PlayerRatingHistoryApi->get_player_rating_history_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayerRatingHistoryApi->get_player_rating_history_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **obfuscated_user_id** | **int**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 

### Return type

[**SingleWrapperPagePlayerRatingHistory**](SingleWrapperPagePlayerRatingHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

