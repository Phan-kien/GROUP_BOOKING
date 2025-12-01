import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_showtime(hall_id, movie_id):
    print("=== CREATE SHOWTIME ===")
    payload = {
        "hall_id": hall_id,
        "movie_id": movie_id,
        "date": "2025-12-01",
        "start_time": "18:30",
        "end_time": "21:30"
    }
    res = requests.post(BASE + "/showtime", json=payload)
    print("Status:", res.status_code)
    try:
        print("JSON:", res.json())
    except:
        print("Response:", res.text)
    print("--------------------------------------------------")
    if res.status_code == 200:
        return res.json().get("showtime_id")
    return None

def test_get_showtimes():
    print("=== GET ALL SHOWTIMES ===")
    res = requests.get(BASE + "/showtimes")
    print("Status:", res.status_code)
    try:
        print("JSON:", res.json())
    except:
        print("Response:", res.text)
    print("--------------------------------------------------")

if __name__ == "__main__":
    # Thay hall_id và movie_id bằng dữ liệu thực tế
    hall_id = 1
    movie_id = "UUID-AVENGERS"
    showtime_id = test_create_showtime(hall_id, movie_id)
    test_get_showtimes()
