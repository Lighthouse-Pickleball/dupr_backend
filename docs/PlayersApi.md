# dupr_backend.PlayersApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_rating_history_overtime_using_post**](PlayersApi.md#get_player_rating_history_overtime_using_post) | **POST** /player/{version}/{id}/rating-history | getPlayerRatingHistoryOvertime
[**get_statistics_using_get**](PlayersApi.md#get_statistics_using_get) | **GET** /player/{version}/stats/{id} | getStatistics
[**invite_using_post**](PlayersApi.md#invite_using_post) | **POST** /player/{version}/invite | invite
[**match_history_by_filters_using_post**](PlayersApi.md#match_history_by_filters_using_post) | **POST** /player/{version}/{id}/history | matchHistoryByFilters
[**match_history_using_get**](PlayersApi.md#match_history_using_get) | **GET** /player/{version}/{id}/history | matchHistory
[**player_info_using_get**](PlayersApi.md#player_info_using_get) | **GET** /player/{version}/{id} | playerInfo
[**public_search_using_post**](PlayersApi.md#public_search_using_post) | **POST** /player/{version}/search/public | publicSearch
[**search_claim_player_using_post**](PlayersApi.md#search_claim_player_using_post) | **POST** /player/{version}/claim | searchClaimPlayer
[**search_using_post**](PlayersApi.md#search_using_post) | **POST** /player/{version}/search | search
[**unclaimed_player_using_get**](PlayersApi.md#unclaimed_player_using_get) | **GET** /player/{version}/claim/{id} | unclaimedPlayer


# **get_player_rating_history_overtime_using_post**
> SingleWrapperOfPlayerRatingOvertime get_player_rating_history_overtime_using_post(authorization, id, version, request)

getPlayerRatingHistoryOvertime

### Example


```python
import dupr_backend
from dupr_backend.models.player_rating_history_overtime_request import PlayerRatingHistoryOvertimeRequest
from dupr_backend.models.single_wrapper_of_player_rating_overtime import SingleWrapperOfPlayerRatingOvertime
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
    api_instance = dupr_backend.PlayersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PlayerRatingHistoryOvertimeRequest() # PlayerRatingHistoryOvertimeRequest | request

    try:
        # getPlayerRatingHistoryOvertime
        api_response = api_instance.get_player_rating_history_overtime_using_post(authorization, id, version, request)
        print("The response of PlayersApi->get_player_rating_history_overtime_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player_rating_history_overtime_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**PlayerRatingHistoryOvertimeRequest**](PlayerRatingHistoryOvertimeRequest.md)| request | 

### Return type

[**SingleWrapperOfPlayerRatingOvertime**](SingleWrapperOfPlayerRatingOvertime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_using_get**
> SingleWrapperOfUserStatisticResponse get_statistics_using_get(authorization, id, version)

getStatistics

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_user_statistic_response import SingleWrapperOfUserStatisticResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getStatistics
        api_response = api_instance.get_statistics_using_get(authorization, id, version)
        print("The response of PlayersApi->get_statistics_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_statistics_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUserStatisticResponse**](SingleWrapperOfUserStatisticResponse.md)

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

# **invite_using_post**
> SingleWrapperOfPlayerResponse invite_using_post(authorization, version, request)

invite

### Example


```python
import dupr_backend
from dupr_backend.models.invite_request import InviteRequest
from dupr_backend.models.single_wrapper_of_player_response import SingleWrapperOfPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.InviteRequest() # InviteRequest | request

    try:
        # invite
        api_response = api_instance.invite_using_post(authorization, version, request)
        print("The response of PlayersApi->invite_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->invite_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**InviteRequest**](InviteRequest.md)| request | 

### Return type

[**SingleWrapperOfPlayerResponse**](SingleWrapperOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_history_by_filters_using_post**
> SingleWrapperOfPageOfMatchResponse match_history_by_filters_using_post(authorization, id, version, request)

matchHistoryByFilters

### Example


```python
import dupr_backend
from dupr_backend.models.match_search_request import MatchSearchRequest
from dupr_backend.models.single_wrapper_of_page_of_match_response import SingleWrapperOfPageOfMatchResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MatchSearchRequest() # MatchSearchRequest | request

    try:
        # matchHistoryByFilters
        api_response = api_instance.match_history_by_filters_using_post(authorization, id, version, request)
        print("The response of PlayersApi->match_history_by_filters_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->match_history_by_filters_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MatchSearchRequest**](MatchSearchRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_history_using_get**
> SingleWrapperOfPageOfMatchResponse match_history_using_get(authorization, id, limit, offset, version)

matchHistory

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_match_response import SingleWrapperOfPageOfMatchResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # matchHistory
        api_response = api_instance.match_history_using_get(authorization, id, limit, offset, version)
        print("The response of PlayersApi->match_history_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->match_history_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

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

# **player_info_using_get**
> SingleWrapperOfPlayerResponse player_info_using_get(authorization, id, version)

playerInfo

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_player_response import SingleWrapperOfPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # playerInfo
        api_response = api_instance.player_info_using_get(authorization, id, version)
        print("The response of PlayersApi->player_info_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->player_info_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPlayerResponse**](SingleWrapperOfPlayerResponse.md)

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

# **public_search_using_post**
> SingleWrapperOfPageOfPlayerResponse public_search_using_post(version, request)

publicSearch

### Example


```python
import dupr_backend
from dupr_backend.models.search_request import SearchRequest
from dupr_backend.models.single_wrapper_of_page_of_player_response import SingleWrapperOfPageOfPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.SearchRequest() # SearchRequest | request

    try:
        # publicSearch
        api_response = api_instance.public_search_using_post(version, request)
        print("The response of PlayersApi->public_search_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->public_search_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**SearchRequest**](SearchRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_claim_player_using_post**
> SingleWrapperOfPageOfUnclaimedPlayerResponse search_claim_player_using_post(version, request)

searchClaimPlayer

### Example


```python
import dupr_backend
from dupr_backend.models.claim_player_search_request import ClaimPlayerSearchRequest
from dupr_backend.models.single_wrapper_of_page_of_unclaimed_player_response import SingleWrapperOfPageOfUnclaimedPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClaimPlayerSearchRequest() # ClaimPlayerSearchRequest | request

    try:
        # searchClaimPlayer
        api_response = api_instance.search_claim_player_using_post(version, request)
        print("The response of PlayersApi->search_claim_player_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->search_claim_player_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClaimPlayerSearchRequest**](ClaimPlayerSearchRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfUnclaimedPlayerResponse**](SingleWrapperOfPageOfUnclaimedPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_using_post**
> SingleWrapperOfPageOfPlayerResponse search_using_post(authorization, version, request)

search

### Example


```python
import dupr_backend
from dupr_backend.models.search_request import SearchRequest
from dupr_backend.models.single_wrapper_of_page_of_player_response import SingleWrapperOfPageOfPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.SearchRequest() # SearchRequest | request

    try:
        # search
        api_response = api_instance.search_using_post(authorization, version, request)
        print("The response of PlayersApi->search_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->search_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**SearchRequest**](SearchRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unclaimed_player_using_get**
> SingleWrapperOfUnclaimedPlayerResponse unclaimed_player_using_get(id, version)

unclaimedPlayer

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_unclaimed_player_response import SingleWrapperOfUnclaimedPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # unclaimedPlayer
        api_response = api_instance.unclaimed_player_using_get(id, version)
        print("The response of PlayersApi->unclaimed_player_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->unclaimed_player_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnclaimedPlayerResponse**](SingleWrapperOfUnclaimedPlayerResponse.md)

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

