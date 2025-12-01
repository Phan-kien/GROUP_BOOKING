from flask import Blueprint,Flask, request, jsonify, session
from backend.BUSINESS.CustomerBusiness import CustomerBusiness

#app = Flask(__name__)
auth_api = Blueprint("auth_api", __name__)
auth_api.secret_key = "supersecretkey"
customer_business = CustomerBusiness()

@auth_api.route('/')
def home():
    return "Auth API is running!"
@auth_api.route("/register", methods=["POST"])
def register():
    data = request.json
    customer, error = customer_business.register(
        data.get("name"),
        data.get("email"),
        data.get("phone"),
        data.get("password")
    )
    if error:
        return jsonify({"error": error}), 400
    summary = customer_business.get_customer_summary(customer)
    return jsonify({"message": "Đăng ký thành công", "customer": summary})

@auth_api.route("/login", methods=["POST"])
def login():
    data = request.json
    customer, error = customer_business.login(
        data.get("email"),
        data.get("password")
    )
    if error:
        return jsonify({"error": error}), 400
    # Lưu session
    session["cus_id"] = customer.cus_id
    summary = customer_business.get_customer_summary(customer)
    return jsonify({"message": "Đăng nhập thành công", "customer": summary})

@auth_api.route("/logout", methods=["POST"])
def logout():
    session.pop("cus_id", None)
    return jsonify({"message": "Đăng xuất thành công"})

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)


