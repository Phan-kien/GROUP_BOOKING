from flask import Blueprint,Flask, request, jsonify, session
from backend.BUSINESS.CustomerBusiness import CustomerBusiness
from backend.DAO.Customer.CustomerDAO_dao import CustomerDAO
from backend.DAO.Customer.Customer_entity import Customer


#app = Flask(__name__)
customer_api = Blueprint("customer_api", __name__)
customer_api.secret_key = "supersecretkey"
customer_business = CustomerBusiness()
dao = CustomerDAO()
@customer_api.route('/')
def home():
    return "Auth API is running!"
@customer_api.route("/register", methods=["POST"])
def register_customer():
    """
        Tạo customer mới.
        Frontend tự sinh cus_id.
        Các field name, email, number_phone có thể để trống.
        """
    data = request.json
    if not data or "cus_id" not in data:
        return jsonify({"error": "Thiếu cus_id"}), 400

    cus_id = data.get("cus_id")
    name = data.get("name")
    email = data.get("email")
    phone = data.get("number_phone")

    try:
        customer = Customer(cus_id=cus_id, name=name, email=email, number_phone=phone)
        dao.create_customer(customer)
        return jsonify({
            "cus_id": cus_id,
            "name": name,
            "email": email,
            "number_phone": phone,
            "message": "Customer lưu thành công"
        }), 201
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


