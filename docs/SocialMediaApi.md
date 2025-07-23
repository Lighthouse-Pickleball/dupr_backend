# dupr_backend.SocialMediaApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_provider_data**](SocialMediaApi.md#delete_provider_data) | **POST** /social/{version}/{provider}/delete | 
[**get_instagram_login**](SocialMediaApi.md#get_instagram_login) | **GET** /social/{version}/instagram/login | 
[**get_login_detail**](SocialMediaApi.md#get_login_detail) | **GET** /social/{version}/login | 
[**get_share_messages**](SocialMediaApi.md#get_share_messages) | **GET** /social/share/{version}/message | 
[**update_social_login_details**](SocialMediaApi.md#update_social_login_details) | **PUT** /social/{version}/login | 


# **delete_provider_data**
> DeleteUserResponse delete_provider_data(version, provider, body)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.delete_user_response import DeleteUserResponse
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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    version = 'version_example' # str | 
    provider = 'provider_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.delete_provider_data(version, provider, body)
        print("The response of SocialMediaApi->delete_provider_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->delete_provider_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **provider** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

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

# **get_instagram_login**
> object get_instagram_login(version, code=code, error=error, error_reason=error_reason, error_description=error_description, state=state)

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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    version = 'version_example' # str | 
    code = 'code_example' # str |  (optional)
    error = 'error_example' # str |  (optional)
    error_reason = 'error_reason_example' # str |  (optional)
    error_description = 'error_description_example' # str |  (optional)
    state = 56 # int |  (optional)

    try:
        api_response = api_instance.get_instagram_login(version, code=code, error=error, error_reason=error_reason, error_description=error_description, state=state)
        print("The response of SocialMediaApi->get_instagram_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->get_instagram_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **code** | **str**|  | [optional] 
 **error** | **str**|  | [optional] 
 **error_reason** | **str**|  | [optional] 
 **error_description** | **str**|  | [optional] 
 **state** | **int**|  | [optional] 

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

# **get_login_detail**
> Wrapper get_login_detail(version)

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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    version = 'version_example' # str | 

    try:
        api_response = api_instance.get_login_detail(version)
        print("The response of SocialMediaApi->get_login_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->get_login_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 

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

# **get_share_messages**
> Wrapper get_share_messages(version)

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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    version = 'version_example' # str | 

    try:
        api_response = api_instance.get_share_messages(version)
        print("The response of SocialMediaApi->get_share_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->get_share_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 

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

# **update_social_login_details**
> Wrapper update_social_login_details(version, user_auth_provider_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.user_auth_provider_request import UserAuthProviderRequest
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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    version = 'version_example' # str | 
    user_auth_provider_request = dupr_backend.UserAuthProviderRequest() # UserAuthProviderRequest | 

    try:
        api_response = api_instance.update_social_login_details(version, user_auth_provider_request)
        print("The response of SocialMediaApi->update_social_login_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->update_social_login_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **user_auth_provider_request** | [**UserAuthProviderRequest**](UserAuthProviderRequest.md)|  | 

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

