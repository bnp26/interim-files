import urllib3
import json
from json_minify import json_minify
PROVIDER_PAYLOADS = {"ubereats": "uber_sample_payload_2.json", "deliverydudes": "deliverydudes_sample_1.json", "ontray": "ontray_sample_order_2.json", "allset": "allset_sample_order_3.json", "caternow": "caterNow_sample_order_1.json", "doordash": "doordash_sample_order_1.json", "opendining": "open_dining_sample_order_1.json"}

def get_oos_payloads():
    try:
        import json
        payloads = {}
        for name in PROVIDER_PAYLOADS:
            payloads[name] = dict()
            current = payloads[name]
            current["provider"] = name
            current["type"] = "oos"
            with open("../orders-endpoints/sample_json/" + PROVIDER_PAYLOADS[name], "r") as f:
                payload = ""
                for line in f.readlines():
                    payload += line.replace("\n\t", "").strip()
                current["payload"] = payload
                payloads[name] = current
        return payloads
    except Exception as e:
        print e.message

def main():
    import urllib3
    import json

    http = urllib3.PoolManager()
    # lets seed some provider payloads
    payloads = get_oos_payloads()
    print payloads
    for i in payloads:
        data = payloads[i]
        data["payload"] = json_minify(data["payload"])
        data = json.dumps(payloads[i])
        print 'minified: {}'.format(data)
        encoded_data = data
        url = "http://localhost:8080/api/payload/seed"
        headers ={
                "Authorization": "Basic b3JkZXJtYXJrOm1vbmV5cHJpbnRpbmdtYWNoaW5l",
                "Cache-Control": "no-cache",
                "Content-Type": "application/json",
                "Postman-Token": "c9f67ec7-1c41-56eb-be8e-b3c5b57e03a3",
                "X-Appengine-Inbound-Appid": "ordermark-app",
                "ordermark-appid": "ordermark-app"}
        print data
        resp = http.request(
                'POST',
                url,
                body=encoded_data,
                headers=headers)
        print resp.data
main()

