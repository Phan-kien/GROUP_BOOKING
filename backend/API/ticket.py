from flask import Blueprint,Flask, request, jsonify
from backend.BUSINESS.TicketBusiness import TicketBusiness

#app = Flask(__name__)
ticket_api = Blueprint("ticket_api", __name__)
ticket_business = TicketBusiness()

@ticket_api.route("/tickets", methods=["GET"])
def get_tickets():
    tickets = ticket_business.get_all_tickets()
    data = [
        {
            "ticket_id": t.ticket_id,
            "price": t.price,
            "seat": t.seat,
            "cus_id": t.cus_id,
            "showtime_id": t.showtime_id,
            "payment_id": t.payment_id
        } for t in tickets
    ]
    return jsonify(data), 200

@ticket_api.route("/ticket", methods=["POST"])
def create_ticket():
    data = request.json
    required_fields = ["price", "seat", "cus_id", "showtime_id"]
    if not data or not all(f in data for f in required_fields):
        return jsonify({"error": "Thiếu dữ liệu bắt buộc"}), 400
    ticket = ticket_business.create_ticket(
        price=data["price"],
        seat=data["seat"],
        cus_id=data["cus_id"],
        showtime_id=data["showtime_id"],
        payment_id=data.get("payment_id")
    )
    return jsonify({
        "ticket_id": ticket.ticket_id,
        "price": ticket.price,
        "seat": ticket.seat,
        "cus_id": ticket.cus_id,
        "showtime_id": ticket.showtime_id,
        "payment_id": ticket.payment_id,
        "message": "Tạo ticket thành công"
    }), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
