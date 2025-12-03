# test_api_customer_optionB.py
import requests
import uuid

BASE = "http://127.0.0.1:5000/api"

def generate_cus_id():
    """Tạo cus_id kiểu CUS-UUID"""
    return "CUS-" + str(uuid.uuid4())[:16]

def test_create_customer(name=None, email=None, phone=None):
    print("=== CREATE CUSTOMER ===")
    payload = {
        "cus_id": generate_cus_id(),
        "name": name,
        "email": email,
        "number_phone": phone
    }
    try:
        res = requests.post(f"{BASE}/register", json=payload)
        print("POST status:", res.status_code)
        try:
            print("Response JSON:", res.json())
        except Exception:
            print("Response text:", res.text)
        print("-" * 50)
        return payload["cus_id"] if res.status_code in (200, 201) else None
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

def test_get_customer(cus_id):
    print("=== GET CUSTOMER ===")
    try:
        res = requests.get(f"{BASE}/customer/{cus_id}")
        print("GET status:", res.status_code)
        try:
            print("Response JSON:", res.json())
        except Exception:
            print("Response text:", res.text)
        print("-" * 50)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

if __name__ == "__main__":
    # Tạo customer mới (các field optional)
    cus_id = test_create_customer(name="Nguyen Van A", email="a@example.com", phone="0912345678")

    if cus_id:
        # Lấy thông tin customer vừa tạo
        test_get_customer(cus_id)
    else:
        print("Tạo customer thất bại, không thể GET")
