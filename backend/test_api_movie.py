import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_movie():
    print("=== CREATE MOVIE ===")
    payload = {
        "title": "Avengers: Endgame",
        "duration": 181,
        "genre": "Action",
        "release_date": "2019-04-26",
        "rating": 8.4
    }
    res = requests.post(BASE + "/movie", json=payload)
    print("Status:", res.status_code)
    try:
        print("JSON:", res.json())
    except:
        print("Response:", res.text)
    print("--------------------------------------------------")
    if res.status_code == 200:
        return res.json().get("movie_id")
    return None

def test_get_movies():
    print("=== GET ALL MOVIES ===")
    res = requests.get(BASE + "/movies")
    print("Status:", res.status_code)
    try:
        print("JSON:", res.json())
    except:
        print("Response:", res.text)
    print("--------------------------------------------------")

if __name__ == "__main__":
    movie_id = test_create_movie()
    test_get_movies()
