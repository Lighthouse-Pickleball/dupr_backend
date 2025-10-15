# dupr_backend.AuthenticationApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_registration**](AuthenticationApi.md#device_registration) | **PUT** /auth/{version}/device | 
[**email_already_exists**](AuthenticationApi.md#email_already_exists) | **GET** /auth/email/{version}/exists | 
[**email_exists**](AuthenticationApi.md#email_exists) | **POST** /auth/email/{version}/exists | 
[**initiate_reset_password**](AuthenticationApi.md#initiate_reset_password) | **GET** /auth/password/{version}/initiate | 
[**login**](AuthenticationApi.md#login) | **POST** /auth/{version}/login | 
[**login_read_only_token**](AuthenticationApi.md#login_read_only_token) | **POST** /auth/{version}/login-read-only-token | 
[**login_read_only_token_with_full_access_token**](AuthenticationApi.md#login_read_only_token_with_full_access_token) | **POST** /auth/{version}/login-read-only-token-with-session | 
[**panel_login**](AuthenticationApi.md#panel_login) | **POST** /auth/panel/{version}/login | 
[**refresh_access_token**](AuthenticationApi.md#refresh_access_token) | **GET** /auth/{version}/refresh | 
[**register**](AuthenticationApi.md#register) | **POST** /auth/{version}/signup | 
[**reset_password1**](AuthenticationApi.md#reset_password1) | **GET** /auth/password/{version}/reset | 
[**send_verification_email1**](AuthenticationApi.md#send_verification_email1) | **GET** /auth/email/{version}/resend | 
[**validate_ambassador_code**](AuthenticationApi.md#validate_ambassador_code) | **GET** /auth/{version}/validate | 
[**verify_email_address1**](AuthenticationApi.md#verify_email_address1) | **GET** /auth/email/{version}/verify | 
[**verify_user_email**](AuthenticationApi.md#verify_user_email) | **POST** /auth/email/{version}/verify | 


# **device_registration**
> Wrapper device_registration(version, device_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.device_request import DeviceRequest
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    device_request = dupr_backend.DeviceRequest() # DeviceRequest | 

    try:
        api_response = api_instance.device_registration(version, device_request)
        print("The response of AuthenticationApi->device_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->device_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **device_request** | [**DeviceRequest**](DeviceRequest.md)|  | 

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

# **email_already_exists**
> SingleWrapperBoolean email_already_exists(version, email)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_boolean import SingleWrapperBoolean
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    email = 'user@example.com' # str | 

    try:
        api_response = api_instance.email_already_exists(version, email)
        print("The response of AuthenticationApi->email_already_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->email_already_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **email** | **str**|  | 

### Return type

[**SingleWrapperBoolean**](SingleWrapperBoolean.md)

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

# **email_exists**
> SingleWrapperBoolean email_exists(version, email_exist_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.email_exist_request import EmailExistRequest
from dupr_backend.models.single_wrapper_boolean import SingleWrapperBoolean
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    email_exist_request = dupr_backend.EmailExistRequest() # EmailExistRequest | 

    try:
        api_response = api_instance.email_exists(version, email_exist_request)
        print("The response of AuthenticationApi->email_exists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->email_exists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **email_exist_request** | [**EmailExistRequest**](EmailExistRequest.md)|  | 

### Return type

[**SingleWrapperBoolean**](SingleWrapperBoolean.md)

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

# **initiate_reset_password**
> Wrapper initiate_reset_password(version, email)

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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    email = 'email_example' # str | 

    try:
        api_response = api_instance.initiate_reset_password(version, email)
        print("The response of AuthenticationApi->initiate_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->initiate_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **email** | **str**|  | 

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

# **login**
> SingleWrapperAuthResponse login(version, login_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.login_request import LoginRequest
from dupr_backend.models.single_wrapper_auth_response import SingleWrapperAuthResponse
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    login_request = dupr_backend.LoginRequest() # LoginRequest | 

    try:
        api_response = api_instance.login(version, login_request)
        print("The response of AuthenticationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**SingleWrapperAuthResponse**](SingleWrapperAuthResponse.md)

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

# **login_read_only_token**
> object login_read_only_token(version, x_authorization, login_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.login_request import LoginRequest
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    x_authorization = 'x_authorization_example' # str | 
    login_request = dupr_backend.LoginRequest() # LoginRequest | 

    try:
        api_response = api_instance.login_read_only_token(version, x_authorization, login_request)
        print("The response of AuthenticationApi->login_read_only_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_read_only_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **x_authorization** | **str**|  | 
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

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

# **login_read_only_token_with_full_access_token**
> object login_read_only_token_with_full_access_token(version, x_authorization)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    x_authorization = 'x_authorization_example' # str | 

    try:
        api_response = api_instance.login_read_only_token_with_full_access_token(version, x_authorization)
        print("The response of AuthenticationApi->login_read_only_token_with_full_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login_read_only_token_with_full_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **x_authorization** | **str**|  | 

### Return type

**object**

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

# **panel_login**
> SingleWrapperAuthResponse panel_login(version, login_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.login_request import LoginRequest
from dupr_backend.models.single_wrapper_auth_response import SingleWrapperAuthResponse
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    login_request = dupr_backend.LoginRequest() # LoginRequest | 

    try:
        api_response = api_instance.panel_login(version, login_request)
        print("The response of AuthenticationApi->panel_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->panel_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**SingleWrapperAuthResponse**](SingleWrapperAuthResponse.md)

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

# **refresh_access_token**
> object refresh_access_token(version, x_refresh_token)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    x_refresh_token = 'x_refresh_token_example' # str | 

    try:
        api_response = api_instance.refresh_access_token(version, x_refresh_token)
        print("The response of AuthenticationApi->refresh_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->refresh_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **x_refresh_token** | **str**|  | 

### Return type

**object**

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

# **register**
> SingleWrapperAuthResponse register(version, player_sign_up_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.player_sign_up_request import PlayerSignUpRequest
from dupr_backend.models.single_wrapper_auth_response import SingleWrapperAuthResponse
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    player_sign_up_request = dupr_backend.PlayerSignUpRequest() # PlayerSignUpRequest | 

    try:
        api_response = api_instance.register(version, player_sign_up_request)
        print("The response of AuthenticationApi->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **player_sign_up_request** | [**PlayerSignUpRequest**](PlayerSignUpRequest.md)|  | 

### Return type

[**SingleWrapperAuthResponse**](SingleWrapperAuthResponse.md)

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

# **reset_password1**
> Wrapper reset_password1(version, email, code, x_password)

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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    email = 'email_example' # str | 
    code = 'code_example' # str | 
    x_password = 'x_password_example' # str | 

    try:
        api_response = api_instance.reset_password1(version, email, code, x_password)
        print("The response of AuthenticationApi->reset_password1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->reset_password1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **email** | **str**|  | 
 **code** | **str**|  | 
 **x_password** | **str**|  | 

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

# **send_verification_email1**
> Wrapper send_verification_email1(version, email)

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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    email = 'email_example' # str | 

    try:
        api_response = api_instance.send_verification_email1(version, email)
        print("The response of AuthenticationApi->send_verification_email1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->send_verification_email1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **email** | **str**|  | 

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

# **validate_ambassador_code**
> Wrapper validate_ambassador_code(version, code)

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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    code = 'DUPR100' # str | 

    try:
        api_response = api_instance.validate_ambassador_code(version, code)
        print("The response of AuthenticationApi->validate_ambassador_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->validate_ambassador_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **code** | **str**|  | 

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

# **verify_email_address1**
> SingleWrapperBoolean verify_email_address1(version, email, code)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_boolean import SingleWrapperBoolean
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    email = 'email_example' # str | 
    code = 'code_example' # str | 

    try:
        api_response = api_instance.verify_email_address1(version, email, code)
        print("The response of AuthenticationApi->verify_email_address1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->verify_email_address1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **email** | **str**|  | 
 **code** | **str**|  | 

### Return type

[**SingleWrapperBoolean**](SingleWrapperBoolean.md)

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

# **verify_user_email**
> SingleWrapperUserResponse verify_user_email(version, verify_token_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_user_response import SingleWrapperUserResponse
from dupr_backend.models.verify_token_request import VerifyTokenRequest
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
    api_instance = dupr_backend.AuthenticationApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    verify_token_request = dupr_backend.VerifyTokenRequest() # VerifyTokenRequest | 

    try:
        api_response = api_instance.verify_user_email(version, verify_token_request)
        print("The response of AuthenticationApi->verify_user_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->verify_user_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **verify_token_request** | [**VerifyTokenRequest**](VerifyTokenRequest.md)|  | 

### Return type

[**SingleWrapperUserResponse**](SingleWrapperUserResponse.md)

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

