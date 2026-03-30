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
    "Authorization":             "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiIxNTY4MjVjOC1kMmM0LTQ5M2ItOWMxNi1lYTRlZjA1MDkzYWYiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vZTZiNmFmMTktMDA1YS00YzljLTkxYTMtMzdmZWQyY2JhZWQ4L3YyLjAiLCJpYXQiOjE3NzQ5MTIzMTgsIm5iZiI6MTc3NDkxMjMxOCwiZXhwIjoxNzc0OTE2MjE4LCJhaW8iOiJBU1FBMi84YkFBQUFLdjRoOTFaYnYybWgycmltVm9yWURPUG5DbFMxd3BVVWdPRHE5RWd5ZEkwPSIsImF6cCI6ImMxZDYzYzRmLTJjOWYtNDBkYS04NzJhLTNmMTJmNGEzMjg1NiIsImF6cGFjciI6IjEiLCJvaWQiOiJlMzQyNzJlZS1mOTE5LTQ5ZGQtOGQ3MS1hZGZlYWNmZTI0MjciLCJyaCI6IjEuQVh3QUdhLTI1bG9BbkV5Um96Zi0wc3V1Mk1nbGFCWEUwanRKbkJicVR2QlFrNjhBQUFCOEFBLiIsInN1YiI6ImUzNDI3MmVlLWY5MTktNDlkZC04ZDcxLWFkZmVhY2ZlMjQyNyIsInRpZCI6ImU2YjZhZjE5LTAwNWEtNGM5Yy05MWEzLTM3ZmVkMmNiYWVkOCIsInV0aSI6IkNvb3JGU3ZnblU2NzZnRlR3OUJYQUEiLCJ2ZXIiOiIyLjAiLCJ4bXNfZnRkIjoiY0hveHMwS0w0M3JaemRGSU1xNnZBVlVaVTVmenhBaWpEeDJ4M1pNNWdqQUJkWE51YjNKMGFDMWtjMjF6In0.VE3mDjY2kvNQP_hnE2nNk8ZUE8Dky_dXeIZ6lFnIWGBAdNGJkNa0bkEXrY8ubOHXUXqUU77mChgaEV1sGQROdoEo3pekkpYJI7kVXGxbOk1JmUOf6IBP_liSbrKLCy9paEpYUVmii9g589AA1JqCrhyR6rJlmHVcF5WGPHyPun6InyZudTh3ChutWUewWiAxsoYEgaCLlXjCK184P3iMdMunxi-ndReuBrAQo9ZnGGzVHcjjEPaMcUVzkwi3_iRhdesOd8XmUbggQP4gY5V2_WSBO3IUSDJk7RpdMuLr0W3LWeGvnElS9e1Iqe4_J596zOT5nYHJNJyN7oHDGlqmZQ",
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
