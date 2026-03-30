import hmac
import hashlib
import json
import requests

# ─── Body ────────────────────────────────────────────────────────────────────
body = {
    "Userid": "USQUAVIDEV",
    "Userpassword": "JQxw@GQ91Y#o8i"
}

# ─── Calcular HMAC-SHA256 ─────────────────────────────────────────────────────
secret_key = "APIBK-Dev-SxVik.xrf4gPD72xKhz"
body_serialized = json.dumps(body, separators=(",", ":"))

hash_alfin = hmac.new(
    secret_key.encode("utf-8"),
    body_serialized.encode("utf-8"),
    hashlib.sha256
).hexdigest()

# ─── Headers ──────────────────────────────────────────────────────────────────
headers = {
    "Content-Type":              "application/json",
    "Canal":                     "ABSERVICES",
    "Usuario":                   "USQUAVIDEV",
    "Device":                    "10.10.10.10",
    "Requerimiento":             "1",
    "token":                     "127554919986E6787C39A56F",
    "Ocp-Apim-Subscription-Key": "5075dc31fe4045d2b0e6b98c8a75c737",
    "X-Azure-APGW":              "APIMDES001",
    "Authorization":             "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiI4NGI5MTdmZi1mZDgwLTQ2NGMtODFiNS0xNmI0YTBiMzI0ODkiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vZTZiNmFmMTktMDA1YS00YzljLTkxYTMtMzdmZWQyY2JhZWQ4L3YyLjAiLCJpYXQiOjE3NzQ5MTI0ODAsIm5iZiI6MTc3NDkxMjQ4MCwiZXhwIjoxNzc0OTE2MzgwLCJhaW8iOiJBU1FBMi84YkFBQUFUaGpIT2RIb2RCSnZKZVJTa2xPclE5THBpN3ZBcm0rcEgySlFyZlI3MGxBPSIsImF6cCI6Ijk0NDljNGJlLWExY2ItNDZmYi1iMzVjLTdmMDA4OTAxZDMzOSIsImF6cGFjciI6IjEiLCJvaWQiOiI0OGRiODk0Yi02ODJlLTQ5NDAtOTI0OS0yMmYwNmEzZWU5MWUiLCJyaCI6IjEuQVh3QUdhLTI1bG9BbkV5Um96Zi0wc3V1MlA4WHVZU0FfVXhHZ2JVV3RLQ3pKSWtBQUFCOEFBLiIsInN1YiI6IjQ4ZGI4OTRiLTY4MmUtNDk0MC05MjQ5LTIyZjA2YTNlZTkxZSIsInRpZCI6ImU2YjZhZjE5LTAwNWEtNGM5Yy05MWEzLTM3ZmVkMmNiYWVkOCIsInV0aSI6IjJ6ZTJ4SmlGWFV5ZXk3YWx2TjVZQUEiLCJ2ZXIiOiIyLjAiLCJ4bXNfZnRkIjoiNWdQNll1dnJrVGZhaVVSWjJXR1U3cjJYSnA1TnFobC1TaDJxUUJzTm9qTUJkWE56YjNWMGFDMWtjMjF6In0.icJ_59FcQShJyv6JhRa5ty7OxOa-amXhvz_EVR8Fah-KQT45cw-WlLijEO4-u37Nb-Y0fB3jIGeCcsNnUd_rz8wQvCJWXaJ-YLl9nY9ZPnqzkR4dDDwxARck3sKtWiUILCzav8GJY2_umXAXSHEBpMf_xbKb7RJqvMx82uAEb3yxgWt2ntP88Xmq5GkQVCRoUxrOzkJL7ULDRqSMomxcqjZOfeA0vKPislSFAAtoOQ2XlyVN9d4J8XZcXngCwMiLZtNPKw-Zk1_nMTfrv2k5fXxSzUPMySh5JleXpVKwG8NcJy6vC7_sUb9E23vyWXoGl5ZYOfZOaAxh3pKEe4sgUg",
    "alfinhash":                 hash_alfin,
}

# ─── Request ──────────────────────────────────────────────────────────────────
response = requests.post(
    url="https://apibaasdev.alfinbanco.pe/api/Authenticate/v1/Execute",
    headers=headers,
    json=body,
    timeout=30
)

# ─── Respuesta ────────────────────────────────────────────────────────────────
print(f"Status:  {response.status_code}")
print(f"Body raw: {response.text}")

if response.text:
    try:
        print(f"Response JSON: {response.json()}")
    except Exception:
        print("Response no es JSON, ver Body raw arriba")
else:
    print("Response: vacía (sin body)")
