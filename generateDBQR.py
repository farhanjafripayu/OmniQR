import http.client
import urllib.parse
import hashlib
import json  # Add this line to import the json module

def generate_dynamic_bharat_qr(transaction_id, transaction_amount, merchant_vpa, expiry_time,
                                qr_name, qr_city, qr_pincode, customer_name, customer_city,
                                customer_pincode, customer_phone, customer_email, customer_address,
                                udf3, udf4, udf5):
    key = "smsplus"
    salt = "ibib0"
    command = "generate_dynamic_bharat_qr"
    
    var1_data = {
        'transactionId': transaction_id,
        'transactionAmount': transaction_amount,
        'merchantVpa': merchant_vpa,
        'expiryTime': expiry_time,
        'qrName': qr_name,
        'qrCity': qr_city,
        'qrPinCode': qr_pincode,
        'customerName': customer_name,
        'customerCity': customer_city,
        'customerPinCode': customer_pincode,
        'customerPhone': customer_phone,
        'customerEmail': customer_email,
        'customerAddress': customer_address,
        'udf3': udf3,
        'udf4': udf4,
        'udf5': udf5,
        'outputType': 'string'
    }
    
    var1_json = json.dumps(var1_data)
    
    # Concatenate key, command, var1, and salt
    concat_string = f"{key}|{command}|{var1_json}|{salt}".lower()
    print(concat_string)
    # Calculate SHA512 hash
    sha512_hash = hashlib.sha512(concat_string.encode()).hexdigest()
    print(sha512_hash)
    payload = urllib.parse.urlencode({
        'command': command,
        'key': key,
        'hash': sha512_hash,
        'var1': var1_json
    })

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    conn = http.client.HTTPSConnection("info.payu.in")
    conn.request("POST", "/merchant/postservice.php?form=2", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()

    return data.decode("utf-8")

# Example usage:
response = generate_dynamic_bharat_qr(
    transaction_id="DBQR1981",
    transaction_amount="1",
    merchant_vpa="gauravdua1.payu@indus",
    expiry_time="3600",
    qr_name="payu",
    qr_city="Gurgaon",
    qr_pincode="122001",
    customer_name="Ravi",
    customer_city="Ranchi",
    customer_pincode="834001",
    customer_phone="7800078000",
    customer_email="hello@payu.in",
    customer_address="Ggn",
    udf3="deliveryboy1",
    udf4="sector14",
    udf5="cod"
)

print(response)
