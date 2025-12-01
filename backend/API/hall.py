from flask import Blueprint, Flask, request, jsonify
from backend.BUSINESS.HallBusiness import HallBusiness

#app = Flask(__name__)
hall_api = Blueprint("hall_api", __name__)
hall_business = HallBusiness()

@hall_api.route("/halls", methods=["GET"])
def get_halls():
    halls = hall_business.get_all_halls()
    data = [{"hall_id": h.hall_id, "cinema_id": h.cinema_id, "hall_name": h.hall_name} for h in halls]
    return jsonify(data), 200

@hall_api.route("/hall", methods=["POST"])
def create_hall():
    data = request.json
    if not data or "hall_name" not in data or "cinema_id" not in data:
        return jsonify({"error": "Thiếu hall_name hoặc cinema_id"}), 400
    hall = hall_business.create_hall(data["cinema_id"], data["hall_name"])
    return jsonify({
        "hall_id": hall.hall_id,
        "cinema_id": hall.cinema_id,
        "hall_name": hall.hall_name,
        "message": "Tạo hall thành công"
    }), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
