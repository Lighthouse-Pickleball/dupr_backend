# dupr_backend.MatchesApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_match**](MatchesApi.md#confirm_match) | **POST** /match/{version}/confirm | 
[**delete_match1**](MatchesApi.md#delete_match1) | **DELETE** /match/{version}/delete/{id} | 
[**get_dupr_performance_data**](MatchesApi.md#get_dupr_performance_data) | **GET** /match/{version}/performance | 
[**get_dupr_performance_data_user**](MatchesApi.md#get_dupr_performance_data_user) | **GET** /match/{version}/performance/{id} | 
[**get_match_expected_score**](MatchesApi.md#get_match_expected_score) | **POST** /match/{version}/expected-score | 
[**get_match_rating_simulator**](MatchesApi.md#get_match_rating_simulator) | **POST** /match/{version}/rating-simulator | 
[**get_user_match_history**](MatchesApi.md#get_user_match_history) | **GET** /match/{version}/history/unauthenticated/{id} | 
[**match_details**](MatchesApi.md#match_details) | **GET** /match/{id} | 
[**pending_match_details**](MatchesApi.md#pending_match_details) | **GET** /match/{version}/pending | 
[**save_match**](MatchesApi.md#save_match) | **PUT** /match/{version}/save | 
[**save_verified_match**](MatchesApi.md#save_verified_match) | **PUT** /match/verified/{version}/save | 
[**save_verified_match_cvs**](MatchesApi.md#save_verified_match_cvs) | **PUT** /match/verified/{version}/save/csv/add | 
[**score_formats**](MatchesApi.md#score_formats) | **GET** /match/{version}/score/formats | 
[**share_match**](MatchesApi.md#share_match) | **POST** /match/{version}/share/{id}/newsfeed | 
[**user_match_history**](MatchesApi.md#user_match_history) | **GET** /match/{version}/history | 
[**user_match_history_by_filters**](MatchesApi.md#user_match_history_by_filters) | **POST** /match/{version}/history | 


# **confirm_match**
> Wrapper confirm_match(version, match_confirm_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.match_confirm_request import MatchConfirmRequest
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    match_confirm_request = dupr_backend.MatchConfirmRequest() # MatchConfirmRequest | 

    try:
        api_response = api_instance.confirm_match(version, match_confirm_request)
        print("The response of MatchesApi->confirm_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->confirm_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **match_confirm_request** | [**MatchConfirmRequest**](MatchConfirmRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **delete_match1**
> Wrapper delete_match1(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.delete_match1(version, id)
        print("The response of MatchesApi->delete_match1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->delete_match1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **get_dupr_performance_data**
> ArrayWrapperObject get_dupr_performance_data(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_object import ArrayWrapperObject
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.get_dupr_performance_data(version)
        print("The response of MatchesApi->get_dupr_performance_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_dupr_performance_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperObject**](ArrayWrapperObject.md)

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

# **get_dupr_performance_data_user**
> ArrayWrapperObject get_dupr_performance_data_user(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_object import ArrayWrapperObject
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.get_dupr_performance_data_user(version, id)
        print("The response of MatchesApi->get_dupr_performance_data_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_dupr_performance_data_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**ArrayWrapperObject**](ArrayWrapperObject.md)

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

# **get_match_expected_score**
> MatchExpectedScoreResponse get_match_expected_score(version, match_expected_score_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.match_expected_score_request import MatchExpectedScoreRequest
from dupr_backend.models.match_expected_score_response import MatchExpectedScoreResponse
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    match_expected_score_request = dupr_backend.MatchExpectedScoreRequest() # MatchExpectedScoreRequest | 

    try:
        api_response = api_instance.get_match_expected_score(version, match_expected_score_request)
        print("The response of MatchesApi->get_match_expected_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_match_expected_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **match_expected_score_request** | [**MatchExpectedScoreRequest**](MatchExpectedScoreRequest.md)|  | 

### Return type

[**MatchExpectedScoreResponse**](MatchExpectedScoreResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match_rating_simulator**
> object get_match_rating_simulator(version, match_rating_simulator_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.match_rating_simulator_request import MatchRatingSimulatorRequest
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    match_rating_simulator_request = dupr_backend.MatchRatingSimulatorRequest() # MatchRatingSimulatorRequest | 

    try:
        api_response = api_instance.get_match_rating_simulator(version, match_rating_simulator_request)
        print("The response of MatchesApi->get_match_rating_simulator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_match_rating_simulator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **match_rating_simulator_request** | [**MatchRatingSimulatorRequest**](MatchRatingSimulatorRequest.md)|  | 

### Return type

**object**

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

# **get_user_match_history**
> SingleWrapperPageMatchResponse get_user_match_history(version, id, offset, limit)

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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    offset = 56 # int | 
    limit = 56 # int | 

    try:
        api_response = api_instance.get_user_match_history(version, id, offset, limit)
        print("The response of MatchesApi->get_user_match_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->get_user_match_history: %s\n" % e)
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

# **match_details**
> SingleWrapperMatchResponse match_details(id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_match_response import SingleWrapperMatchResponse
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
    api_instance = dupr_backend.MatchesApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.match_details(id)
        print("The response of MatchesApi->match_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->match_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SingleWrapperMatchResponse**](SingleWrapperMatchResponse.md)

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

# **pending_match_details**
> ArrayWrapperLong pending_match_details(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_long import ArrayWrapperLong
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.pending_match_details(version)
        print("The response of MatchesApi->pending_match_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->pending_match_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperLong**](ArrayWrapperLong.md)

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

# **save_match**
> SingleWrapperLong save_match(version, match_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.match_request import MatchRequest
from dupr_backend.models.single_wrapper_long import SingleWrapperLong
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    match_request = dupr_backend.MatchRequest() # MatchRequest | 

    try:
        api_response = api_instance.save_match(version, match_request)
        print("The response of MatchesApi->save_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->save_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **match_request** | [**MatchRequest**](MatchRequest.md)|  | 

### Return type

[**SingleWrapperLong**](SingleWrapperLong.md)

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

# **save_verified_match**
> Wrapper save_verified_match(version, verified_match_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.verified_match_request import VerifiedMatchRequest
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    verified_match_request = dupr_backend.VerifiedMatchRequest() # VerifiedMatchRequest | 

    try:
        api_response = api_instance.save_verified_match(version, verified_match_request)
        print("The response of MatchesApi->save_verified_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->save_verified_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **verified_match_request** | [**VerifiedMatchRequest**](VerifiedMatchRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **save_verified_match_cvs**
> Wrapper save_verified_match_cvs(version, request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    request = None # bytearray | 

    try:
        api_response = api_instance.save_verified_match_cvs(version, request)
        print("The response of MatchesApi->save_verified_match_cvs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->save_verified_match_cvs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **request** | **bytearray**|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **score_formats**
> ArrayWrapperScoreFormatResponse score_formats(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_score_format_response import ArrayWrapperScoreFormatResponse
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.score_formats(version)
        print("The response of MatchesApi->score_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->score_formats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperScoreFormatResponse**](ArrayWrapperScoreFormatResponse.md)

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

# **share_match**
> SingleWrapperPostResponse share_match(version, id, share_match_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.share_match_request import ShareMatchRequest
from dupr_backend.models.single_wrapper_post_response import SingleWrapperPostResponse
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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    share_match_request = dupr_backend.ShareMatchRequest() # ShareMatchRequest | 

    try:
        api_response = api_instance.share_match(version, id, share_match_request)
        print("The response of MatchesApi->share_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->share_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **share_match_request** | [**ShareMatchRequest**](ShareMatchRequest.md)|  | 

### Return type

[**SingleWrapperPostResponse**](SingleWrapperPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_match_history**
> SingleWrapperPageMatchResponse user_match_history(version, offset, limit)

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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    offset = 56 # int | 
    limit = 56 # int | 

    try:
        api_response = api_instance.user_match_history(version, offset, limit)
        print("The response of MatchesApi->user_match_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->user_match_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
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

# **user_match_history_by_filters**
> SingleWrapperPageMatchResponse user_match_history_by_filters(version, match_search_request)

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
    api_instance = dupr_backend.MatchesApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    match_search_request = dupr_backend.MatchSearchRequest() # MatchSearchRequest | 

    try:
        api_response = api_instance.user_match_history_by_filters(version, match_search_request)
        print("The response of MatchesApi->user_match_history_by_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MatchesApi->user_match_history_by_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
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

