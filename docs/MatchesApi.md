# dupr_backend.MatchesApi

All URIs are relative to *//https://backend.mydupr.com/*

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
> Wrapper confirm_match_using_post1(body, authorization, version)

confirmMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
body = dupr_backend.MatchConfirmRequest() # MatchConfirmRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # confirmMatch
    api_response = api_instance.confirm_match_using_post1(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->confirm_match_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchConfirmRequest**](MatchConfirmRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_match_using_delete**
> Wrapper delete_match_using_delete(authorization, id, version)

deleteMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # deleteMatch
    api_response = api_instance.delete_match_using_delete(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->delete_match_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dupr_performance_data_user_using_get**
> ArrayWrapperOfobject get_dupr_performance_data_user_using_get(authorization, id, version)

getDuprPerformanceDataUser

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getDuprPerformanceDataUser
    api_response = api_instance.get_dupr_performance_data_user_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->get_dupr_performance_data_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfobject**](ArrayWrapperOfobject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dupr_performance_data_using_get**
> ArrayWrapperOfobject get_dupr_performance_data_using_get(authorization, version)

getDuprPerformanceData

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getDuprPerformanceData
    api_response = api_instance.get_dupr_performance_data_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->get_dupr_performance_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfobject**](ArrayWrapperOfobject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match_rating_simulator_using_post**
> SingleWrapperOfMatchRatingSimulatorResponse get_match_rating_simulator_using_post(body, version, x_forwarded_for=x_forwarded_for)

getMatchRatingSimulator

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
body = dupr_backend.MatchRatingSimulatorRequest() # MatchRatingSimulatorRequest | request
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # getMatchRatingSimulator
    api_response = api_instance.get_match_rating_simulator_using_post(body, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->get_match_rating_simulator_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchRatingSimulatorRequest**](MatchRatingSimulatorRequest.md)| request | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfMatchRatingSimulatorResponse**](SingleWrapperOfMatchRatingSimulatorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_match_history_using_get**
> SingleWrapperOfPageOfMatchResponse get_user_match_history_using_get(id, limit, offset, version, x_forwarded_for=x_forwarded_for)

getUserMatchHistory

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
id = 789 # int | id
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # getUserMatchHistory
    api_response = api_instance.get_user_match_history_using_get(id, limit, offset, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->get_user_match_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_details_using_get**
> SingleWrapperOfMatchResponse match_details_using_get(authorization, id)

matchDetails

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id

try:
    # matchDetails
    api_response = api_instance.match_details_using_get(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->match_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 

### Return type

[**SingleWrapperOfMatchResponse**](SingleWrapperOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pending_match_details_using_get**
> ArrayWrapperOflong pending_match_details_using_get(authorization, version)

pendingMatchDetails

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # pendingMatchDetails
    api_response = api_instance.pending_match_details_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->pending_match_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOflong**](ArrayWrapperOflong.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_match_using_put**
> SingleWrapperOflong save_match_using_put(body, authorization, version)

saveMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
body = dupr_backend.MatchRequest() # MatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # saveMatch
    api_response = api_instance.save_match_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->save_match_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchRequest**](MatchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOflong**](SingleWrapperOflong.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_verified_match_cvs_using_put**
> Wrapper save_verified_match_cvs_using_put(authorization, version, request=request)

saveVerifiedMatchCVS

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
request = 'request_example' # str |  (optional)

try:
    # saveVerifiedMatchCVS
    api_response = api_instance.save_verified_match_cvs_using_put(authorization, version, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->save_verified_match_cvs_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **request** | **str**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_verified_match_using_put1**
> Wrapper save_verified_match_using_put1(body, authorization, version)

saveVerifiedMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
body = dupr_backend.VerifiedMatchRequest() # VerifiedMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # saveVerifiedMatch
    api_response = api_instance.save_verified_match_using_put1(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->save_verified_match_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifiedMatchRequest**](VerifiedMatchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **score_formats_using_get**
> ArrayWrapperOfScoreFormatResponse score_formats_using_get(authorization, version)

scoreFormats

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # scoreFormats
    api_response = api_instance.score_formats_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->score_formats_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfScoreFormatResponse**](ArrayWrapperOfScoreFormatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_match_using_post**
> SingleWrapperOfPostResponse share_match_using_post(body, authorization, id, version)

shareMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
body = dupr_backend.ShareMatchRequest() # ShareMatchRequest | shareRequest
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # shareMatch
    api_response = api_instance.share_match_using_post(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->share_match_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShareMatchRequest**](ShareMatchRequest.md)| shareRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPostResponse**](SingleWrapperOfPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_match_history_by_filters_using_post**
> SingleWrapperOfPageOfMatchResponse user_match_history_by_filters_using_post(body, authorization, version)

userMatchHistoryByFilters

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
body = dupr_backend.MatchSearchRequest() # MatchSearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # userMatchHistoryByFilters
    api_response = api_instance.user_match_history_by_filters_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->user_match_history_by_filters_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchSearchRequest**](MatchSearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_match_history_using_get**
> SingleWrapperOfPageOfMatchResponse user_match_history_using_get(authorization, limit, offset, version)

userMatchHistory

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MatchesApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # userMatchHistory
    api_response = api_instance.user_match_history_using_get(authorization, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->user_match_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
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

