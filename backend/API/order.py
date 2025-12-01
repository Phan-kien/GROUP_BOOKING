from flask import Blueprint, Flask, request, jsonify
from backend.BUSINESS.OrderBusiness import OrderBusiness
from datetime import datetime

#app = Flask(__name__)
order_api = Blueprint("order_api", __name__)
order_business = OrderBusiness()

@order_api.route("/orders", methods=["GET"])
def get_orders():
    orders = order_business.get_all_orders()
    data = [
        {
            "order_id": o.order_id,
            "cus_id": o.cus_id,
            "combo_id": o.combo_id,
            "payment_id": o.payment_id,
            "date": o.date.strftime("%Y-%m-%d %H:%M:%S") if o.date else None
        } for o in orders
    ]
    return jsonify(data), 200

@order_api.route("/order", methods=["POST"])
def create_order():
    data = request.json
    if not data or "cus_id" not in data:
        return jsonify({"error": "Thiếu cus_id"}), 400
    cus_id = data.get("cus_id")
    combo_id = data.get("combo_id")
    payment_id = data.get("payment_id")
    date = datetime.now()
    order = order_business.create_order(cus_id, combo_id, payment_id, date)
    return jsonify({
        "order_id": order.order_id,
        "cus_id": order.cus_id,
        "combo_id": order.combo_id,
        "payment_id": order.payment_id,
        "date": order.date.strftime("%Y-%m-%d %H:%M:%S"),
        "message": "Tạo order thành công"
    }), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
