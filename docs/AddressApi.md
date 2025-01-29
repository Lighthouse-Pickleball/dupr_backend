# dupr_backend.AddressApi

All URIs are relative to *https://backend.mydupr.com/*

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
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AddressApi()
q = 'q_example' # str | q
st = 'st_example' # str | st
version = 'version_example' # str | version

try:
    # autocomplete
    api_response = api_instance.autocomplete_using_get(q, st, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->autocomplete_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| q | 
 **st** | **str**| st | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfArrayOfAutocompletePrediction**](SingleWrapperOfArrayOfAutocompletePrediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_address_using_delete**
> Wrapper delete_user_address_using_delete(body, authorization, version)

deleteUserAddress

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AddressApi()
body = dupr_backend.IdPayload() # IdPayload | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # deleteUserAddress
    api_response = api_instance.delete_user_address_using_delete(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->delete_user_address_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdPayload**](IdPayload.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geocode_using_get**
> ArrayWrapperOfGeocodingResult geocode_using_get(lat, lon, version)

geocode

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AddressApi()
lat = 1.2 # float | lat
lon = 1.2 # float | lon
version = 'version_example' # str | version

try:
    # geocode
    api_response = api_instance.geocode_using_get(lat, lon, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->geocode_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| lat | 
 **lon** | **float**| lon | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfGeocodingResult**](ArrayWrapperOfGeocodingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_details_using_get**
> SingleWrapperOfGeocodingResult place_details_using_get(place_id, version)

placeDetails

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AddressApi()
place_id = 'place_id_example' # str | placeId
version = 'version_example' # str | version

try:
    # placeDetails
    api_response = api_instance.place_details_using_get(place_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->place_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_id** | **str**| placeId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfGeocodingResult**](SingleWrapperOfGeocodingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_address_using_put**
> SingleWrapperOfIdPayload save_address_using_put(body, version)

saveAddress

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AddressApi()
body = dupr_backend.AddressRequest() # AddressRequest | request
version = 'version_example' # str | version

try:
    # saveAddress
    api_response = api_instance.save_address_using_put(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->save_address_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddressRequest**](AddressRequest.md)| request | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfIdPayload**](SingleWrapperOfIdPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

