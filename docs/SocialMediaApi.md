# dupr_backend.SocialMediaApi

All URIs are relative to *//https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_provider_data_using_post**](SocialMediaApi.md#delete_provider_data_using_post) | **POST** /social/{version}/{provider}/delete | deleteProviderData
[**get_instagram_login_using_get**](SocialMediaApi.md#get_instagram_login_using_get) | **GET** /social/{version}/instagram/login | getInstagramLogin
[**get_login_detail_using_get**](SocialMediaApi.md#get_login_detail_using_get) | **GET** /social/{version}/login | getLoginDetail
[**get_share_messages_using_get**](SocialMediaApi.md#get_share_messages_using_get) | **GET** /social/share/{version}/message | getShareMessages
[**update_social_login_details_using_put**](SocialMediaApi.md#update_social_login_details_using_put) | **PUT** /social/{version}/login | updateSocialLoginDetails

# **delete_provider_data_using_post**
> DeleteUserResponse delete_provider_data_using_post(body, provider, version)

deleteProviderData

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SocialMediaApi()
body = 'body_example' # str | request
provider = 'provider_example' # str | provider
version = 'version_example' # str | version

try:
    # deleteProviderData
    api_response = api_instance.delete_provider_data_using_post(body, provider, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->delete_provider_data_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| request | 
 **provider** | **str**| provider | 
 **version** | **str**| version | 

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instagram_login_using_get**
> object get_instagram_login_using_get(code, state, version, error=error, error_description=error_description, error_reason=error_reason)

getInstagramLogin

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SocialMediaApi()
code = 'code_example' # str | code
state = 789 # int | state
version = 'version_example' # str | version
error = 'error_example' # str | error (optional)
error_description = 'error_description_example' # str | error_description (optional)
error_reason = 'error_reason_example' # str | error_reason (optional)

try:
    # getInstagramLogin
    api_response = api_instance.get_instagram_login_using_get(code, state, version, error=error, error_description=error_description, error_reason=error_reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_instagram_login_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| code | 
 **state** | **int**| state | 
 **version** | **str**| version | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_detail_using_get**
> Wrapper get_login_detail_using_get(authorization, version)

getLoginDetail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SocialMediaApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getLoginDetail
    api_response = api_instance.get_login_detail_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_login_detail_using_get: %s\n" % e)
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

# **get_share_messages_using_get**
> Wrapper get_share_messages_using_get(authorization, version)

getShareMessages

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SocialMediaApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getShareMessages
    api_response = api_instance.get_share_messages_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->get_share_messages_using_get: %s\n" % e)
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

# **update_social_login_details_using_put**
> Wrapper update_social_login_details_using_put(body, authorization, version)

updateSocialLoginDetails

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.SocialMediaApi()
body = dupr_backend.UserAuthProviderRequest() # UserAuthProviderRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateSocialLoginDetails
    api_response = api_instance.update_social_login_details_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SocialMediaApi->update_social_login_details_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAuthProviderRequest**](UserAuthProviderRequest.md)| request | 
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

