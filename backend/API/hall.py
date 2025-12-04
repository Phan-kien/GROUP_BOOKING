from flask import Blueprint, Flask, request, jsonify
from backend.BUSINESS.HallBusiness import HallBusiness
from backend.DAO.Hall.Hall_entity import Hall
from backend.config import get_connection

#app = Flask(__name__)
hall_api = Blueprint("hall_api", __name__)
hall_business = HallBusiness()

@hall_api.route("/halls", methods=["GET"])
def get_halls():
    cinema_id = request.args.get("cinema_id")
    movie_id = request.args.get("movie_id")

    # Nếu không có filter => return full
    if not cinema_id and not movie_id:
        halls = hall_business.get_all_halls()
        return jsonify([
            {"hall_id": h.hall_id, "cinema_id": h.cinema_id, "hall_name": h.hall_name}
            for h in halls
        ])

    # Nếu chỉ lọc theo cinema
    if cinema_id and not movie_id:
        halls = hall_business.get_halls_by_cinema(cinema_id)
        return jsonify([
            {"hall_id": h.hall_id, "cinema_id": h.cinema_id, "hall_name": h.hall_name}
            for h in halls
        ])

    # Nếu lọc theo cinema + movie
    if cinema_id and movie_id:
        halls = hall_business.get_halls_by_cinema_and_movie(cinema_id, movie_id)
        return jsonify([
            {"hall_id": h.hall_id, "cinema_id": h.cinema_id, "hall_name": h.hall_name}
            for h in halls
        ])

@hall_api.route("/hall", methods=["POST"])
def create_hall():
    data = request.json
    if not data or "hall_name" not in data or "cinema_id" not in data:
        return jsonify({"error": "Thiếu hall_name hoặc cinema_id"}), 400
    hall = hall_business.create_hall(data["cinema_id"], data["hall_name"])
    return jsonify({
        "hall_id": hall.hall_id,
        "cinema_id": hall.cinema_id,
        "hall_name": hall.hall_name,
        "message": "Tạo hall thành công"
    }), 200

@hall_api.route("/hall/by-cinema/<cinema_id>", methods=["GET"])
def get_halls_by_cinema_and_movie(self, cinema_id, movie_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
            SELECT h.hall_id, h.cinema_id, h.hall_name
            FROM tbl_hall h
                     JOIN tbl_showtime s ON s.hall_id = h.hall_id
            WHERE h.cinema_id = %s \
              AND s.movie_id = %s
            GROUP BY h.hall_id \
            """

    cursor.execute(query, (cinema_id, movie_id))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [Hall(hall_id=r[0], cinema_id=r[1], hall_name=r[2]) for r in rows]


    @hall_api.route("/hall/by-cinema/<cinema_id>", methods=["GET"])
    def get_halls_by_cinema(cinema_id):
        halls = hall_business.get_halls_by_cinema(cinema_id)

        result = []
        for h in halls:
            result.append({
                "hall_id": h.hall_id,
                "cinema_id": h.cinema_id,
                "hall_name": h.hall_name
            })

        return jsonify(result)

    #if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
