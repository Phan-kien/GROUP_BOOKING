from flask import Blueprint, Flask, request, jsonify
from backend.BUSINESS.ComboBusiness import ComboBusiness

#app = Flask(__name__)
combo_api = Blueprint("combo_api", __name__)
combo_business = ComboBusiness()

@combo_api.route("/combos", methods=["GET"])
def get_combos():
    combos = combo_business.get_all_combos()
    data = [
        {"combo_id": c.combo_id, "combo_name": c.combo_name, "description": c.description, "price": float(c.price)}
        for c in combos
    ]
    return jsonify(data), 200

@combo_api.route("/combo", methods=["POST"])
def create_combo():
    data = request.json
    if not data or "combo_name" not in data or "price" not in data:
        return jsonify({"error": "Thiếu combo_name hoặc price"}), 400
    name = data.get("combo_name")
    description = data.get("description")
    price = data.get("price")
    combo = combo_business.create_combo(name, description, price)
    return jsonify({
        "combo_id": combo.combo_id,
        "combo_name": combo.combo_name,
        "description": combo.description,
        "price": float(combo.price),
        "message": "Tạo combo thành công"
    }), 200

@combo_api.route("/combo/<int:combo_id>", methods=["PUT"])
def update_combo(combo_id):
    data = request.json
    name = data.get("combo_name")
    description = data.get("description")
    price = data.get("price")
    combo_business.update_combo(combo_id, name, description, price)
    return jsonify({"message": "Cập nhật combo thành công"}), 200

@combo_api.route("/combo/<int:combo_id>", methods=["DELETE"])
def delete_combo(combo_id):
    combo_business.delete_combo(combo_id)
    return jsonify({"message": "Xóa combo thành công"}), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
