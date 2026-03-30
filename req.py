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
    "Authorization":             "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiI4NGI5MTdmZi1mZDgwLTQ2NGMtODFiNS0xNmI0YTBiMzI0ODkiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vZTZiNmFmMTktMDA1YS00YzljLTkxYTMtMzdmZWQyY2JhZWQ4L3YyLjAiLCJpYXQiOjE3NzQ5MTA3MjksIm5iZiI6MTc3NDkxMDcyOSwiZXhwIjoxNzc0OTE0NjI5LCJhaW8iOiJBU1FBMi84YkFBQUFUZXZ1UWFJdDE5dkRtbUJTY3hSaytQTzNOcXd4K3VMWGRCMWxLKytsZys4PSIsImF6cCI6Ijk0NDljNGJlLWExY2ItNDZmYi1iMzVjLTdmMDA4OTAxZDMzOSIsImF6cGFjciI6IjEiLCJvaWQiOiI0OGRiODk0Yi02ODJlLTQ5NDAtOTI0OS0yMmYwNmEzZWU5MWUiLCJyaCI6IjEuQVh3QUdhLTI1bG9BbkV5Um96Zi0wc3V1MlA4WHVZU0FfVXhHZ2JVV3RLQ3pKSWtBQUFCOEFBLiIsInN1YiI6IjQ4ZGI4OTRiLTY4MmUtNDk0MC05MjQ5LTIyZjA2YTNlZTkxZSIsInRpZCI6ImU2YjZhZjE5LTAwNWEtNGM5Yy05MWEzLTM3ZmVkMmNiYWVkOCIsInV0aSI6IndtOWV2cW81NGstMTNLVm04Y0pBQUEiLCJ2ZXIiOiIyLjAiLCJ4bXNfZnRkIjoiMVlYM1JtMzRieHVVMzdmR0NMS3o4SVJRb0ZUZzQzWHpBTG5xMHg4TUhCQUJkWE4zWlhOME15MWtjMjF6In0.HxANLgqcJcNoAkFTYa16eO-w0Ax7aJgpcan3rcq24iZsOZp8s-n58vXXYE_SkMAz-LbsLk_aZAO0PWGfy4o7Lj027NhGsbixt6oSr8jri-eFbBhKZWIQSB5pMaKOAM-93dCuFPCZYUgDoUEAxcvHi5aXB8VP-8yXmpE0whFL_A1xX2ZnRulouWNexim7QuatVhAOravshtVmd3OuHqlnkBjHhdaDiI1KteaFLsQ9CGm5IjTd_6FhEoZnku8X3Bc_y2CYl_3yHt8VfBRlBy-SBTP57cdI1yXu1BIcbhMfV8egLyBz2Yk-lk3-p0PTqUqIpWKkeXOmHarnEzEp1HffgA",
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
