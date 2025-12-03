from flask import Blueprint,Flask, request, jsonify, session
from backend.BUSINESS.CustomerBusiness import CustomerBusiness

#app = Flask(__name__)
customer_api = Blueprint("customer_api", __name__)
customer_api.secret_key = "supersecretkey"
customer_business = CustomerBusiness()

@customer_api.route('/')
def home():
    return "Auth API is running!"
@customer_api.route("/register", methods=["POST"])
def register_customer():
    data = request.json
    if not data or "cus_id" not in data:
        return jsonify({"error": "cus_id là bắt buộc"}), 400

    cus_id = data["cus_id"]
    name = data.get("name")
    email = data.get("email")
    phone = data.get("number_phone")

    try:
        customer = customer_business.register(cus_id, name, email, phone)
        return jsonify({
            "cus_id": customer.cus_id,
            "name": customer.name,
            "email": customer.email,
            "number_phone": customer.number_phone,
            "message": "Tạo customer thành công"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@customer_api.route("/customer/<cus_id>", methods=["GET"])
def get_customer(cus_id):
    customer = customer_business.get_customer_by_id(cus_id)
    if not customer:
        return jsonify({"error": "Customer không tồn tại"}), 404

    return jsonify({
        "cus_id": customer.cus_id,
        "name": customer.name,
        "email": customer.email,
        "number_phone": customer.number_phone
    }), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)


