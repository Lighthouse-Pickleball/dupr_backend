# dupr_backend.StripeApi

All URIs are relative to *//https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_charge_updates_using_post**](StripeApi.md#account_charge_updates_using_post) | **POST** /stripe/account/{version}/charge | accountChargeUpdates
[**account_checkout_updates_using_post**](StripeApi.md#account_checkout_updates_using_post) | **POST** /stripe/account/{version}/checkout | accountCheckoutUpdates
[**charge_updates_using_post**](StripeApi.md#charge_updates_using_post) | **POST** /stripe/{version}/charge | chargeUpdates
[**checkout_account_payment_intent_using_post**](StripeApi.md#checkout_account_payment_intent_using_post) | **POST** /stripe/account/{version}/payment-intent | checkoutAccountPaymentIntent
[**checkout_payment_intent_using_post**](StripeApi.md#checkout_payment_intent_using_post) | **POST** /stripe/{version}/payment-intent | checkoutPaymentIntent
[**checkout_updates_using_post**](StripeApi.md#checkout_updates_using_post) | **POST** /stripe/{version}/checkout | checkoutUpdates
[**club_account_updates_using_post**](StripeApi.md#club_account_updates_using_post) | **POST** /stripe/account/{version}/updated | clubAccountUpdates
[**invoice_updates_using_post**](StripeApi.md#invoice_updates_using_post) | **POST** /stripe/{version}/invoices | invoiceUpdates
[**subscription_updates_using_post**](StripeApi.md#subscription_updates_using_post) | **POST** /stripe/{version}/subscriptions | subscriptionUpdates

# **account_charge_updates_using_post**
> object account_charge_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

accountChargeUpdates

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # accountChargeUpdates
    api_response = api_instance.account_charge_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->account_charge_updates_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_checkout_updates_using_post**
> object account_checkout_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

accountCheckoutUpdates

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # accountCheckoutUpdates
    api_response = api_instance.account_checkout_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->account_checkout_updates_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_updates_using_post**
> object charge_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

chargeUpdates

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # chargeUpdates
    api_response = api_instance.charge_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->charge_updates_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_account_payment_intent_using_post**
> object checkout_account_payment_intent_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

checkoutAccountPaymentIntent

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # checkoutAccountPaymentIntent
    api_response = api_instance.checkout_account_payment_intent_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->checkout_account_payment_intent_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_payment_intent_using_post**
> object checkout_payment_intent_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

checkoutPaymentIntent

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # checkoutPaymentIntent
    api_response = api_instance.checkout_payment_intent_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->checkout_payment_intent_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_updates_using_post**
> object checkout_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

checkoutUpdates

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # checkoutUpdates
    api_response = api_instance.checkout_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->checkout_updates_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_account_updates_using_post**
> object club_account_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

clubAccountUpdates

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # clubAccountUpdates
    api_response = api_instance.club_account_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->club_account_updates_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_updates_using_post**
> object invoice_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

invoiceUpdates

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # invoiceUpdates
    api_response = api_instance.invoice_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->invoice_updates_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_updates_using_post**
> object subscription_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)

subscriptionUpdates

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.StripeApi()
body = 'body_example' # str | body
authorization = 'Bearer ' # str |  (default to Bearer )
stripe_signature = 'stripe_signature_example' # str | stripe-signature
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # subscriptionUpdates
    api_response = api_instance.subscription_updates_using_post(body, authorization, stripe_signature, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StripeApi->subscription_updates_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| body | 
 **authorization** | **str**|  | [default to Bearer ]
 **stripe_signature** | **str**| stripe-signature | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

