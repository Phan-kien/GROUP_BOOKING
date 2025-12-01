import requests
from datetime import datetime

BASE = "http://127.0.0.1:5000/api"

def test_create_payment():
    payload = {
        "cus_id": 3,
        "amount": 200000,
        "payment_paid": True,
        "status": "Thành công",
        "method": "Tiền mặt"
    }
    res = requests.post(BASE + "/payment", json=payload)
    print("=== CREATE PAYMENT ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-" * 50)
    return res.json().get("payment_id")

def test_get_payments():
    res = requests.get(BASE + "/payments")
    print("=== GET ALL PAYMENTS ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-" * 50)

if __name__ == "__main__":
    payment_id = test_create_payment()
    test_get_payments()
