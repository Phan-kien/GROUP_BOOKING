import requests
import uuid

BASE = "http://127.0.0.1:5000/api"

cus_id = str(uuid.uuid4())

# POST register
payload = {
    "cus_id": cus_id,
    "name": "Nguyen Van A",
    "email": "a@example.com",
    "number_phone": "0912345678"
}

res = requests.post(f"{BASE}/customer/register", json=payload)
print("POST status:", res.status_code)
try:
    print(res.json())
except:
    print("Response text:", res.text)

# GET customer
res = requests.get(f"{BASE}/customer/{cus_id}")
print("GET status:", res.status_code)
try:
    print(res.json())
except:
    print("Response text:", res.text)
