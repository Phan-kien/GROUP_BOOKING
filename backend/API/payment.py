from flask import Blueprint, Flask, request, jsonify
from backend.BUSINESS.PaymentBusiness import PaymentBusiness
from datetime import datetime

#app = Flask(__name__)
payment_api = Blueprint("payment_api", __name__)
payment_business = PaymentBusiness()

@payment_api.route("/payments", methods=["GET"])
def get_payments():
    payments = payment_business.get_all_payments()
    data = [
        {
            "payment_id": p.payment_id,
            "cus_id": p.cus_id,
            "amount": float(p.amount),
            "payment_date": p.payment_date.strftime("%Y-%m-%d %H:%M:%S") if p.payment_date else None,
            "payment_paid": p.payment_paid,
            "status": p.status,
            "method": p.method
        }
        for p in payments
    ]
    return jsonify(data), 200

@payment_api.route("/payment", methods=["POST"])
def create_payment():
    data = request.json
    if not data or "cus_id" not in data or "amount" not in data:
        return jsonify({"error": "Thiếu cus_id hoặc amount"}), 400
    cus_id = data.get("cus_id")
    amount = data.get("amount")
    payment_date = datetime.now()
    payment_paid = data.get("payment_paid", False)
    status = data.get("status")
    method = data.get("method")
    payment = payment_business.create_payment(cus_id, amount, payment_date, payment_paid, status, method)
    return jsonify({
        "payment_id": payment.payment_id,
        "cus_id": payment.cus_id,
        "amount": float(payment.amount),
        "payment_date": payment.payment_date.strftime("%Y-%m-%d %H:%M:%S"),
        "payment_paid": payment.payment_paid,
        "status": payment.status,
        "method": payment.method,
        "message": "Tạo payment thành công"
    }), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
