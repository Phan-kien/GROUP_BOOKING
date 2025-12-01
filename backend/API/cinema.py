from flask import Blueprint,Flask, request, jsonify
from backend.BUSINESS.CinemaBusiness import CinemaBusiness

#app = Flask(__name__)
cinema_api = Blueprint("cinema_api", __name__)
cinema_business = CinemaBusiness()

@cinema_api.route("/cinemas", methods=["GET"])
def get_cinemas():
    cinemas = cinema_business.get_all_cinemas()
    data = [{"cinema_id": c.cinema_id, "cinema_name": c.cinema_name, "address": c.address} for c in cinemas]
    return jsonify(data), 200

@cinema_api.route("/cinema", methods=["POST"])
def create_cinema():
    data = request.json
    if not data or "cinema_name" not in data:
        return jsonify({"error": "Thiếu cinema_name"}), 400
    name = data.get("cinema_name")
    address = data.get("address")
    cinema = cinema_business.create_cinema(name, address)
    return jsonify({"cinema_id": cinema.cinema_id, "cinema_name": cinema.cinema_name, "address": cinema.address, "message": "Tạo cinema thành công"}), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)


