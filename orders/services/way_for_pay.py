import requests
import random
# API = "https://sandbox.wayforpay.com"
import hmac
import hashlib
API = "https://api.wayforpay.com/api"


# Базовий ключ, тому не ховаю
SECRET_KEY_TEST = "flk3409refn54t54t*FNJRET"

def reques_to_api(parametrss):
    end = random.randint(0,100000)
    # end = 14701
    order_id="test_order_for_shopHub" + str(end)

    products = []
    counts = []
    prices = []
    total_price = parametrss[0]["total_price"]
    merchantSignature_str = f"test_merch_n1;www.shophub.com;{order_id};1421412898;{total_price};UAH;"
    for param in parametrss:
        products.append(param["name"])
        counts.append(param["count"])
        prices.append(param["price"])

    

    for product in products:
        merchantSignature_str += f"{product};"
    for count in counts:
        merchantSignature_str += f"{count};"
    for price in prices:
        merchantSignature_str += f"{price};"
    merchantSignature_str = merchantSignature_str[:-1]

    merchant_signature = hmac.new(SECRET_KEY_TEST.encode('utf-8'),
                                merchantSignature_str.encode('utf-8'),
                                hashlib.md5).hexdigest()

    json_query = {
    "transactionType":"CREATE_INVOICE",
    "merchantAccount":"test_merch_n1",
    "merchantDomainName":"www.shophub.com",
    "merchantSignature":merchant_signature,
    "apiVersion":1,
    "orderReference":order_id,
    "orderDate":1421412898,
    "amount":total_price,
    "currency":"UAH",
    "productName":products,
    "productPrice":prices,
    "productCount":counts
    }
    

    response = requests.post(API,json=json_query).json()

    return response["invoiceUrl"]

def check():
    # string = "test_merch_n1;www.shophub.com;test_order_for_shopHub14702;1421412898;439587.0;UAH;OnePlus 11;Sony Xperia 1 V;9;5;30799.0;40599.0"
    string = "test_merch_n1;www.shophub.com;test_order_for_shopHub14702;1421412898;439587.00;UAH;OnePlus 11;Sony Xperia 1 V;9.0;5.0;30799.00;40599.00"
    hash_value = hmac.new(SECRET_KEY_TEST.encode(), string.encode(), hashlib.md5).hexdigest()

    query_json = {
        
    "transactionType": "CREATE_INVOICE",
    "merchantAccount": "test_merch_n1",
    "merchantDomainName": "www.shophub.com",
    "merchantSignature": hash_value,
    "apiVersion": 1,
    "orderReference": "test_order_for_shopHub14702",
    "orderDate": 1421412898,
    "amount": 439587.0,
    "currency": "UAH",
    "productName": ["OnePlus 11", "Sony Xperia 1 V"],
    "productPrice": [30799.0, 40599.0],
    "productCount": [9, 5]        
    }



    

    print("merchantSignature:", hash_value)
    response = requests.post(API,json=query_json).json()
    print(response)

# check()
# reques_to_api()
# "4941ea0c7f5b4833c2bd06b1fefcdc0b"
# "2d838772256b86faaee8dd8b9f495abd"
# "4058071f78581862ccdb857fd2841d9e"