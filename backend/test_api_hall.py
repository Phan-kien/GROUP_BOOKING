import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_hall():
    print("=== CREATE HALL ===")
    payload = {
        "cinema_id": "CIN251203001",        # ID cinema đã tồn tại trong DB
        "hall_name": "Hall A"
    }
    res = requests.post(BASE + "/hall", json=payload)
    print("Status:", res.status_code)
    try:
        print("JSON:", res.json())
    except:
        print("Response:", res.text)
    print("--------------------------------------------------")
    if res.status_code == 200:
        return res.json().get("hall_id")
    return None

def test_get_halls():
    print("=== GET ALL HALLS ===")
    res = requests.get(BASE + "/halls")
    print("Status:", res.status_code)
    try:
        print("JSON:", res.json())
    except:
        print("Response:", res.text)
    print("--------------------------------------------------")

if __name__ == "__main__":
    hall_id = test_create_hall()
    test_get_halls()
