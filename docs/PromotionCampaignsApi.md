# dupr_backend.PromotionCampaignsApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_eligibility**](PromotionCampaignsApi.md#check_eligibility) | **POST** /admin/promotions/eligibility | 
[**create_product_group**](PromotionCampaignsApi.md#create_product_group) | **PUT** /admin/promotions/product | 
[**create_promotion**](PromotionCampaignsApi.md#create_promotion) | **PUT** /admin/promotions/create | 
[**delete_promotion**](PromotionCampaignsApi.md#delete_promotion) | **DELETE** /admin/promotions | 
[**get_all_products**](PromotionCampaignsApi.md#get_all_products) | **GET** /admin/promotions/products | 
[**get_all_promotions**](PromotionCampaignsApi.md#get_all_promotions) | **GET** /admin/promotions/all | 
[**get_eligible_promotions_by_client_key**](PromotionCampaignsApi.md#get_eligible_promotions_by_client_key) | **POST** /admin/promotions/eligibility/clientKey | 
[**get_promotion_by_id**](PromotionCampaignsApi.md#get_promotion_by_id) | **GET** /admin/promotions | 
[**update_promotion**](PromotionCampaignsApi.md#update_promotion) | **PUT** /admin/promotions/update | 


# **check_eligibility**
> ResultBoolean check_eligibility(check_promotion_eligibility_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.check_promotion_eligibility_request import CheckPromotionEligibilityRequest
from dupr_backend.models.result_boolean import ResultBoolean
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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)
    check_promotion_eligibility_request = dupr_backend.CheckPromotionEligibilityRequest() # CheckPromotionEligibilityRequest | 

    try:
        api_response = api_instance.check_eligibility(check_promotion_eligibility_request)
        print("The response of PromotionCampaignsApi->check_eligibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->check_eligibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_promotion_eligibility_request** | [**CheckPromotionEligibilityRequest**](CheckPromotionEligibilityRequest.md)|  | 

### Return type

[**ResultBoolean**](ResultBoolean.md)

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

# **create_product_group**
> object create_product_group(promotion_product_create_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.promotion_product_create_request import PromotionProductCreateRequest
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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)
    promotion_product_create_request = dupr_backend.PromotionProductCreateRequest() # PromotionProductCreateRequest | 

    try:
        api_response = api_instance.create_product_group(promotion_product_create_request)
        print("The response of PromotionCampaignsApi->create_product_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->create_product_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_product_create_request** | [**PromotionProductCreateRequest**](PromotionProductCreateRequest.md)|  | 

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

# **create_promotion**
> object create_promotion(promotion_campaign_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.promotion_campaign_request import PromotionCampaignRequest
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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)
    promotion_campaign_request = dupr_backend.PromotionCampaignRequest() # PromotionCampaignRequest | 

    try:
        api_response = api_instance.create_promotion(promotion_campaign_request)
        print("The response of PromotionCampaignsApi->create_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->create_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_campaign_request** | [**PromotionCampaignRequest**](PromotionCampaignRequest.md)|  | 

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

# **delete_promotion**
> object delete_promotion(delete_promotion_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.delete_promotion_request import DeletePromotionRequest
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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)
    delete_promotion_request = dupr_backend.DeletePromotionRequest() # DeletePromotionRequest | 

    try:
        api_response = api_instance.delete_promotion(delete_promotion_request)
        print("The response of PromotionCampaignsApi->delete_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->delete_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_promotion_request** | [**DeletePromotionRequest**](DeletePromotionRequest.md)|  | 

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

# **get_all_products**
> object get_all_products()

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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)

    try:
        api_response = api_instance.get_all_products()
        print("The response of PromotionCampaignsApi->get_all_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->get_all_products: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **get_all_promotions**
> object get_all_promotions()

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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)

    try:
        api_response = api_instance.get_all_promotions()
        print("The response of PromotionCampaignsApi->get_all_promotions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->get_all_promotions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **get_eligible_promotions_by_client_key**
> ResultString get_eligible_promotions_by_client_key(get_eligible_promotions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.get_eligible_promotions_request import GetEligiblePromotionsRequest
from dupr_backend.models.result_string import ResultString
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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)
    get_eligible_promotions_request = dupr_backend.GetEligiblePromotionsRequest() # GetEligiblePromotionsRequest | 

    try:
        api_response = api_instance.get_eligible_promotions_by_client_key(get_eligible_promotions_request)
        print("The response of PromotionCampaignsApi->get_eligible_promotions_by_client_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->get_eligible_promotions_by_client_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_eligible_promotions_request** | [**GetEligiblePromotionsRequest**](GetEligiblePromotionsRequest.md)|  | 

### Return type

[**ResultString**](ResultString.md)

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

# **get_promotion_by_id**
> object get_promotion_by_id(get_promotions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.get_promotions_request import GetPromotionsRequest
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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)
    get_promotions_request = dupr_backend.GetPromotionsRequest() # GetPromotionsRequest | 

    try:
        api_response = api_instance.get_promotion_by_id(get_promotions_request)
        print("The response of PromotionCampaignsApi->get_promotion_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->get_promotion_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_promotions_request** | [**GetPromotionsRequest**](GetPromotionsRequest.md)|  | 

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

# **update_promotion**
> object update_promotion(promotion_campaign)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.promotion_campaign import PromotionCampaign
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
    api_instance = dupr_backend.PromotionCampaignsApi(api_client)
    promotion_campaign = dupr_backend.PromotionCampaign() # PromotionCampaign | 

    try:
        api_response = api_instance.update_promotion(promotion_campaign)
        print("The response of PromotionCampaignsApi->update_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCampaignsApi->update_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_campaign** | [**PromotionCampaign**](PromotionCampaign.md)|  | 

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

