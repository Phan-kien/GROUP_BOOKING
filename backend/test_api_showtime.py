import requests

BASE = "http://127.0.0.1:5000/api"


def test_create_showtime(hall_id, movie_id, date="2025-12-25", start_time="18:30", end_time="21:30"):
    print("=== CREATE SHOWTIME ===")
    payload = {
        "hall_id": hall_id,
        "movie_id": movie_id,
        "date": date,
        "start_time": start_time,
        "end_time": end_time
    }
    try:
        res = requests.post(f"{BASE}/showtime", json=payload)
        print("Status:", res.status_code)
        try:
            json_data = res.json()
            print("JSON:", json_data)
        except Exception:
            print("Response:", res.text)
            json_data = {}
        print("-" * 50)
        return json_data.get("showtime_id")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None


def test_get_showtimes():
    print("=== GET ALL SHOWTIMES ===")
    try:
        res = requests.get(f"{BASE}/showtimes")
        print("Status:", res.status_code)
        try:
            print("JSON:", res.json())
        except Exception:
            print("Response:", res.text)
        print("-" * 50)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


if __name__ == "__main__":
    # Thay hall_id và movie_id bằng dữ liệu thực tế trong DB của bạn
    hall_id = 1
    movie_id = "MOV251203001"

    # Tạo showtime mới
    showtime_id = test_create_showtime(hall_id, movie_id)

    # Lấy tất cả showtimes
    test_get_showtimes()