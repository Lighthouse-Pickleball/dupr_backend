# dupr_backend.AuthenticationApi

All URIs are relative to *http://https://backend.mydupr.com*

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
> Wrapper device_registration_using_put(version, request)

deviceRegistration

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.device_request import DeviceRequest
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.DeviceRequest() # DeviceRequest | request

    try:
        # deviceRegistration
        api_response = api_instance.device_registration_using_put(version, request)
        print("The response of AuthenticationApi->device_registration_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->device_registration_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**DeviceRequest**](DeviceRequest.md)| request | 

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

# **email_already_exists_using_get**
> SingleWrapperOfboolean email_already_exists_using_get(email, version)

emailAlreadyExists

### Example

```python
import time
import os
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    email = 'user@example.com' # str | email
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # emailAlreadyExists
        api_response = api_instance.email_already_exists_using_get(email, version)
        print("The response of AuthenticationApi->email_already_exists_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->email_already_exists_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 
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

# **email_exists_using_post**
> SingleWrapperOfboolean email_exists_using_post(version, email_exist_request)

emailExists

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.email_exist_request import EmailExistRequest
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    email_exist_request = dupr_backend.EmailExistRequest() # EmailExistRequest | emailExistRequest

    try:
        # emailExists
        api_response = api_instance.email_exists_using_post(version, email_exist_request)
        print("The response of AuthenticationApi->email_exists_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->email_exists_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **email_exist_request** | [**EmailExistRequest**](EmailExistRequest.md)| emailExistRequest | 

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

# **initiate_reset_password_using_get**
> Wrapper initiate_reset_password_using_get(email, version)

initiateResetPassword

### Example

```python
import time
import os
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    email = 'email_example' # str | email
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # initiateResetPassword
        api_response = api_instance.initiate_reset_password_using_get(email, version)
        print("The response of AuthenticationApi->initiate_reset_password_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->initiate_reset_password_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 
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

# **login_read_only_token_using_post**
> SingleWrapperOfobject login_read_only_token_using_post(version, x_authorization, request, x_forwarded_for=x_forwarded_for)

loginReadOnlyToken

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.login_request import LoginRequest
from dupr_backend.models.single_wrapper_ofobject import SingleWrapperOfobject
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    x_authorization = 'x_authorization_example' # str | x-authorization
    request = dupr_backend.LoginRequest() # LoginRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # loginReadOnlyToken
        api_response = api_instance.login_read_only_token_using_post(version, x_authorization, request, x_forwarded_for=x_forwarded_for)
        print("The response of AuthenticationApi->login_read_only_token_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_read_only_token_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_authorization** | **str**| x-authorization | 
 **request** | [**LoginRequest**](LoginRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfobject**](SingleWrapperOfobject.md)

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

# **login_read_only_token_with_full_access_token_using_post**
> SingleWrapperOfobject login_read_only_token_with_full_access_token_using_post(version, x_authorization, x_forwarded_for=x_forwarded_for)

loginReadOnlyTokenWithFullAccessToken

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_ofobject import SingleWrapperOfobject
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    x_authorization = 'x_authorization_example' # str | x-authorization
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # loginReadOnlyTokenWithFullAccessToken
        api_response = api_instance.login_read_only_token_with_full_access_token_using_post(version, x_authorization, x_forwarded_for=x_forwarded_for)
        print("The response of AuthenticationApi->login_read_only_token_with_full_access_token_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_read_only_token_with_full_access_token_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_authorization** | **str**| x-authorization | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfobject**](SingleWrapperOfobject.md)

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

# **login_using_post**
> SingleWrapperOfAuthResponse login_using_post(version, request, x_forwarded_for=x_forwarded_for)

login

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.login_request import LoginRequest
from dupr_backend.models.single_wrapper_of_auth_response import SingleWrapperOfAuthResponse
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LoginRequest() # LoginRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # login
        api_response = api_instance.login_using_post(version, request, x_forwarded_for=x_forwarded_for)
        print("The response of AuthenticationApi->login_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LoginRequest**](LoginRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfAuthResponse**](SingleWrapperOfAuthResponse.md)

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

# **panel_login_using_post**
> SingleWrapperOfAuthResponse panel_login_using_post(version, request, x_forwarded_for=x_forwarded_for)

panelLogin

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.login_request import LoginRequest
from dupr_backend.models.single_wrapper_of_auth_response import SingleWrapperOfAuthResponse
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LoginRequest() # LoginRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # panelLogin
        api_response = api_instance.panel_login_using_post(version, request, x_forwarded_for=x_forwarded_for)
        print("The response of AuthenticationApi->panel_login_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->panel_login_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LoginRequest**](LoginRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfAuthResponse**](SingleWrapperOfAuthResponse.md)

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

# **refresh_access_token_using_get**
> SingleWrapperOfstring refresh_access_token_using_get(version, x_refresh_token)

refreshAccessToken

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_ofstring import SingleWrapperOfstring
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    x_refresh_token = 'x_refresh_token_example' # str | x-refresh-token

    try:
        # refreshAccessToken
        api_response = api_instance.refresh_access_token_using_get(version, x_refresh_token)
        print("The response of AuthenticationApi->refresh_access_token_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->refresh_access_token_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_refresh_token** | **str**| x-refresh-token | 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

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

# **register_using_post**
> SingleWrapperOfAuthResponse register_using_post(version, request, x_forwarded_for=x_forwarded_for)

register

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.player_sign_up_request import PlayerSignUpRequest
from dupr_backend.models.single_wrapper_of_auth_response import SingleWrapperOfAuthResponse
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PlayerSignUpRequest() # PlayerSignUpRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # register
        api_response = api_instance.register_using_post(version, request, x_forwarded_for=x_forwarded_for)
        print("The response of AuthenticationApi->register_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->register_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**PlayerSignUpRequest**](PlayerSignUpRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfAuthResponse**](SingleWrapperOfAuthResponse.md)

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

# **reset_password_using_get**
> Wrapper reset_password_using_get(code, email, version, x_password)

resetPassword

### Example

```python
import time
import os
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    code = 'code_example' # str | code
    email = 'email_example' # str | email
    version = 'v1.0' # str | version (default to 'v1.0')
    x_password = 'x_password_example' # str | x-password

    try:
        # resetPassword
        api_response = api_instance.reset_password_using_get(code, email, version, x_password)
        print("The response of AuthenticationApi->reset_password_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->reset_password_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 
 **email** | **str**| email | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_password** | **str**| x-password | 

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

# **send_verification_email_using_get**
> Wrapper send_verification_email_using_get(email, version)

sendVerificationEmail

### Example

```python
import time
import os
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    email = 'email_example' # str | email
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # sendVerificationEmail
        api_response = api_instance.send_verification_email_using_get(email, version)
        print("The response of AuthenticationApi->send_verification_email_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->send_verification_email_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 
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

# **validate_ambassador_code_using_get**
> Wrapper validate_ambassador_code_using_get(code, version)

validateAmbassadorCode

### Example

```python
import time
import os
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    code = 'DUPR100' # str | code
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # validateAmbassadorCode
        api_response = api_instance.validate_ambassador_code_using_get(code, version)
        print("The response of AuthenticationApi->validate_ambassador_code_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->validate_ambassador_code_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 
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

# **verify_email_address_using_get**
> SingleWrapperOfboolean verify_email_address_using_get(code, email, version)

verifyEmailAddress

### Example

```python
import time
import os
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    code = 'code_example' # str | code
    email = 'email_example' # str | email
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # verifyEmailAddress
        api_response = api_instance.verify_email_address_using_get(code, email, version)
        print("The response of AuthenticationApi->verify_email_address_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->verify_email_address_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 
 **email** | **str**| email | 
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

# **verify_user_email_using_post**
> SingleWrapperOfUserResponse verify_user_email_using_post(version, verify_token_request)

verifyUserEmail

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_user_response import SingleWrapperOfUserResponse
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    verify_token_request = dupr_backend.VerifyTokenRequest() # VerifyTokenRequest | verifyTokenRequest

    try:
        # verifyUserEmail
        api_response = api_instance.verify_user_email_using_post(version, verify_token_request)
        print("The response of AuthenticationApi->verify_user_email_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->verify_user_email_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **verify_token_request** | [**VerifyTokenRequest**](VerifyTokenRequest.md)| verifyTokenRequest | 

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

