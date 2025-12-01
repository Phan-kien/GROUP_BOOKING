from flask import Blueprint, Flask, request, jsonify
from backend.BUSINESS.ShowtimeBusiness import ShowtimeBusiness

#app = Flask(__name__)
showtime_api = Blueprint("showtime_api", __name__)
showtime_business = ShowtimeBusiness()

def timedelta_to_str(td):
    if td is None:
        return None
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
@showtime_api.route("/showtimes", methods=["GET"])
def get_showtimes():
    showtimes = showtime_business.get_all_showtimes()
    data = []
    for s in showtimes:
        data.append({
            "showtime_id": s.showtime_id,
            "hall_id": s.hall_id,
            "movie_id": s.movie_id,
            "date": s.date.isoformat() if s.date else None,
            "start_time": timedelta_to_str(s.start_time),
            "end_time": timedelta_to_str(s.end_time)
        })
    return jsonify(data), 200


@showtime_api.route("/showtime", methods=["POST"])
def create_showtime():
    data = request.json
    required_fields = ["hall_id", "movie_id", "date", "start_time", "end_time"]
    if not data or any(field not in data for field in required_fields):
        return jsonify({"error": "Thiếu thông tin showtime"}), 400

    showtime = showtime_business.create_showtime(
        hall_id=data["hall_id"],
        movie_id=data["movie_id"],
        date=data["date"],
        start_time=data["start_time"],
        end_time=data["end_time"]
    )
    return jsonify({
        "showtime_id": showtime.showtime_id,
        "hall_id": showtime.hall_id,
        "movie_id": showtime.movie_id,
        "date": showtime.date.isoformat() if showtime.date else None,
        "start_time": showtime.start_time.strftime("%H:%M:%S") if showtime.start_time else None,
        "end_time": showtime.end_time.strftime("%H:%M:%S") if showtime.end_time else None,
        "message": "Tạo showtime thành công"
    }), 200

#if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
