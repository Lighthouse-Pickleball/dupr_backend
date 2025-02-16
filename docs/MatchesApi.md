# dupr_backend.MatchesApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_match_using_post1**](MatchesApi.md#confirm_match_using_post1) | **POST** /match/{version}/confirm | confirmMatch
[**delete_match_using_delete**](MatchesApi.md#delete_match_using_delete) | **DELETE** /match/{version}/delete/{id} | deleteMatch
[**get_dupr_performance_data_user_using_get**](MatchesApi.md#get_dupr_performance_data_user_using_get) | **GET** /match/{version}/performance/{id} | getDuprPerformanceDataUser
[**get_dupr_performance_data_using_get**](MatchesApi.md#get_dupr_performance_data_using_get) | **GET** /match/{version}/performance | getDuprPerformanceData
[**get_match_rating_simulator_using_post**](MatchesApi.md#get_match_rating_simulator_using_post) | **POST** /match/{version}/rating-simulator | getMatchRatingSimulator
[**get_user_match_history_using_get**](MatchesApi.md#get_user_match_history_using_get) | **GET** /match/{version}/history/unauthenticated/{id} | getUserMatchHistory
[**match_details_using_get**](MatchesApi.md#match_details_using_get) | **GET** /match/{id} | matchDetails
[**pending_match_details_using_get**](MatchesApi.md#pending_match_details_using_get) | **GET** /match/{version}/pending | pendingMatchDetails
[**save_match_using_put**](MatchesApi.md#save_match_using_put) | **PUT** /match/{version}/save | saveMatch
[**save_verified_match_cvs_using_put**](MatchesApi.md#save_verified_match_cvs_using_put) | **PUT** /match/verified/{version}/save/csv/add | saveVerifiedMatchCVS
[**save_verified_match_using_put1**](MatchesApi.md#save_verified_match_using_put1) | **PUT** /match/verified/{version}/save | saveVerifiedMatch
[**score_formats_using_get**](MatchesApi.md#score_formats_using_get) | **GET** /match/{version}/score/formats | scoreFormats
[**share_match_using_post**](MatchesApi.md#share_match_using_post) | **POST** /match/{version}/share/{id}/newsfeed | shareMatch
[**user_match_history_by_filters_using_post**](MatchesApi.md#user_match_history_by_filters_using_post) | **POST** /match/{version}/history | userMatchHistoryByFilters
[**user_match_history_using_get**](MatchesApi.md#user_match_history_using_get) | **GET** /match/{version}/history | userMatchHistory


# **confirm_match_using_post1**
> Wrapper confirm_match_using_post1(authorization, version, request)

confirmMatch

### Example


```python
import dupr_backend
from dupr_backend.models.match_confirm_request import MatchConfirmRequest
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MatchConfirmRequest() # MatchConfirmRequest | request

    try:
        # confirmMatch
        api_response = api_instance.confirm_match_using_post1(authorization, version, request)
        print("The response of MatchesApi->confirm_match_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->confirm_match_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MatchConfirmRequest**](MatchConfirmRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **delete_match_using_delete**
> Wrapper delete_match_using_delete(authorization, id, version)

deleteMatch

### Example


```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteMatch
        api_response = api_instance.delete_match_using_delete(authorization, id, version)
        print("The response of MatchesApi->delete_match_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->delete_match_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **get_dupr_performance_data_user_using_get**
> ArrayWrapperOfobject get_dupr_performance_data_user_using_get(authorization, id, version)

getDuprPerformanceDataUser

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_ofobject import ArrayWrapperOfobject
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.2' # str | version (default to 'v1.2')

    try:
        # getDuprPerformanceDataUser
        api_response = api_instance.get_dupr_performance_data_user_using_get(authorization, id, version)
        print("The response of MatchesApi->get_dupr_performance_data_user_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_dupr_performance_data_user_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.2&#39;]

### Return type

[**ArrayWrapperOfobject**](ArrayWrapperOfobject.md)

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

# **get_dupr_performance_data_using_get**
> ArrayWrapperOfobject get_dupr_performance_data_using_get(authorization, version)

getDuprPerformanceData

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_ofobject import ArrayWrapperOfobject
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.2' # str | version (default to 'v1.2')

    try:
        # getDuprPerformanceData
        api_response = api_instance.get_dupr_performance_data_using_get(authorization, version)
        print("The response of MatchesApi->get_dupr_performance_data_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_dupr_performance_data_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.2&#39;]

### Return type

[**ArrayWrapperOfobject**](ArrayWrapperOfobject.md)

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

# **get_match_rating_simulator_using_post**
> SingleWrapperOfMatchRatingSimulatorResponse get_match_rating_simulator_using_post(version, request, x_forwarded_for=x_forwarded_for)

getMatchRatingSimulator

### Example


```python
import dupr_backend
from dupr_backend.models.match_rating_simulator_request import MatchRatingSimulatorRequest
from dupr_backend.models.single_wrapper_of_match_rating_simulator_response import SingleWrapperOfMatchRatingSimulatorResponse
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.2' # str | version (default to 'v1.2')
    request = dupr_backend.MatchRatingSimulatorRequest() # MatchRatingSimulatorRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # getMatchRatingSimulator
        api_response = api_instance.get_match_rating_simulator_using_post(version, request, x_forwarded_for=x_forwarded_for)
        print("The response of MatchesApi->get_match_rating_simulator_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_match_rating_simulator_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.2&#39;]
 **request** | [**MatchRatingSimulatorRequest**](MatchRatingSimulatorRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfMatchRatingSimulatorResponse**](SingleWrapperOfMatchRatingSimulatorResponse.md)

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

# **get_user_match_history_using_get**
> SingleWrapperOfPageOfMatchResponse get_user_match_history_using_get(id, limit, offset, version, x_forwarded_for=x_forwarded_for)

getUserMatchHistory

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
    api_instance = dupr_backend.MatchesApi(api_client)
    id = 56 # int | id
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # getUserMatchHistory
        api_response = api_instance.get_user_match_history_using_get(id, limit, offset, version, x_forwarded_for=x_forwarded_for)
        print("The response of MatchesApi->get_user_match_history_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_user_match_history_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

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

# **match_details_using_get**
> SingleWrapperOfMatchResponse match_details_using_get(authorization, id)

matchDetails

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_match_response import SingleWrapperOfMatchResponse
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id

    try:
        # matchDetails
        api_response = api_instance.match_details_using_get(authorization, id)
        print("The response of MatchesApi->match_details_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->match_details_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 

### Return type

[**SingleWrapperOfMatchResponse**](SingleWrapperOfMatchResponse.md)

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

# **pending_match_details_using_get**
> ArrayWrapperOflong pending_match_details_using_get(authorization, version)

pendingMatchDetails

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_oflong import ArrayWrapperOflong
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # pendingMatchDetails
        api_response = api_instance.pending_match_details_using_get(authorization, version)
        print("The response of MatchesApi->pending_match_details_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->pending_match_details_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOflong**](ArrayWrapperOflong.md)

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

# **save_match_using_put**
> SingleWrapperOflong save_match_using_put(authorization, version, request)

saveMatch

### Example


```python
import dupr_backend
from dupr_backend.models.match_request import MatchRequest
from dupr_backend.models.single_wrapper_oflong import SingleWrapperOflong
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MatchRequest() # MatchRequest | request

    try:
        # saveMatch
        api_response = api_instance.save_match_using_put(authorization, version, request)
        print("The response of MatchesApi->save_match_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->save_match_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MatchRequest**](MatchRequest.md)| request | 

### Return type

[**SingleWrapperOflong**](SingleWrapperOflong.md)

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

# **save_verified_match_cvs_using_put**
> Wrapper save_verified_match_cvs_using_put(authorization, version, request=request)

saveVerifiedMatchCVS

### Example


```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = None # bytearray |  (optional)

    try:
        # saveVerifiedMatchCVS
        api_response = api_instance.save_verified_match_cvs_using_put(authorization, version, request=request)
        print("The response of MatchesApi->save_verified_match_cvs_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->save_verified_match_cvs_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | **bytearray**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_verified_match_using_put1**
> Wrapper save_verified_match_using_put1(authorization, version, request)

saveVerifiedMatch

### Example


```python
import dupr_backend
from dupr_backend.models.verified_match_request import VerifiedMatchRequest
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.VerifiedMatchRequest() # VerifiedMatchRequest | request

    try:
        # saveVerifiedMatch
        api_response = api_instance.save_verified_match_using_put1(authorization, version, request)
        print("The response of MatchesApi->save_verified_match_using_put1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->save_verified_match_using_put1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**VerifiedMatchRequest**](VerifiedMatchRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **score_formats_using_get**
> ArrayWrapperOfScoreFormatResponse score_formats_using_get(authorization, version)

scoreFormats

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_score_format_response import ArrayWrapperOfScoreFormatResponse
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # scoreFormats
        api_response = api_instance.score_formats_using_get(authorization, version)
        print("The response of MatchesApi->score_formats_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->score_formats_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfScoreFormatResponse**](ArrayWrapperOfScoreFormatResponse.md)

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

# **share_match_using_post**
> SingleWrapperOfPostResponse share_match_using_post(authorization, id, version, share_request)

shareMatch

### Example


```python
import dupr_backend
from dupr_backend.models.share_match_request import ShareMatchRequest
from dupr_backend.models.single_wrapper_of_post_response import SingleWrapperOfPostResponse
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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    share_request = dupr_backend.ShareMatchRequest() # ShareMatchRequest | shareRequest

    try:
        # shareMatch
        api_response = api_instance.share_match_using_post(authorization, id, version, share_request)
        print("The response of MatchesApi->share_match_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->share_match_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **share_request** | [**ShareMatchRequest**](ShareMatchRequest.md)| shareRequest | 

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_match_history_by_filters_using_post**
> SingleWrapperOfPageOfMatchResponse user_match_history_by_filters_using_post(authorization, version, request)

userMatchHistoryByFilters

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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MatchSearchRequest() # MatchSearchRequest | request

    try:
        # userMatchHistoryByFilters
        api_response = api_instance.user_match_history_by_filters_using_post(authorization, version, request)
        print("The response of MatchesApi->user_match_history_by_filters_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->user_match_history_by_filters_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **user_match_history_using_get**
> SingleWrapperOfPageOfMatchResponse user_match_history_using_get(authorization, limit, offset, version)

userMatchHistory

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
    api_instance = dupr_backend.MatchesApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # userMatchHistory
        api_response = api_instance.user_match_history_using_get(authorization, limit, offset, version)
        print("The response of MatchesApi->user_match_history_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->user_match_history_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

