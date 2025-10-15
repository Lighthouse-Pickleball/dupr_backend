# dupr_backend.PlayersApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_rating_history_overtime**](PlayersApi.md#get_player_rating_history_overtime) | **POST** /player/{version}/{id}/rating-history | 
[**get_statistics1**](PlayersApi.md#get_statistics1) | **GET** /player/{version}/stats/{id} | 
[**invite**](PlayersApi.md#invite) | **POST** /player/{version}/invite | 
[**match_history**](PlayersApi.md#match_history) | **GET** /player/{version}/{id}/history | 
[**match_history_by_filters**](PlayersApi.md#match_history_by_filters) | **POST** /player/{version}/{id}/history | 
[**player_info**](PlayersApi.md#player_info) | **GET** /player/{version}/{id} | 
[**player_info_by_dupr_id**](PlayersApi.md#player_info_by_dupr_id) | **POST** /player/search/byDuprId | 
[**public_search**](PlayersApi.md#public_search) | **POST** /player/{version}/search/public | 
[**search**](PlayersApi.md#search) | **POST** /player/{version}/search | 
[**search_claim_player**](PlayersApi.md#search_claim_player) | **POST** /player/{version}/claim | 
[**unclaimed_player**](PlayersApi.md#unclaimed_player) | **GET** /player/{version}/claim/{id} | 
[**unclaimed_player_details**](PlayersApi.md#unclaimed_player_details) | **POST** /player/{version}/claim/details | 


# **get_player_rating_history_overtime**
> SingleWrapperPlayerRatingOvertime get_player_rating_history_overtime(version, id, player_rating_history_overtime_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.player_rating_history_overtime_request import PlayerRatingHistoryOvertimeRequest
from dupr_backend.models.single_wrapper_player_rating_overtime import SingleWrapperPlayerRatingOvertime
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    player_rating_history_overtime_request = dupr_backend.PlayerRatingHistoryOvertimeRequest() # PlayerRatingHistoryOvertimeRequest | 

    try:
        api_response = api_instance.get_player_rating_history_overtime(version, id, player_rating_history_overtime_request)
        print("The response of PlayersApi->get_player_rating_history_overtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player_rating_history_overtime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **player_rating_history_overtime_request** | [**PlayerRatingHistoryOvertimeRequest**](PlayerRatingHistoryOvertimeRequest.md)|  | 

### Return type

[**SingleWrapperPlayerRatingOvertime**](SingleWrapperPlayerRatingOvertime.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics1**
> SingleWrapperUserStatisticResponse get_statistics1(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_user_statistic_response import SingleWrapperUserStatisticResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.get_statistics1(version, id)
        print("The response of PlayersApi->get_statistics1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_statistics1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperUserStatisticResponse**](SingleWrapperUserStatisticResponse.md)

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

# **invite**
> SingleWrapperPlayerResponse invite(version, invite_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.invite_request import InviteRequest
from dupr_backend.models.single_wrapper_player_response import SingleWrapperPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    invite_request = dupr_backend.InviteRequest() # InviteRequest | 

    try:
        api_response = api_instance.invite(version, invite_request)
        print("The response of PlayersApi->invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **invite_request** | [**InviteRequest**](InviteRequest.md)|  | 

### Return type

[**SingleWrapperPlayerResponse**](SingleWrapperPlayerResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_history**
> SingleWrapperPageMatchResponse match_history(version, id, offset, limit)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_match_response import SingleWrapperPageMatchResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    offset = 56 # int | 
    limit = 56 # int | 

    try:
        api_response = api_instance.match_history(version, id, offset, limit)
        print("The response of PlayersApi->match_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->match_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 

### Return type

[**SingleWrapperPageMatchResponse**](SingleWrapperPageMatchResponse.md)

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

# **match_history_by_filters**
> SingleWrapperPageMatchResponse match_history_by_filters(version, id, match_search_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.match_search_request import MatchSearchRequest
from dupr_backend.models.single_wrapper_page_match_response import SingleWrapperPageMatchResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    match_search_request = dupr_backend.MatchSearchRequest() # MatchSearchRequest | 

    try:
        api_response = api_instance.match_history_by_filters(version, id, match_search_request)
        print("The response of PlayersApi->match_history_by_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->match_history_by_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **match_search_request** | [**MatchSearchRequest**](MatchSearchRequest.md)|  | 

### Return type

[**SingleWrapperPageMatchResponse**](SingleWrapperPageMatchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_info**
> SingleWrapperPlayerResponse player_info(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_player_response import SingleWrapperPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.player_info(version, id)
        print("The response of PlayersApi->player_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->player_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperPlayerResponse**](SingleWrapperPlayerResponse.md)

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

# **player_info_by_dupr_id**
> ResultUserByDuprIdResponse player_info_by_dupr_id(user_by_dupr_id_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.result_user_by_dupr_id_response import ResultUserByDuprIdResponse
from dupr_backend.models.user_by_dupr_id_request import UserByDuprIdRequest
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
    api_instance = dupr_backend.PlayersApi(api_client)
    user_by_dupr_id_request = dupr_backend.UserByDuprIdRequest() # UserByDuprIdRequest | 

    try:
        api_response = api_instance.player_info_by_dupr_id(user_by_dupr_id_request)
        print("The response of PlayersApi->player_info_by_dupr_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->player_info_by_dupr_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_by_dupr_id_request** | [**UserByDuprIdRequest**](UserByDuprIdRequest.md)|  | 

### Return type

[**ResultUserByDuprIdResponse**](ResultUserByDuprIdResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_search**
> SingleWrapperPagePlayerResponse public_search(version, search_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.search_request import SearchRequest
from dupr_backend.models.single_wrapper_page_player_response import SingleWrapperPagePlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    search_request = dupr_backend.SearchRequest() # SearchRequest | 

    try:
        api_response = api_instance.public_search(version, search_request)
        print("The response of PlayersApi->public_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->public_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**SingleWrapperPagePlayerResponse**](SingleWrapperPagePlayerResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SingleWrapperPagePlayerResponse search(version, search_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.search_request import SearchRequest
from dupr_backend.models.single_wrapper_page_player_response import SingleWrapperPagePlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    search_request = dupr_backend.SearchRequest() # SearchRequest | 

    try:
        api_response = api_instance.search(version, search_request)
        print("The response of PlayersApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**SingleWrapperPagePlayerResponse**](SingleWrapperPagePlayerResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_claim_player**
> SingleWrapperPageUnclaimedPlayerResponse search_claim_player(version, claim_player_search_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.claim_player_search_request import ClaimPlayerSearchRequest
from dupr_backend.models.single_wrapper_page_unclaimed_player_response import SingleWrapperPageUnclaimedPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    claim_player_search_request = dupr_backend.ClaimPlayerSearchRequest() # ClaimPlayerSearchRequest | 

    try:
        api_response = api_instance.search_claim_player(version, claim_player_search_request)
        print("The response of PlayersApi->search_claim_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->search_claim_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **claim_player_search_request** | [**ClaimPlayerSearchRequest**](ClaimPlayerSearchRequest.md)|  | 

### Return type

[**SingleWrapperPageUnclaimedPlayerResponse**](SingleWrapperPageUnclaimedPlayerResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unclaimed_player**
> SingleWrapperUnclaimedPlayerResponse unclaimed_player(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unclaimed_player_response import SingleWrapperUnclaimedPlayerResponse
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.unclaimed_player(version, id)
        print("The response of PlayersApi->unclaimed_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->unclaimed_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperUnclaimedPlayerResponse**](SingleWrapperUnclaimedPlayerResponse.md)

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

# **unclaimed_player_details**
> ResultUnclaimedPlayerDetailsResponse unclaimed_player_details(version, unclaimed_player_details_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.result_unclaimed_player_details_response import ResultUnclaimedPlayerDetailsResponse
from dupr_backend.models.unclaimed_player_details_request import UnclaimedPlayerDetailsRequest
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
    api_instance = dupr_backend.PlayersApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    unclaimed_player_details_request = dupr_backend.UnclaimedPlayerDetailsRequest() # UnclaimedPlayerDetailsRequest | 

    try:
        api_response = api_instance.unclaimed_player_details(version, unclaimed_player_details_request)
        print("The response of PlayersApi->unclaimed_player_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->unclaimed_player_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **unclaimed_player_details_request** | [**UnclaimedPlayerDetailsRequest**](UnclaimedPlayerDetailsRequest.md)|  | 

### Return type

[**ResultUnclaimedPlayerDetailsResponse**](ResultUnclaimedPlayerDetailsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

