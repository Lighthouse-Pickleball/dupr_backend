# dupr_backend.AddressApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](AddressApi.md#autocomplete) | **GET** /address/{version}/autocomplete | 
[**delete_user_address**](AddressApi.md#delete_user_address) | **DELETE** /address/{version}/delete | 
[**geocode**](AddressApi.md#geocode) | **GET** /address/{version}/geocode | 
[**place_details**](AddressApi.md#place_details) | **GET** /address/{version}/details | 
[**save_address**](AddressApi.md#save_address) | **PUT** /address/{version}/save | 


# **autocomplete**
> SingleWrapperAutocompletePrediction autocomplete(version, q, st)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_autocomplete_prediction import SingleWrapperAutocompletePrediction
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
    api_instance = dupr_backend.AddressApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    q = 'san' # str | 
    st = '2922eecb-11f9-4d74-8123-ad2fc32078f2' # str | 

    try:
        api_response = api_instance.autocomplete(version, q, st)
        print("The response of AddressApi->autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **q** | **str**|  | 
 **st** | **str**|  | 

### Return type

[**SingleWrapperAutocompletePrediction**](SingleWrapperAutocompletePrediction.md)

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

# **delete_user_address**
> Wrapper delete_user_address(version, id_payload)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.id_payload import IdPayload
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
    api_instance = dupr_backend.AddressApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id_payload = dupr_backend.IdPayload() # IdPayload | 

    try:
        api_response = api_instance.delete_user_address(version, id_payload)
        print("The response of AddressApi->delete_user_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->delete_user_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id_payload** | [**IdPayload**](IdPayload.md)|  | 

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

# **geocode**
> ArrayWrapperGeocodingResult geocode(version, lat, lon)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_geocoding_result import ArrayWrapperGeocodingResult
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
    api_instance = dupr_backend.AddressApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    lat = 16.691543 # float | 
    lon = 74.225591 # float | 

    try:
        api_response = api_instance.geocode(version, lat, lon)
        print("The response of AddressApi->geocode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->geocode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **lat** | **float**|  | 
 **lon** | **float**|  | 

### Return type

[**ArrayWrapperGeocodingResult**](ArrayWrapperGeocodingResult.md)

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

# **place_details**
> SingleWrapperGeocodingResult place_details(version, place_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_geocoding_result import SingleWrapperGeocodingResult
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
    api_instance = dupr_backend.AddressApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    place_id = 'ChIJd7zN_thz54gRnr-lPAaywwo' # str | 

    try:
        api_response = api_instance.place_details(version, place_id)
        print("The response of AddressApi->place_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->place_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **place_id** | **str**|  | 

### Return type

[**SingleWrapperGeocodingResult**](SingleWrapperGeocodingResult.md)

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

# **save_address**
> SingleWrapperIdPayload save_address(version, address_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.address_request import AddressRequest
from dupr_backend.models.single_wrapper_id_payload import SingleWrapperIdPayload
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
    api_instance = dupr_backend.AddressApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    address_request = dupr_backend.AddressRequest() # AddressRequest | 

    try:
        api_response = api_instance.save_address(version, address_request)
        print("The response of AddressApi->save_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->save_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **address_request** | [**AddressRequest**](AddressRequest.md)|  | 

### Return type

[**SingleWrapperIdPayload**](SingleWrapperIdPayload.md)

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

