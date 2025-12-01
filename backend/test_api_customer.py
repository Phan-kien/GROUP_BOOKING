import requests

BASE = "http://127.0.0.1:5000/api"

def print_response(r):
    print("Status:", r.status_code)
    try:
        print("JSON:", r.json())
    except:
        print("Text:", r.text)
    print("-" * 50)

print("=== REGISTER ===")
r = requests.post(
    BASE + "/register",
    json={
        "name": "kien",
        "email": "kien@gmail.com",
        "number_phone:1234567890"
        "password": "123456"
    }
)
print_response(r)

print("=== LOGIN ===")
r = requests.post(
    BASE + "/login",
    json={
        "email": "kien@gmail.com",
        "password": "123456"
    }
)
print_response(r)
