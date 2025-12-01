from flask import Blueprint,Flask, request, jsonify
from backend.BUSINESS.BookBusiness import BookBusiness
from datetime import datetime

#app = Flask(__name__)
book_api = Blueprint("book_api", __name__)
book_business = BookBusiness()

@book_api.route("/books", methods=["GET"])
def get_books():
    books = book_business.get_all_books()
    data = [
        {
            "book_id": b.book_id,
            "cus_id": b.cus_id,
            "ticket_id": b.ticket_id,
            "payment_id": b.payment_id,
            "date": b.date.strftime("%Y-%m-%d %H:%M:%S") if b.date else None
        } for b in books
    ]
    return jsonify(data), 200

@book_api.route("/book", methods=["POST"])
def create_book():
    data = request.json
    required_fields = ["cus_id", "ticket_id"]
    if not data or not all(f in data for f in required_fields):
        return jsonify({"error": "Thiếu dữ liệu bắt buộc"}), 400
    date = datetime.now()
    book = book_business.create_book(
        cus_id=data["cus_id"],
        ticket_id=data["ticket_id"],
        payment_id=data.get("payment_id"),
        date=date
    )
    return jsonify({
        "book_id": book.book_id,
        "cus_id": book.cus_id,
        "ticket_id": book.ticket_id,
        "payment_id": book.payment_id,
        "date": book.date.strftime("%Y-%m-%d %H:%M:%S"),
        "message": "Tạo booking thành công"
    }), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
