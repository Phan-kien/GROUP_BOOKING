import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_ticket():
    payload = {
        "price": 120000,
        "seat": "A1",
        "cus_id": 3,
        "showtime_id": 1,
        "payment_id": 1
    }
    res = requests.post(BASE + "/ticket", json=payload)
    print("=== CREATE TICKET ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-"*50)
    return res.json().get("ticket_id")

def test_get_tickets():
    res = requests.get(BASE + "/tickets")
    print("=== GET ALL TICKETS ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-"*50)

if __name__ == "__main__":
    ticket_id = test_create_ticket()
    test_get_tickets()
