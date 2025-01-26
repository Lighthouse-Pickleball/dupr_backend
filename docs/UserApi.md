# dupr_backend.UserApi

All URIs are relative to *//https://backend.mydupr.com/*

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
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # deleteUser
    api_response = api_instance.delete_user_using_delete(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete**
> int delete_using_delete(authorization, id)

delete

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = ['id_example'] # list[str] | id

try:
    # delete
    api_response = api_instance.delete_using_delete(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | [**list[str]**](str.md)| id | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculated_statistics_using_get**
> SingleWrapperOfPreCalculatedUserStatisticsResponse get_calculated_statistics_using_get(authorization, id, version)

getCalculatedStatistics

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getCalculatedStatistics
    api_response = api_instance.get_calculated_statistics_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_calculated_statistics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPreCalculatedUserStatisticsResponse**](SingleWrapperOfPreCalculatedUserStatisticsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_using_get**
> SingleWrapperOfUserResponse get_profile_using_get(authorization, version)

getProfile

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getProfile
    api_response = api_instance.get_profile_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_profile_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rating_using_get**
> SingleWrapperOfPlayerRatingResponse get_rating_using_get(authorization, version)

getRating

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getRating
    api_response = api_instance.get_rating_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_rating_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPlayerRatingResponse**](SingleWrapperOfPlayerRatingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_using_get**
> SingleWrapperOfMapOfstringAndstring get_settings_using_get(authorization, version)

getSettings

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getSettings
    api_response = api_instance.get_settings_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_settings_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMapOfstringAndstring**](SingleWrapperOfMapOfstringAndstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sponsor_logo_using_get**
> SingleWrapperOfSponsorLogoResponse get_sponsor_logo_using_get(obfuscated_id, version)

getSponsorLogo

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
obfuscated_id = 789 # int | obfuscatedId
version = 'version_example' # str | version

try:
    # getSponsorLogo
    api_response = api_instance.get_sponsor_logo_using_get(obfuscated_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_sponsor_logo_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **obfuscated_id** | **int**| obfuscatedId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfSponsorLogoResponse**](SingleWrapperOfSponsorLogoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_using_get1**
> SingleWrapperOfUserStatisticResponse get_statistics_using_get1(authorization, version)

getStatistics

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getStatistics
    api_response = api_instance.get_statistics_using_get1(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_statistics_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUserStatisticResponse**](SingleWrapperOfUserStatisticResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_initialization_information_bulk_using_post**
> ArrayWrapperOfPlayerInitializationDataResponse get_user_initialization_information_bulk_using_post(body, authorization, format, version)

getUserInitializationInformationBulk

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.UserListRequest() # UserListRequest | userListRequest
authorization = 'Bearer ' # str |  (default to Bearer )
format = 'format_example' # str | format
version = 'version_example' # str | version

try:
    # getUserInitializationInformationBulk
    api_response = api_instance.get_user_initialization_information_bulk_using_post(body, authorization, format, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_initialization_information_bulk_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserListRequest**](UserListRequest.md)| userListRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **format** | **str**| format | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfPlayerInitializationDataResponse**](ArrayWrapperOfPlayerInitializationDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_initialization_information_using_get**
> ArrayWrapperOfPlayerInitializationProgressResponse get_user_initialization_information_using_get(authorization, user_id, version)

getUserInitializationInformation

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
user_id = 789 # int | userId
version = 'version_example' # str | version

try:
    # getUserInitializationInformation
    api_response = api_instance.get_user_initialization_information_using_get(authorization, user_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_initialization_information_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **user_id** | **int**| userId | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfPlayerInitializationProgressResponse**](ArrayWrapperOfPlayerInitializationProgressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verfied_statistics_using_get**
> Wrapper get_verfied_statistics_using_get(authorization, version)

getVerfiedStatistics

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getVerfiedStatistics
    api_response = api_instance.get_verfied_statistics_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_verfied_statistics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history_using_get**
> list[NotificationHistoryResponse] history_using_get(authorization, limit, offset)

history

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 789 # int | limit
offset = 789 # int | offset

try:
    # history
    api_response = api_instance.history_using_get(authorization, limit, offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 

### Return type

[**list[NotificationHistoryResponse]**](NotificationHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_sole_director_using_get**
> SingleWrapperOfboolean is_sole_director_using_get(authorization, version)

isSoleDirector

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # isSoleDirector
    api_response = api_instance.is_sole_director_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->is_sole_director_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_using_post**
> Wrapper logout_using_post(body, authorization, version)

logout

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.LogoutRequest() # LogoutRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # logout
    api_response = api_instance.logout_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->logout_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogoutRequest**](LogoutRequest.md)| request | 
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

# **reset_password_using_post**
> Wrapper reset_password_using_post(body, authorization, version)

resetPassword

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.ResetPasswordRequest() # ResetPasswordRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # resetPassword
    api_response = api_instance.reset_password_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->reset_password_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordRequest**](ResetPasswordRequest.md)| request | 
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

# **send_email_verification_link_using_post**
> Wrapper send_email_verification_link_using_post(body, authorization, version)

sendEmailVerificationLink

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.EmailExistRequest() # EmailExistRequest | emailExistRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # sendEmailVerificationLink
    api_response = api_instance.send_email_verification_link_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->send_email_verification_link_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailExistRequest**](EmailExistRequest.md)| emailExistRequest | 
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

# **send_phone_otp_using_post**
> Wrapper send_phone_otp_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)

sendPhoneOTP

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.SendOtpRequest() # SendOtpRequest | smsOtp
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # sendPhoneOTP
    api_response = api_instance.send_phone_otp_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->send_phone_otp_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendOtpRequest**](SendOtpRequest.md)| smsOtp | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_verification_email_using_post**
> Wrapper send_verification_email_using_post(body, authorization, version)

sendVerificationEmail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.EmailExistRequest() # EmailExistRequest | emailExistRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # sendVerificationEmail
    api_response = api_instance.send_verification_email_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->send_verification_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailExistRequest**](EmailExistRequest.md)| emailExistRequest | 
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

# **update_lucra_connection_using_put1**
> Wrapper update_lucra_connection_using_put1(body, authorization, version)

updateLucraConnection

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.UserLucraRequest() # UserLucraRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateLucraConnection
    api_response = api_instance.update_lucra_connection_using_put1(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_lucra_connection_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserLucraRequest**](UserLucraRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_preferences_using_put**
> Wrapper update_preferences_using_put(body, authorization, version)

updatePreferences

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.UserPreferencesRequest() # UserPreferencesRequest | preference
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updatePreferences
    api_response = api_instance.update_preferences_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_preferences_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPreferencesRequest**](UserPreferencesRequest.md)| preference | 
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

# **update_profile_using_put**
> SingleWrapperOfUserResponse update_profile_using_put(body, authorization, version)

updateProfile

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.PlayerProfileRequest() # PlayerProfileRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateProfile
    api_response = api_instance.update_profile_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_profile_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayerProfileRequest**](PlayerProfileRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_using_put**
> Wrapper update_settings_using_put(body, authorization, version)

updateSettings

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.UserSettingsRequest() # UserSettingsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateSettings
    api_response = api_instance.update_settings_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_settings_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSettingsRequest**](UserSettingsRequest.md)| request | 
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

# **verify_captcha_using_post**
> SingleWrapperOfboolean verify_captcha_using_post(body, version)

verifyCaptcha

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.VerifyTokenRequest() # VerifyTokenRequest | verifyTokenRequest
version = 'version_example' # str | version

try:
    # verifyCaptcha
    api_response = api_instance.verify_captcha_using_post(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->verify_captcha_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyTokenRequest**](VerifyTokenRequest.md)| verifyTokenRequest | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email_address_using_post**
> SingleWrapperOfboolean verify_email_address_using_post(body, version)

verifyEmailAddress

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.VerifyEmailRequest() # VerifyEmailRequest | verifyEmailRequest
version = 'version_example' # str | version

try:
    # verifyEmailAddress
    api_response = api_instance.verify_email_address_using_post(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->verify_email_address_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyEmailRequest**](VerifyEmailRequest.md)| verifyEmailRequest | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_phone_number_using_post**
> Wrapper verify_phone_number_using_post(body, authorization, version)

verifyPhoneNumber

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.UserApi()
body = dupr_backend.VerifyOtpRequest() # VerifyOtpRequest | smsOtp
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # verifyPhoneNumber
    api_response = api_instance.verify_phone_number_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->verify_phone_number_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyOtpRequest**](VerifyOtpRequest.md)| smsOtp | 
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

