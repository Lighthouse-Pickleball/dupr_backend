# dupr_backend.UserApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_using_delete**](UserApi.md#delete_user_using_delete) | **DELETE** /user/{version}/delete | deleteUser
[**delete_using_delete**](UserApi.md#delete_using_delete) | **DELETE** /notifications/history | delete
[**get_calculated_statistics_using_get**](UserApi.md#get_calculated_statistics_using_get) | **GET** /user/calculated/{version}/stats/{id} | getCalculatedStatistics
[**get_profile_using_get**](UserApi.md#get_profile_using_get) | **GET** /user/{version}/profile | getProfile
[**get_rating_using_get**](UserApi.md#get_rating_using_get) | **GET** /user/{version}/rating | getRating
[**get_settings_using_get**](UserApi.md#get_settings_using_get) | **GET** /user/{version}/settings | getSettings
[**get_sponsor_logo_using_get**](UserApi.md#get_sponsor_logo_using_get) | **GET** /user/{version}/sponsor | getSponsorLogo
[**get_statistics_using_get1**](UserApi.md#get_statistics_using_get1) | **GET** /user/{version}/stats | getStatistics
[**get_user_initialization_information_bulk_using_post**](UserApi.md#get_user_initialization_information_bulk_using_post) | **POST** /user/{version}/initialization/bulk | getUserInitializationInformationBulk
[**get_user_initialization_information_using_get**](UserApi.md#get_user_initialization_information_using_get) | **GET** /user/{version}/initialization/{userId} | getUserInitializationInformation
[**get_verfied_statistics_using_get**](UserApi.md#get_verfied_statistics_using_get) | **GET** /user/verified/{version}/stats | getVerfiedStatistics
[**history_using_get**](UserApi.md#history_using_get) | **GET** /notifications/history | history
[**is_sole_director_using_get**](UserApi.md#is_sole_director_using_get) | **GET** /user/{version}/sole_director | isSoleDirector
[**logout_using_post**](UserApi.md#logout_using_post) | **POST** /user/{version}/logout | logout
[**reset_password_using_post**](UserApi.md#reset_password_using_post) | **POST** /user/password/{version}/reset | resetPassword
[**send_email_verification_link_using_post**](UserApi.md#send_email_verification_link_using_post) | **POST** /user/email/verify/{version}/initiate | sendEmailVerificationLink
[**send_phone_otp_using_post**](UserApi.md#send_phone_otp_using_post) | **POST** /user/phone/{version}/resend | sendPhoneOTP
[**send_verification_email_using_post**](UserApi.md#send_verification_email_using_post) | **POST** /user/email/{version}/resend | sendVerificationEmail
[**update_lucra_connection_using_put1**](UserApi.md#update_lucra_connection_using_put1) | **PUT** /user/{version}/lucra-connect | updateLucraConnection
[**update_preferences_using_put**](UserApi.md#update_preferences_using_put) | **PUT** /user/{version}/preferences | updatePreferences
[**update_profile_using_put**](UserApi.md#update_profile_using_put) | **PUT** /user/{version}/profile | updateProfile
[**update_settings_using_put**](UserApi.md#update_settings_using_put) | **PUT** /user/{version}/settings | updateSettings
[**verify_captcha_using_post**](UserApi.md#verify_captcha_using_post) | **POST** /user/open/captcha/{version}/verify | verifyCaptcha
[**verify_email_address_using_post**](UserApi.md#verify_email_address_using_post) | **POST** /user/email/{version}/verify | verifyEmailAddress
[**verify_phone_number_using_post**](UserApi.md#verify_phone_number_using_post) | **POST** /user/phone/{version}/verify | verifyPhoneNumber


# **delete_user_using_delete**
> SingleWrapperOfUnit delete_user_using_delete(authorization, version)

deleteUser

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteUser
        api_response = api_instance.delete_user_using_delete(authorization, version)
        print("The response of UserApi->delete_user_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

# **delete_using_delete**
> int delete_using_delete(authorization, id)

delete

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = ['id_example'] # List[str] | id

    try:
        # delete
        api_response = api_instance.delete_using_delete(authorization, id)
        print("The response of UserApi->delete_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | [**List[str]**](str.md)| id | 

### Return type

**int**

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

# **get_calculated_statistics_using_get**
> SingleWrapperOfPreCalculatedUserStatisticsResponse get_calculated_statistics_using_get(authorization, id, version)

getCalculatedStatistics

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_pre_calculated_user_statistics_response import SingleWrapperOfPreCalculatedUserStatisticsResponse
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getCalculatedStatistics
        api_response = api_instance.get_calculated_statistics_using_get(authorization, id, version)
        print("The response of UserApi->get_calculated_statistics_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_calculated_statistics_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPreCalculatedUserStatisticsResponse**](SingleWrapperOfPreCalculatedUserStatisticsResponse.md)

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

# **get_profile_using_get**
> SingleWrapperOfUserResponse get_profile_using_get(authorization, version)

getProfile

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_user_response import SingleWrapperOfUserResponse
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getProfile
        api_response = api_instance.get_profile_using_get(authorization, version)
        print("The response of UserApi->get_profile_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_profile_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

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

# **get_rating_using_get**
> SingleWrapperOfPlayerRatingResponse get_rating_using_get(authorization, version)

getRating

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_player_rating_response import SingleWrapperOfPlayerRatingResponse
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getRating
        api_response = api_instance.get_rating_using_get(authorization, version)
        print("The response of UserApi->get_rating_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_rating_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPlayerRatingResponse**](SingleWrapperOfPlayerRatingResponse.md)

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

# **get_settings_using_get**
> SingleWrapperOfMapOfstringAndstring get_settings_using_get(authorization, version)

getSettings

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_map_ofstring_andstring import SingleWrapperOfMapOfstringAndstring
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getSettings
        api_response = api_instance.get_settings_using_get(authorization, version)
        print("The response of UserApi->get_settings_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_settings_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfMapOfstringAndstring**](SingleWrapperOfMapOfstringAndstring.md)

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

# **get_sponsor_logo_using_get**
> SingleWrapperOfSponsorLogoResponse get_sponsor_logo_using_get(obfuscated_id, version)

getSponsorLogo

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_sponsor_logo_response import SingleWrapperOfSponsorLogoResponse
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
    api_instance = dupr_backend.UserApi(api_client)
    obfuscated_id = 56 # int | obfuscatedId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getSponsorLogo
        api_response = api_instance.get_sponsor_logo_using_get(obfuscated_id, version)
        print("The response of UserApi->get_sponsor_logo_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_sponsor_logo_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obfuscated_id** | **int**| obfuscatedId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfSponsorLogoResponse**](SingleWrapperOfSponsorLogoResponse.md)

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

# **get_statistics_using_get1**
> SingleWrapperOfUserStatisticResponse get_statistics_using_get1(authorization, version)

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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getStatistics
        api_response = api_instance.get_statistics_using_get1(authorization, version)
        print("The response of UserApi->get_statistics_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_statistics_using_get1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **get_user_initialization_information_bulk_using_post**
> ArrayWrapperOfPlayerInitializationDataResponse get_user_initialization_information_bulk_using_post(authorization, format, version, user_list_request)

getUserInitializationInformationBulk

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_player_initialization_data_response import ArrayWrapperOfPlayerInitializationDataResponse
from dupr_backend.models.user_list_request import UserListRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    format = 'format_example' # str | format
    version = 'v1.0' # str | version (default to 'v1.0')
    user_list_request = dupr_backend.UserListRequest() # UserListRequest | userListRequest

    try:
        # getUserInitializationInformationBulk
        api_response = api_instance.get_user_initialization_information_bulk_using_post(authorization, format, version, user_list_request)
        print("The response of UserApi->get_user_initialization_information_bulk_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_initialization_information_bulk_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **format** | **str**| format | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **user_list_request** | [**UserListRequest**](UserListRequest.md)| userListRequest | 

### Return type

[**ArrayWrapperOfPlayerInitializationDataResponse**](ArrayWrapperOfPlayerInitializationDataResponse.md)

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

# **get_user_initialization_information_using_get**
> ArrayWrapperOfPlayerInitializationProgressResponse get_user_initialization_information_using_get(authorization, user_id, version)

getUserInitializationInformation

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_player_initialization_progress_response import ArrayWrapperOfPlayerInitializationProgressResponse
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    user_id = 56 # int | userId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getUserInitializationInformation
        api_response = api_instance.get_user_initialization_information_using_get(authorization, user_id, version)
        print("The response of UserApi->get_user_initialization_information_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_initialization_information_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **user_id** | **int**| userId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfPlayerInitializationProgressResponse**](ArrayWrapperOfPlayerInitializationProgressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verfied_statistics_using_get**
> Wrapper get_verfied_statistics_using_get(authorization, version)

getVerfiedStatistics

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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getVerfiedStatistics
        api_response = api_instance.get_verfied_statistics_using_get(authorization, version)
        print("The response of UserApi->get_verfied_statistics_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_verfied_statistics_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **history_using_get**
> List[NotificationHistoryResponse] history_using_get(authorization, limit, offset)

history

### Example


```python
import dupr_backend
from dupr_backend.models.notification_history_response import NotificationHistoryResponse
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset

    try:
        # history
        api_response = api_instance.history_using_get(authorization, limit, offset)
        print("The response of UserApi->history_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->history_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 

### Return type

[**List[NotificationHistoryResponse]**](NotificationHistoryResponse.md)

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

# **is_sole_director_using_get**
> SingleWrapperOfboolean is_sole_director_using_get(authorization, version)

isSoleDirector

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_ofboolean import SingleWrapperOfboolean
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # isSoleDirector
        api_response = api_instance.is_sole_director_using_get(authorization, version)
        print("The response of UserApi->is_sole_director_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->is_sole_director_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

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

# **logout_using_post**
> Wrapper logout_using_post(authorization, version, request)

logout

### Example


```python
import dupr_backend
from dupr_backend.models.logout_request import LogoutRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LogoutRequest() # LogoutRequest | request

    try:
        # logout
        api_response = api_instance.logout_using_post(authorization, version, request)
        print("The response of UserApi->logout_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->logout_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LogoutRequest**](LogoutRequest.md)| request | 

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

# **reset_password_using_post**
> Wrapper reset_password_using_post(authorization, version, request)

resetPassword

### Example


```python
import dupr_backend
from dupr_backend.models.reset_password_request import ResetPasswordRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ResetPasswordRequest() # ResetPasswordRequest | request

    try:
        # resetPassword
        api_response = api_instance.reset_password_using_post(authorization, version, request)
        print("The response of UserApi->reset_password_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->reset_password_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ResetPasswordRequest**](ResetPasswordRequest.md)| request | 

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

# **send_email_verification_link_using_post**
> Wrapper send_email_verification_link_using_post(authorization, version, email_exist_request)

sendEmailVerificationLink

### Example


```python
import dupr_backend
from dupr_backend.models.email_exist_request import EmailExistRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    email_exist_request = dupr_backend.EmailExistRequest() # EmailExistRequest | emailExistRequest

    try:
        # sendEmailVerificationLink
        api_response = api_instance.send_email_verification_link_using_post(authorization, version, email_exist_request)
        print("The response of UserApi->send_email_verification_link_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->send_email_verification_link_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **email_exist_request** | [**EmailExistRequest**](EmailExistRequest.md)| emailExistRequest | 

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

# **send_phone_otp_using_post**
> Wrapper send_phone_otp_using_post(authorization, version, sms_otp, x_forwarded_for=x_forwarded_for)

sendPhoneOTP

### Example


```python
import dupr_backend
from dupr_backend.models.send_otp_request import SendOtpRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    sms_otp = dupr_backend.SendOtpRequest() # SendOtpRequest | smsOtp
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # sendPhoneOTP
        api_response = api_instance.send_phone_otp_using_post(authorization, version, sms_otp, x_forwarded_for=x_forwarded_for)
        print("The response of UserApi->send_phone_otp_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->send_phone_otp_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **sms_otp** | [**SendOtpRequest**](SendOtpRequest.md)| smsOtp | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

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

# **send_verification_email_using_post**
> Wrapper send_verification_email_using_post(authorization, version, email_exist_request)

sendVerificationEmail

### Example


```python
import dupr_backend
from dupr_backend.models.email_exist_request import EmailExistRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    email_exist_request = dupr_backend.EmailExistRequest() # EmailExistRequest | emailExistRequest

    try:
        # sendVerificationEmail
        api_response = api_instance.send_verification_email_using_post(authorization, version, email_exist_request)
        print("The response of UserApi->send_verification_email_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->send_verification_email_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **email_exist_request** | [**EmailExistRequest**](EmailExistRequest.md)| emailExistRequest | 

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

# **update_lucra_connection_using_put1**
> Wrapper update_lucra_connection_using_put1(authorization, version, request)

updateLucraConnection

### Example


```python
import dupr_backend
from dupr_backend.models.user_lucra_request import UserLucraRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserLucraRequest() # UserLucraRequest | request

    try:
        # updateLucraConnection
        api_response = api_instance.update_lucra_connection_using_put1(authorization, version, request)
        print("The response of UserApi->update_lucra_connection_using_put1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_lucra_connection_using_put1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserLucraRequest**](UserLucraRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **update_preferences_using_put**
> Wrapper update_preferences_using_put(authorization, version, preference)

updatePreferences

### Example


```python
import dupr_backend
from dupr_backend.models.user_preferences_request import UserPreferencesRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    preference = dupr_backend.UserPreferencesRequest() # UserPreferencesRequest | preference

    try:
        # updatePreferences
        api_response = api_instance.update_preferences_using_put(authorization, version, preference)
        print("The response of UserApi->update_preferences_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_preferences_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **preference** | [**UserPreferencesRequest**](UserPreferencesRequest.md)| preference | 

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

# **update_profile_using_put**
> SingleWrapperOfUserResponse update_profile_using_put(authorization, version, request)

updateProfile

### Example


```python
import dupr_backend
from dupr_backend.models.player_profile_request import PlayerProfileRequest
from dupr_backend.models.single_wrapper_of_user_response import SingleWrapperOfUserResponse
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PlayerProfileRequest() # PlayerProfileRequest | request

    try:
        # updateProfile
        api_response = api_instance.update_profile_using_put(authorization, version, request)
        print("The response of UserApi->update_profile_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_profile_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**PlayerProfileRequest**](PlayerProfileRequest.md)| request | 

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

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

# **update_settings_using_put**
> Wrapper update_settings_using_put(authorization, version, request)

updateSettings

### Example


```python
import dupr_backend
from dupr_backend.models.user_settings_request import UserSettingsRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserSettingsRequest() # UserSettingsRequest | request

    try:
        # updateSettings
        api_response = api_instance.update_settings_using_put(authorization, version, request)
        print("The response of UserApi->update_settings_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_settings_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserSettingsRequest**](UserSettingsRequest.md)| request | 

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

# **verify_captcha_using_post**
> SingleWrapperOfboolean verify_captcha_using_post(version, verify_token_request)

verifyCaptcha

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_ofboolean import SingleWrapperOfboolean
from dupr_backend.models.verify_token_request import VerifyTokenRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    verify_token_request = dupr_backend.VerifyTokenRequest() # VerifyTokenRequest | verifyTokenRequest

    try:
        # verifyCaptcha
        api_response = api_instance.verify_captcha_using_post(version, verify_token_request)
        print("The response of UserApi->verify_captcha_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->verify_captcha_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **verify_token_request** | [**VerifyTokenRequest**](VerifyTokenRequest.md)| verifyTokenRequest | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

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

# **verify_email_address_using_post**
> SingleWrapperOfboolean verify_email_address_using_post(version, verify_email_request)

verifyEmailAddress

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_ofboolean import SingleWrapperOfboolean
from dupr_backend.models.verify_email_request import VerifyEmailRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    verify_email_request = dupr_backend.VerifyEmailRequest() # VerifyEmailRequest | verifyEmailRequest

    try:
        # verifyEmailAddress
        api_response = api_instance.verify_email_address_using_post(version, verify_email_request)
        print("The response of UserApi->verify_email_address_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->verify_email_address_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **verify_email_request** | [**VerifyEmailRequest**](VerifyEmailRequest.md)| verifyEmailRequest | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

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

# **verify_phone_number_using_post**
> Wrapper verify_phone_number_using_post(authorization, version, sms_otp)

verifyPhoneNumber

### Example


```python
import dupr_backend
from dupr_backend.models.verify_otp_request import VerifyOtpRequest
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
    api_instance = dupr_backend.UserApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    sms_otp = dupr_backend.VerifyOtpRequest() # VerifyOtpRequest | smsOtp

    try:
        # verifyPhoneNumber
        api_response = api_instance.verify_phone_number_using_post(authorization, version, sms_otp)
        print("The response of UserApi->verify_phone_number_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->verify_phone_number_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **sms_otp** | [**VerifyOtpRequest**](VerifyOtpRequest.md)| smsOtp | 

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

