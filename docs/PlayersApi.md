# dupr_backend.PlayersApi

All URIs are relative to *//https://backend.mydupr.com/*

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
> SingleWrapperOfPlayerRatingOvertime get_player_rating_history_overtime_using_post(body, authorization, id, version)

getPlayerRatingHistoryOvertime

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
body = dupr_backend.PlayerRatingHistoryOvertimeRequest() # PlayerRatingHistoryOvertimeRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getPlayerRatingHistoryOvertime
    api_response = api_instance.get_player_rating_history_overtime_using_post(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_rating_history_overtime_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayerRatingHistoryOvertimeRequest**](PlayerRatingHistoryOvertimeRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPlayerRatingOvertime**](SingleWrapperOfPlayerRatingOvertime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_using_get**
> SingleWrapperOfUserStatisticResponse get_statistics_using_get(authorization, id, version)

getStatistics

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getStatistics
    api_response = api_instance.get_statistics_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_statistics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUserStatisticResponse**](SingleWrapperOfUserStatisticResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_using_post**
> SingleWrapperOfPlayerResponse invite_using_post(body, authorization, version)

invite

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
body = dupr_backend.InviteRequest() # InviteRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # invite
    api_response = api_instance.invite_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->invite_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InviteRequest**](InviteRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPlayerResponse**](SingleWrapperOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_history_by_filters_using_post**
> SingleWrapperOfPageOfMatchResponse match_history_by_filters_using_post(body, authorization, id, version)

matchHistoryByFilters

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
body = dupr_backend.MatchSearchRequest() # MatchSearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # matchHistoryByFilters
    api_response = api_instance.match_history_by_filters_using_post(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->match_history_by_filters_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchSearchRequest**](MatchSearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_history_using_get**
> SingleWrapperOfPageOfMatchResponse match_history_using_get(authorization, id, limit, offset, version)

matchHistory

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # matchHistory
    api_response = api_instance.match_history_using_get(authorization, id, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->match_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_info_using_get**
> SingleWrapperOfPlayerResponse player_info_using_get(authorization, id, version)

playerInfo

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # playerInfo
    api_response = api_instance.player_info_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->player_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPlayerResponse**](SingleWrapperOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_search_using_post**
> SingleWrapperOfPageOfPlayerResponse public_search_using_post(body, version)

publicSearch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
body = dupr_backend.SearchRequest() # SearchRequest | request
version = 'version_example' # str | version

try:
    # publicSearch
    api_response = api_instance.public_search_using_post(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->public_search_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| request | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_claim_player_using_post**
> SingleWrapperOfPageOfUnclaimedPlayerResponse search_claim_player_using_post(body, version)

searchClaimPlayer

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
body = dupr_backend.ClaimPlayerSearchRequest() # ClaimPlayerSearchRequest | request
version = 'version_example' # str | version

try:
    # searchClaimPlayer
    api_response = api_instance.search_claim_player_using_post(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->search_claim_player_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClaimPlayerSearchRequest**](ClaimPlayerSearchRequest.md)| request | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfUnclaimedPlayerResponse**](SingleWrapperOfPageOfUnclaimedPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_using_post**
> SingleWrapperOfPageOfPlayerResponse search_using_post(body, authorization, version)

search

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
body = dupr_backend.SearchRequest() # SearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # search
    api_response = api_instance.search_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->search_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unclaimed_player_using_get**
> SingleWrapperOfUnclaimedPlayerResponse unclaimed_player_using_get(id, version)

unclaimedPlayer

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PlayersApi()
id = 789 # int | id
version = 'version_example' # str | version

try:
    # unclaimedPlayer
    api_response = api_instance.unclaimed_player_using_get(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->unclaimed_player_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnclaimedPlayerResponse**](SingleWrapperOfUnclaimedPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

