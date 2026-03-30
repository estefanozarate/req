import hmac
import hashlib
import json
import requests

body = {
    "Userid": "USQUAVIDEV",
    "Userpassword": "JQxw@GQ91Y#o8i"
}
secret_key = "APIBK-Dev-SxVik.xrf4gPD72xKhz"
body_serialized = json.dumps(body, separators=(",", ":"))  # Sin espacios, igual que JS
hash_alfin = hmac.new(
    secret_key.encode("utf-8"),
    body_serialized.encode("utf-8"),
    hashlib.sha256
).hexdigest()
headers = {
    "Content-Type":                "application/json",
    "Canal":                       "ABSERVICES",
    "Usuario":                     "USQUAVIDEV",
    "Device":                      "10.10.10.10",
    "Requerimiento":               "1",
    "token":                       "127554919986E6787C39A56F",
    "Ocp-Apim-Subscription-Key":   "5075dc31fe4045d2b0e6b98c8a75c737",
    "X-Azure-APGW":                "APIMDES001",
    "Authorization":               "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9...",
    "alfinhash":                   hash_alfin,
}

BASE_URL = "https://tu-servidor.com"  
response = requests.post(
    url=f"https://apibaasdev.alfinbanco.pe/api/Authenticate/v1/Execute",
    headers=headers,
    json=body,
    #timeout=10
)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
