import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_cinema():
    print("=== CREATE CINEMA ===")
    payload = {
        "cinema_name": "CGV Vida",
        "address": "Hà Nội"
    }
    res = requests.post(BASE + "/cinema", json=payload)
    print("Status:", res.status_code)
    try:
        json_data = res.json()
        print("JSON:", json_data)
        return json_data.get("cinema_id")
    except Exception as e:
        print("Failed to parse JSON:", e)
        print("Response text:", res.text)
        return None
    finally:
        print("-" * 50)

def test_get_cinemas():
    print("=== GET CINEMAS ===")
    res = requests.get(BASE + "/cinemas")
    print("Status:", res.status_code)
    try:
        print("JSON:", res.json())
    except Exception as e:
        print("Failed to parse JSON:", e)
        print("Response text:", res.text)
    finally:
        print("-" * 50)

if __name__ == "__main__":
    # Tạo cinema mới
    cinema_id = test_create_cinema()

    # Lấy danh sách cinema
    test_get_cinemas()
