
curl -X POST -H 'Content-Type: application/json' -H 'Postman-Token: 58d62c69-662e-8235-3c19-7593422a5d2a' -H 'authorization: Basic b3JkZXJtYXJrOm1vbmV5cHJpbnRpbmdtYWNoaW5l' -H 'X-Appengine-Inbound-Appid: ordermark-app' -H 'ordermark-appid: ordermark-app' -d '{
    "confirmation_link": null, 
    "customer": {
        "latitude": 40.7816316, 
        "longitude": -74.023472, 
        "name": "Peter", 
        "phone": "+1 585-721-7787"
    }, 
    "customer_order_id": "706C4", 
    "issues": [], 
    "menu_items": [
        {
            "item_number": 0, 
            "item_id": "e5cf6de9-cf94-4cad-b272-4916a71b4b04", 
            "item_name": "Wings", 
            "quantity": 1, 
            "price": 20.99, 
            "special_instructions": "Extra crispy and RANCH on the side please!!!", 
            "modifiers": [
                {
                    "item_number": 0, 
                    "item_id": "94b19a00-53a1-4914-88c3-526357234dd0", 
                    "item_name": "Choice of Quantity", 
                    "quantity": 1, 
                    "modifiers": [
                        {
                            "item_number": 0, 
                            "item_id": "14d6138a-28d8-4d4d-aacf-f40a9211a3a9", 
                            "item_name": "20 Pieces", 
                            "quantity": 1, 
                            "price": 8.0
                        }
                    ]
                }, 
                {
                    "item_number": 1, 
                    "item_id": "4fd64313-690d-49b6-8c14-b746dcd5d06b", 
                    "item_name": "Choice of Flavor", 
                    "quantity": 1, 
                    "modifiers": [
                        {
                            "item_number": 0, 
                            "item_id": "10ab958f-4cdd-49aa-8bde-d3e586464b3d", 
                            "item_name": "Hot", 
                            "quantity": 1
                        }
                    ]
                }
            ]
        }, 
        {
            "item_number": 1, 
            "item_id": "384f8983-a208-4f2e-8545-a4b0496203b2", 
            "item_name": "New York Cheesecake", 
            "quantity": 1, 
            "price": 6.99
        }, 
        {
            "item_number": 2, 
            "item_id": "e1355c45-8b3b-4761-a803-8bcdcf3153f1", 
            "item_name": "Buffalo Chicken Wrap", 
            "quantity": 1, 
            "price": 12.99
        }, 
        {
            "item_number": 3, 
            "item_id": "7d755a83-3ec1-41e2-890d-71e199c7cde4", 
            "item_name": "Steak Baguette Bites", 
            "quantity": 1, 
            "price": 13.99
        }, 
        {
            "item_number": 4, 
            "item_id": "2c2864ed-ba27-4636-89bc-6207259d43c4", 
            "item_name": "Grilled Chicken Pesto Panini", 
            "quantity": 1, 
            "price": 12.99, 
            "modifiers": [
                {
                    "item_number": 0, 
                    "item_id": "a9408efd-5371-4ceb-a866-b05f9998e9ed", 
                    "item_name": "Choice of Madd Hatter Fries", 
                    "quantity": 1, 
                    "modifiers": [
                        {
                            "item_number": 0, 
                            "item_id": "d58c2e0f-83eb-40db-a530-b51c81ef0c39", 
                            "item_name": "Garlic Parm", 
                            "quantity": 1
                        }
                    ]
                }
            ]
        }
    ], 
    "meta_info": {
        "app_id": "ordermark-app", 
        "confirmation_date": "2018-12-05T01:57:09Z", 
        "email_from": "uber", 
        "email_label": "uber", 
        "email_message_id": "uber", 
        "email_subject": "uber", 
        "email_to": "uber", 
        "is_confirmed": true, 
        "order_type": "O", 
        "original_json": "{\"status\": {\"rushJob\": {\"uuid\": \"f507e76d-2f32-4292-95fb-73b9281c3d42\"}, \"orderJob\": {\"uuid\": \"4a6882c8-e0d3-5f45-a483-d0ca395780fc\", \"currentState\": {\"type\": \"CREATED\", \"timeStarted\": 1543975029579}, \"hasPrepTimeUpdated\": false}, \"workflowUUID\": \"b4e2f718-b58a-4525-b356-b3ffc04706c4\"}, \"estimatedTimes\": {\"estimatedDeliveryTime\": 1543977642035, \"hasCourierBeenWithinPrepTime\": false, \"workflowUUID\": \"b4e2f718-b58a-4525-b356-b3ffc04706c4\", \"estimatedPickupTime\": 1543976229035}, \"restaurantOrder\": {\"storeInstructions\": \"\", \"itemsV2\": [{\"specialInstructions\": \"Extra crispy and RANCH on the side please!!!\", \"uuid\": \"e5cf6de9-cf94-4cad-b272-4916a71b4b04\", \"title\": \"Wings\", \"prices\": 2099, \"customizations\": {\"elements\": [{\"items\": {\"elements\": [{\"price\": 800, \"quantity\": 1, \"uuid\": \"14d6138a-28d8-4d4d-aacf-f40a9211a3a9\", \"title\": \"20 Pieces\"}]}, \"uuid\": \"94b19a00-53a1-4914-88c3-526357234dd0\", \"title\": \"Choice of Quantity\"}, {\"items\": {\"elements\": [{\"price\": 0, \"quantity\": 1, \"uuid\": \"10ab958f-4cdd-49aa-8bde-d3e586464b3d\", \"title\": \"Hot\"}]}, \"uuid\": \"4fd64313-690d-49b6-8c14-b746dcd5d06b\", \"title\": \"Choice of Flavor\"}]}, \"quantity\": 1}, {\"price\": 699, \"quantity\": 1, \"customizations\": {\"elements\": []}, \"uuid\": \"384f8983-a208-4f2e-8545-a4b0496203b2\", \"title\": \"New York Cheesecake\"}, {\"price\": 1299, \"quantity\": 1, \"customizations\": {\"elements\": []}, \"uuid\": \"e1355c45-8b3b-4761-a803-8bcdcf3153f1\", \"title\": \"Buffalo Chicken Wrap\"}, {\"price\": 1399, \"quantity\": 1, \"customizations\": {\"elements\": []}, \"uuid\": \"7d755a83-3ec1-41e2-890d-71e199c7cde4\", \"title\": \"Steak Baguette Bites\"}, {\"price\": 1299, \"quantity\": 1, \"customizations\": {\"elements\": [{\"items\": {\"elements\": [{\"price\": 0, \"quantity\": 1, \"uuid\": \"d58c2e0f-83eb-40db-a530-b51c81ef0c39\", \"title\": \"Garlic Parm\"}]}, \"uuid\": \"a9408efd-5371-4ceb-a866-b05f9998e9ed\", \"title\": \"Choice of Madd Hatter Fries\"}]}, \"uuid\": \"2c2864ed-ba27-4636-89bc-6207259d43c4\", \"title\": \"Grilled Chicken Pesto Panini\"}], \"uuid\": \"b4e2f718-b58a-4525-b356-b3ffc04706c4\", \"isScheduledOrder\": false, \"items\": [{\"specialInstructions\": \"Extra crispy and RANCH on the side please!!!\", \"uuid\": \"e5cf6de9-cf94-4cad-b272-4916a71b4b04\", \"title\": \"Wings\", \"price\": 2099, \"customizations\": [{\"options\": [{\"price\": 800, \"uuid\": \"14d6138a-28d8-4d4d-aacf-f40a9211a3a9\", \"title\": \"20 Pieces\"}], \"uuid\": \"94b19a00-53a1-4914-88c3-526357234dd0\", \"title\": \"Choice of Quantity\"}, {\"options\": [{\"price\": 0, \"uuid\": \"10ab958f-4cdd-49aa-8bde-d3e586464b3d\", \"title\": \"Hot\"}], \"uuid\": \"4fd64313-690d-49b6-8c14-b746dcd5d06b\", \"title\": \"Choice of Flavor\"}], \"quantity\": 1}, {\"price\": 699, \"quantity\": 1, \"customizations\": [], \"uuid\": \"384f8983-a208-4f2e-8545-a4b0496203b2\", \"title\": \"New York Cheesecake\"}, {\"price\": 1299, \"quantity\": 1, \"customizations\": [], \"uuid\": \"e1355c45-8b3b-4761-a803-8bcdcf3153f1\", \"title\": \"Buffalo Chicken Wrap\"}, {\"price\": 1399, \"quantity\": 1, \"customizations\": [], \"uuid\": \"7d755a83-3ec1-41e2-890d-71e199c7cde4\", \"title\": \"Steak Baguette Bites\"}, {\"price\": 1299, \"quantity\": 1, \"customizations\": [{\"options\": [{\"price\": 0, \"uuid\": \"d58c2e0f-83eb-40db-a530-b51c81ef0c39\", \"title\": \"Garlic Parm\"}], \"uuid\": \"a9408efd-5371-4ceb-a866-b05f9998e9ed\", \"title\": \"Choice of Madd Hatter Fries\"}], \"uuid\": \"2c2864ed-ba27-4636-89bc-6207259d43c4\", \"title\": \"Grilled Chicken Pesto Panini\"}], \"marketplaceCharges\": [{\"rawValue\": 6.49, \"key\": \"booking_fee\"}], \"createdAt\": 1543975029579, \"deliveryInstructions\": \"\", \"customerInfo\": {\"lastName\": \"\", \"mobileCountryIso2\": \"US\", \"firstName\": \"Peter\", \"phone\": \"+1 585-721-7787\"}, \"fulfillmentType\": \"DELIVERY\", \"shoppingCart\": {\"items\": [{\"specialInstructions\": \"Extra crispy and RANCH on the side please!!!\", \"title\": \"Wings\", \"price\": 1299, \"customizationV2s\": [{\"childOptions\": {\"options\": [{\"customizationV2List\": [], \"price\": 800, \"quantity\": 1, \"uuid\": \"14d6138a-28d8-4d4d-aacf-f40a9211a3a9\", \"title\": \"20 Pieces\"}]}, \"uuid\": \"94b19a00-53a1-4914-88c3-526357234dd0\", \"title\": \"Choice of Quantity\"}, {\"childOptions\": {\"options\": [{\"customizationV2List\": [], \"price\": 0, \"quantity\": 1, \"uuid\": \"10ab958f-4cdd-49aa-8bde-d3e586464b3d\", \"title\": \"Hot\"}]}, \"uuid\": \"4fd64313-690d-49b6-8c14-b746dcd5d06b\", \"title\": \"Choice of Flavor\"}], \"skuUUID\": \"e5cf6de9-cf94-4cad-b272-4916a71b4b04\", \"quantity\": 1}, {\"price\": 699, \"title\": \"New York Cheesecake\", \"skuUUID\": \"384f8983-a208-4f2e-8545-a4b0496203b2\", \"customizationV2s\": [], \"quantity\": 1}, {\"price\": 1299, \"title\": \"Buffalo Chicken Wrap\", \"skuUUID\": \"e1355c45-8b3b-4761-a803-8bcdcf3153f1\", \"customizationV2s\": [], \"quantity\": 1}, {\"price\": 1399, \"title\": \"Steak Baguette Bites\", \"skuUUID\": \"7d755a83-3ec1-41e2-890d-71e199c7cde4\", \"customizationV2s\": [], \"quantity\": 1}, {\"price\": 1299, \"title\": \"Grilled Chicken Pesto Panini\", \"skuUUID\": \"2c2864ed-ba27-4636-89bc-6207259d43c4\", \"customizationV2s\": [{\"childOptions\": {\"options\": [{\"customizationV2List\": [], \"price\": 0, \"quantity\": 1, \"uuid\": \"d58c2e0f-83eb-40db-a530-b51c81ef0c39\", \"title\": \"Garlic Parm\"}]}, \"uuid\": \"a9408efd-5371-4ceb-a866-b05f9998e9ed\", \"title\": \"Choice of Madd Hatter Fries\"}], \"quantity\": 1}], \"serializedTrackingCodes\": \"[\\\"{\\\\\\\"uuid\\\\\\\":\\\\\\\"395ab425-4d0e-45ee-a656-9e48eb7bba64\\\\\\\",\\\\\\\"codeType\\\\\\\":\\\\\\\"STORE\\\\\\\",\\\\\\\"metaInfo\\\\\\\":{\\\\\\\"pluginName\\\\\\\":\\\\\\\"SuggestedCart\\\\\\\"},\\\\\\\"storePayload\\\\\\\":{\\\\\\\"storeUUID\\\\\\\":\\\\\\\"9f62cbb9-a14f-4d3b-a494-fb30833ba6ef\\\\\\\"}}\\\"]\", \"storeInstructions\": \"\"}, \"deliveryLocation\": {\"latitude\": 40.7816316, \"longitude\": -74.023472, \"address\": {\"city\": \"\", \"title\": \"528 47th St\", \"address1\": \"528 47th St, Union City, NJ 07087, USA\", \"region\": \"\", \"aptOrSuite\": \"3C\", \"country\": \"\", \"postalCode\": \"\"}}, \"preparationTime\": 1543976229000, \"displayId\": \"706C4\", \"checkoutInfo\": [{\"rawValue\": 67.95, \"key\": \"subtotal\"}, {\"rawValue\": 4.51, \"key\": \"tax\"}, {\"rawValue\": 72.46000000000001, \"key\": \"total\"}], \"foodPreparationState\": \"SENT_TO_KITCHEN\"}}", 
        "provider_name": "ubereats"
    }, 
    "miscellaneous": {}, 
    "order": {
        "adjustments_detail": [], 
        "cancelled": false, 
        "delivery_by": "2018-12-05T02:17:09Z", 
        "discounts": 0.0, 
        "discounts_detail": [], 
        "donations_detail": [], 
        "is_revision": false, 
        "order_id": "b4e2f718-b58a-4525-b356-b3ffc04706c4", 
        "payment_method_code": "P", 
        "payment_method_description": "Prepaid", 
        "placed_date": "2018-12-05T01:57:09Z", 
        "requested_date_label": "Prepare by", 
        "sales_tax": 4.51, 
        "service_type_code": "D", 
        "service_type_description": "Delivery", 
        "subtotal": 67.95, 
        "total": 72.46
    }, 
    "restaurant": {}
}' localhost:8080/_ah/push-handlers/order/new
echo curl complete
