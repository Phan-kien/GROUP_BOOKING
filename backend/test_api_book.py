import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_book():
    payload = {
        "cus_id": 3,
        "ticket_id": 1,
        "payment_id": 1
    }
    res = requests.post(BASE + "/book", json=payload)
    print("=== CREATE BOOK ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-"*50)
    return res.json().get("book_id")

def test_get_books():
    res = requests.get(BASE + "/books")
    print("=== GET ALL BOOKS ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-"*50)

if __name__ == "__main__":
    book_id = test_create_book()
    test_get_books()
