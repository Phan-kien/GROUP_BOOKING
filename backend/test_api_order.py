import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_order():
    payload = {
        "cus_id": "CUS251203001",
        "combo_id": "COM251203001",
        "payment_id": "PAY251203001"
    }
    res = requests.post(BASE + "/order", json=payload)
    print("=== CREATE ORDER ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-" * 50)
    return res.json().get("order_id")

def test_get_orders():
    res = requests.get(BASE + "/orders")
    print("=== GET ALL ORDERS ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-" * 50)

if __name__ == "__main__":
    order_id = test_create_order()
    test_get_orders()
