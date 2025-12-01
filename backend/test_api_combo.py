import requests

BASE = "http://127.0.0.1:5000/api"

def test_create_combo():
    payload = {"combo_name": "Combo 1", "description": "Popcorn + Coke", "price": 120000}
    res = requests.post(BASE + "/combo", json=payload)
    print("=== CREATE COMBO ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-" * 50)
    return res.json().get("combo_id")

def test_get_combos():
    res = requests.get(BASE + "/combos")
    print("=== GET ALL COMBOS ===")
    print("Status:", res.status_code)
    print("JSON:", res.json())
    print("-" * 50)

if __name__ == "__main__":
    combo_id = test_create_combo()
    test_get_combos()
