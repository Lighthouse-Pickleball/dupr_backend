# dupr_backend.AddressApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete_using_get**](AddressApi.md#autocomplete_using_get) | **GET** /address/{version}/autocomplete | autocomplete
[**delete_user_address_using_delete**](AddressApi.md#delete_user_address_using_delete) | **DELETE** /address/{version}/delete | deleteUserAddress
[**geocode_using_get**](AddressApi.md#geocode_using_get) | **GET** /address/{version}/geocode | geocode
[**place_details_using_get**](AddressApi.md#place_details_using_get) | **GET** /address/{version}/details | placeDetails
[**save_address_using_put**](AddressApi.md#save_address_using_put) | **PUT** /address/{version}/save | saveAddress


# **autocomplete_using_get**
> SingleWrapperOfArrayOfAutocompletePrediction autocomplete_using_get(q, st, version)

autocomplete

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_array_of_autocomplete_prediction import SingleWrapperOfArrayOfAutocompletePrediction
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
    api_instance = dupr_backend.AddressApi(api_client)
    q = 'san' # str | q
    st = '2922eecb-11f9-4d74-8123-ad2fc32078f2' # str | st
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # autocomplete
        api_response = api_instance.autocomplete_using_get(q, st, version)
        print("The response of AddressApi->autocomplete_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->autocomplete_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| q | 
 **st** | **str**| st | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfArrayOfAutocompletePrediction**](SingleWrapperOfArrayOfAutocompletePrediction.md)

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

# **delete_user_address_using_delete**
> Wrapper delete_user_address_using_delete(authorization, version, request)

deleteUserAddress

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.id_payload import IdPayload
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
    api_instance = dupr_backend.AddressApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.IdPayload() # IdPayload | request

    try:
        # deleteUserAddress
        api_response = api_instance.delete_user_address_using_delete(authorization, version, request)
        print("The response of AddressApi->delete_user_address_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->delete_user_address_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**IdPayload**](IdPayload.md)| request | 

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

# **geocode_using_get**
> ArrayWrapperOfGeocodingResult geocode_using_get(lat, lon, version)

geocode

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_geocoding_result import ArrayWrapperOfGeocodingResult
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
    api_instance = dupr_backend.AddressApi(api_client)
    lat = 16.691543 # float | lat
    lon = 74.225591 # float | lon
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # geocode
        api_response = api_instance.geocode_using_get(lat, lon, version)
        print("The response of AddressApi->geocode_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->geocode_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| lat | 
 **lon** | **float**| lon | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfGeocodingResult**](ArrayWrapperOfGeocodingResult.md)

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

# **place_details_using_get**
> SingleWrapperOfGeocodingResult place_details_using_get(place_id, version)

placeDetails

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_geocoding_result import SingleWrapperOfGeocodingResult
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
    api_instance = dupr_backend.AddressApi(api_client)
    place_id = 'ChIJd7zN_thz54gRnr-lPAaywwo' # str | placeId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # placeDetails
        api_response = api_instance.place_details_using_get(place_id, version)
        print("The response of AddressApi->place_details_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->place_details_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_id** | **str**| placeId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfGeocodingResult**](SingleWrapperOfGeocodingResult.md)

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

# **save_address_using_put**
> SingleWrapperOfIdPayload save_address_using_put(version, request)

saveAddress

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.address_request import AddressRequest
from dupr_backend.models.single_wrapper_of_id_payload import SingleWrapperOfIdPayload
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
    api_instance = dupr_backend.AddressApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.AddressRequest() # AddressRequest | request

    try:
        # saveAddress
        api_response = api_instance.save_address_using_put(version, request)
        print("The response of AddressApi->save_address_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressApi->save_address_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**AddressRequest**](AddressRequest.md)| request | 

### Return type

[**SingleWrapperOfIdPayload**](SingleWrapperOfIdPayload.md)

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

