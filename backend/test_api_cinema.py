import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_cinema():
    print("=== CREATE CINEMA ===")
    payload = {
        "cinema_name": "CGV Vincom",
        "address": "Hà Nội"
    }
    res = requests.post(BASE + "/cinema", json=payload)
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-" * 50)
    return res.json().get("cinema_id")

def test_get_cinemas():
    print("=== GET CINEMAS ===")
    res = requests.get(BASE + "/cinemas")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-" * 50)

if __name__ == "__main__":
    # Tạo cinema mới
    cinema_id = test_create_cinema()

    # Lấy danh sách cinema
    test_get_cinemas()
