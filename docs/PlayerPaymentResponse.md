# PlayerPaymentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**brackets** | [**List[BracketResponse]**](BracketResponse.md) |  | [optional] 
**display_username** | **bool** |  | [optional] 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**dupr_id** | **str** |  | 
**email** | **str** |  | 
**enable_privacy** | **bool** |  | [optional] 
**event_fee** | **float** |  | 
**event_refunded_amount** | **float** |  | 
**first_name** | **str** |  | 
**formatted_address** | **str** |  | [optional] 
**full_name** | **str** |  | 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**invited** | **bool** |  | [optional] 
**is_logged_in_user** | **bool** |  | [optional] 
**is_player1** | **bool** |  | [optional] 
**is_substitute** | **bool** |  | [optional] 
**last_name** | **str** |  | 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**partner_status** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**ratings** | [**PlayerRatingResponse**](PlayerRatingResponse.md) |  | [optional] 
**registered** | **bool** |  | 
**registration_type** | **str** |  | 
**short_address** | **str** |  | [optional] 
**team_status** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**verified_email** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.player_payment_response import PlayerPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPaymentResponse from a JSON string
player_payment_response_instance = PlayerPaymentResponse.from_json(json)
# print the JSON string representation of the object
print PlayerPaymentResponse.to_json()

# convert the object into a dict
player_payment_response_dict = player_payment_response_instance.to_dict()
# create an instance of PlayerPaymentResponse from a dict
player_payment_response_form_dict = player_payment_response.from_dict(player_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


