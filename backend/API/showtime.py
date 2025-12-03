from flask import Blueprint, Flask, request, jsonify
from backend.BUSINESS.ShowtimeBusiness import ShowtimeBusiness
from backend.DAO.Showtime.Showtime_Class import ShowtimeHelper
from datetime import datetime, timedelta, time
#app = Flask(__name__)
showtime_api = Blueprint("showtime_api", __name__)
showtime_business = ShowtimeBusiness()

def time_to_str(t):
    """Chuyển datetime.time hoặc timedelta sang HH:MM:SS"""
    if t is None:
        return None
    if isinstance(t, timedelta):
        total_seconds = int(t.total_seconds())
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return f"{h:02}:{m:02}:{s:02}"
    if isinstance(t, time):
        return t.strftime("%H:%M:%S")
    return str(t)  # fallback
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
            "start_time": time_to_str(s.start_time),
            "end_time": time_to_str(s.end_time)
        })
    return jsonify(data), 200


@showtime_api.route("/showtime", methods=["POST"])
def create_showtime():
    data = request.json
    required_fields = ["hall_id", "movie_id", "date", "start_time", "end_time"]

    if not data or any(field not in data for field in required_fields):
        return jsonify({"error": "Thiếu thông tin showtime"}), 400

    # Chuẩn hoá date và time
    try:
        date_obj = datetime.strptime(data["date"], "%Y-%m-%d").date()
        start_time_obj = ShowtimeHelper.normalize_time(data["start_time"])
        end_time_obj = ShowtimeHelper.normalize_time(data["end_time"])
    except Exception as e:
        return jsonify({"error": f"Định dạng date/time sai: {str(e)}"}), 400

    # Tạo showtime, ID do trigger MySQL tự sinh
    showtime = showtime_business.create_showtime(
        hall_id=data["hall_id"],
        movie_id=data["movie_id"],
        date=date_obj,
        start_time=start_time_obj,
        end_time=end_time_obj
    )

    return jsonify({
        "showtime_id": showtime.showtime_id,
        "hall_id": showtime.hall_id,
        "movie_id": showtime.movie_id,
        "date": showtime.date.isoformat() if showtime.date else None,
        "start_time": time_to_str(showtime.start_time),
        "end_time": time_to_str(showtime.end_time),
        "message": "Tạo showtime thành công"
    }), 200

    #if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
