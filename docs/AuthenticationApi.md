# dupr_backend.AuthenticationApi

All URIs are relative to *//https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_registration_using_put**](AuthenticationApi.md#device_registration_using_put) | **PUT** /auth/{version}/device | deviceRegistration
[**email_already_exists_using_get**](AuthenticationApi.md#email_already_exists_using_get) | **GET** /auth/email/{version}/exists | emailAlreadyExists
[**email_exists_using_post**](AuthenticationApi.md#email_exists_using_post) | **POST** /auth/email/{version}/exists | emailExists
[**initiate_reset_password_using_get**](AuthenticationApi.md#initiate_reset_password_using_get) | **GET** /auth/password/{version}/initiate | initiateResetPassword
[**login_read_only_token_using_post**](AuthenticationApi.md#login_read_only_token_using_post) | **POST** /auth/{version}/login-read-only-token | loginReadOnlyToken
[**login_read_only_token_with_full_access_token_using_post**](AuthenticationApi.md#login_read_only_token_with_full_access_token_using_post) | **POST** /auth/{version}/login-read-only-token-with-session | loginReadOnlyTokenWithFullAccessToken
[**login_using_post**](AuthenticationApi.md#login_using_post) | **POST** /auth/{version}/login | login
[**panel_login_using_post**](AuthenticationApi.md#panel_login_using_post) | **POST** /auth/panel/{version}/login | panelLogin
[**refresh_access_token_using_get**](AuthenticationApi.md#refresh_access_token_using_get) | **GET** /auth/{version}/refresh | refreshAccessToken
[**register_using_post**](AuthenticationApi.md#register_using_post) | **POST** /auth/{version}/signup | register
[**reset_password_using_get**](AuthenticationApi.md#reset_password_using_get) | **GET** /auth/password/{version}/reset | resetPassword
[**send_verification_email_using_get**](AuthenticationApi.md#send_verification_email_using_get) | **GET** /auth/email/{version}/resend | sendVerificationEmail
[**validate_ambassador_code_using_get**](AuthenticationApi.md#validate_ambassador_code_using_get) | **GET** /auth/{version}/validate | validateAmbassadorCode
[**verify_email_address_using_get**](AuthenticationApi.md#verify_email_address_using_get) | **GET** /auth/email/{version}/verify | verifyEmailAddress
[**verify_user_email_using_post**](AuthenticationApi.md#verify_user_email_using_post) | **POST** /auth/email/{version}/verify | verifyUserEmail

# **device_registration_using_put**
> Wrapper device_registration_using_put(body, version)

deviceRegistration

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
body = dupr_backend.DeviceRequest() # DeviceRequest | request
version = 'version_example' # str | version

try:
    # deviceRegistration
    api_response = api_instance.device_registration_using_put(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->device_registration_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceRequest**](DeviceRequest.md)| request | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_already_exists_using_get**
> SingleWrapperOfboolean email_already_exists_using_get(email, version)

emailAlreadyExists

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
email = 'email_example' # str | email
version = 'version_example' # str | version

try:
    # emailAlreadyExists
    api_response = api_instance.email_already_exists_using_get(email, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->email_already_exists_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_exists_using_post**
> SingleWrapperOfboolean email_exists_using_post(body, version)

emailExists

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
body = dupr_backend.EmailExistRequest() # EmailExistRequest | emailExistRequest
version = 'version_example' # str | version

try:
    # emailExists
    api_response = api_instance.email_exists_using_post(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->email_exists_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailExistRequest**](EmailExistRequest.md)| emailExistRequest | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_reset_password_using_get**
> Wrapper initiate_reset_password_using_get(email, version)

initiateResetPassword

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
email = 'email_example' # str | email
version = 'version_example' # str | version

try:
    # initiateResetPassword
    api_response = api_instance.initiate_reset_password_using_get(email, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->initiate_reset_password_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_read_only_token_using_post**
> SingleWrapperOfobject login_read_only_token_using_post(body, x_authorization, version, x_forwarded_for=x_forwarded_for)

loginReadOnlyToken

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
body = dupr_backend.LoginRequest() # LoginRequest | request
x_authorization = 'x_authorization_example' # str | x-authorization
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # loginReadOnlyToken
    api_response = api_instance.login_read_only_token_using_post(body, x_authorization, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_read_only_token_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginRequest**](LoginRequest.md)| request | 
 **x_authorization** | **str**| x-authorization | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfobject**](SingleWrapperOfobject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_read_only_token_with_full_access_token_using_post**
> SingleWrapperOfobject login_read_only_token_with_full_access_token_using_post(version, x_authorization, x_forwarded_for=x_forwarded_for)

loginReadOnlyTokenWithFullAccessToken

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
version = 'version_example' # str | version
x_authorization = 'x_authorization_example' # str | x-authorization
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # loginReadOnlyTokenWithFullAccessToken
    api_response = api_instance.login_read_only_token_with_full_access_token_using_post(version, x_authorization, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_read_only_token_with_full_access_token_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | 
 **x_authorization** | **str**| x-authorization | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfobject**](SingleWrapperOfobject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_post**
> SingleWrapperOfAuthResponse login_using_post(body, version, x_forwarded_for=x_forwarded_for)

login

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
body = dupr_backend.LoginRequest() # LoginRequest | request
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # login
    api_response = api_instance.login_using_post(body, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginRequest**](LoginRequest.md)| request | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfAuthResponse**](SingleWrapperOfAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **panel_login_using_post**
> SingleWrapperOfAuthResponse panel_login_using_post(body, version, x_forwarded_for=x_forwarded_for)

panelLogin

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
body = dupr_backend.LoginRequest() # LoginRequest | request
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # panelLogin
    api_response = api_instance.panel_login_using_post(body, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->panel_login_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginRequest**](LoginRequest.md)| request | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfAuthResponse**](SingleWrapperOfAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_access_token_using_get**
> SingleWrapperOfstring refresh_access_token_using_get(version, x_refresh_token)

refreshAccessToken

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
version = 'version_example' # str | version
x_refresh_token = 'x_refresh_token_example' # str | x-refresh-token

try:
    # refreshAccessToken
    api_response = api_instance.refresh_access_token_using_get(version, x_refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->refresh_access_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | 
 **x_refresh_token** | **str**| x-refresh-token | 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_using_post**
> SingleWrapperOfAuthResponse register_using_post(body, version, x_forwarded_for=x_forwarded_for)

register

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
body = dupr_backend.PlayerSignUpRequest() # PlayerSignUpRequest | request
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # register
    api_response = api_instance.register_using_post(body, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->register_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayerSignUpRequest**](PlayerSignUpRequest.md)| request | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfAuthResponse**](SingleWrapperOfAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_using_get**
> Wrapper reset_password_using_get(code, email, version, x_password)

resetPassword

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
code = 'code_example' # str | code
email = 'email_example' # str | email
version = 'version_example' # str | version
x_password = 'x_password_example' # str | x-password

try:
    # resetPassword
    api_response = api_instance.reset_password_using_get(code, email, version, x_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->reset_password_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 
 **email** | **str**| email | 
 **version** | **str**| version | 
 **x_password** | **str**| x-password | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_verification_email_using_get**
> Wrapper send_verification_email_using_get(email, version)

sendVerificationEmail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
email = 'email_example' # str | email
version = 'version_example' # str | version

try:
    # sendVerificationEmail
    api_response = api_instance.send_verification_email_using_get(email, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->send_verification_email_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_ambassador_code_using_get**
> Wrapper validate_ambassador_code_using_get(code, version)

validateAmbassadorCode

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
code = 'code_example' # str | code
version = 'version_example' # str | version

try:
    # validateAmbassadorCode
    api_response = api_instance.validate_ambassador_code_using_get(code, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->validate_ambassador_code_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email_address_using_get**
> SingleWrapperOfboolean verify_email_address_using_get(code, email, version)

verifyEmailAddress

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
code = 'code_example' # str | code
email = 'email_example' # str | email
version = 'version_example' # str | version

try:
    # verifyEmailAddress
    api_response = api_instance.verify_email_address_using_get(code, email, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->verify_email_address_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 
 **email** | **str**| email | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user_email_using_post**
> SingleWrapperOfUserResponse verify_user_email_using_post(body, version)

verifyUserEmail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AuthenticationApi()
body = dupr_backend.VerifyTokenRequest() # VerifyTokenRequest | verifyTokenRequest
version = 'version_example' # str | version

try:
    # verifyUserEmail
    api_response = api_instance.verify_user_email_using_post(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->verify_user_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyTokenRequest**](VerifyTokenRequest.md)| verifyTokenRequest | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

