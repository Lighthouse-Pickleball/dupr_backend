# dupr_backend.SocialMediaApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_provider_data_using_post**](SocialMediaApi.md#delete_provider_data_using_post) | **POST** /social/{version}/{provider}/delete | deleteProviderData
[**get_instagram_login_using_get**](SocialMediaApi.md#get_instagram_login_using_get) | **GET** /social/{version}/instagram/login | getInstagramLogin
[**get_login_detail_using_get**](SocialMediaApi.md#get_login_detail_using_get) | **GET** /social/{version}/login | getLoginDetail
[**get_share_messages_using_get**](SocialMediaApi.md#get_share_messages_using_get) | **GET** /social/share/{version}/message | getShareMessages
[**update_social_login_details_using_put**](SocialMediaApi.md#update_social_login_details_using_put) | **PUT** /social/{version}/login | updateSocialLoginDetails


# **delete_provider_data_using_post**
> DeleteUserResponse delete_provider_data_using_post(provider, version, request)

deleteProviderData

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.delete_user_response import DeleteUserResponse
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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    provider = 'provider_example' # str | provider
    version = 'v1.0' # str | version (default to 'v1.0')
    request = 'request_example' # str | request

    try:
        # deleteProviderData
        api_response = api_instance.delete_provider_data_using_post(provider, version, request)
        print("The response of SocialMediaApi->delete_provider_data_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->delete_provider_data_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| provider | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | **str**| request | 

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

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

# **get_instagram_login_using_get**
> object get_instagram_login_using_get(code, state, version, error=error, error_description=error_description, error_reason=error_reason)

getInstagramLogin

### Example

```python
import time
import os
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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    code = 'code_example' # str | code
    state = 56 # int | state
    version = 'v1.0' # str | version (default to 'v1.0')
    error = 'error_example' # str | error (optional)
    error_description = 'error_description_example' # str | error_description (optional)
    error_reason = 'error_reason_example' # str | error_reason (optional)

    try:
        # getInstagramLogin
        api_response = api_instance.get_instagram_login_using_get(code, state, version, error=error, error_description=error_description, error_reason=error_reason)
        print("The response of SocialMediaApi->get_instagram_login_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->get_instagram_login_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 
 **state** | **int**| state | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **error** | **str**| error | [optional] 
 **error_description** | **str**| error_description | [optional] 
 **error_reason** | **str**| error_reason | [optional] 

### Return type

**object**

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

# **get_login_detail_using_get**
> Wrapper get_login_detail_using_get(authorization, version)

getLoginDetail

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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getLoginDetail
        api_response = api_instance.get_login_detail_using_get(authorization, version)
        print("The response of SocialMediaApi->get_login_detail_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->get_login_detail_using_get: %s\n" % e)
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

# **get_share_messages_using_get**
> Wrapper get_share_messages_using_get(authorization, version)

getShareMessages

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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getShareMessages
        api_response = api_instance.get_share_messages_using_get(authorization, version)
        print("The response of SocialMediaApi->get_share_messages_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->get_share_messages_using_get: %s\n" % e)
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

# **update_social_login_details_using_put**
> Wrapper update_social_login_details_using_put(authorization, version, request)

updateSocialLoginDetails

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.user_auth_provider_request import UserAuthProviderRequest
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
    api_instance = dupr_backend.SocialMediaApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserAuthProviderRequest() # UserAuthProviderRequest | request

    try:
        # updateSocialLoginDetails
        api_response = api_instance.update_social_login_details_using_put(authorization, version, request)
        print("The response of SocialMediaApi->update_social_login_details_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialMediaApi->update_social_login_details_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserAuthProviderRequest**](UserAuthProviderRequest.md)| request | 

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

