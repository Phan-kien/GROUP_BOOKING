from flask import Blueprint, Flask, request, jsonify
from backend.BUSINESS.MovieBusiness import MovieBusiness

#app = Flask(__name__)
movie_api = Blueprint("movie_api", __name__)
movie_business = MovieBusiness()

@movie_api.route("/movies", methods=["GET"])
def get_movies():
    movies = movie_business.get_all_movies()
    data = [{"movie_id": m.movie_id, "title": m.title, "duration": m.duration, "genre": m.genre,
             "release_date": m.release_date, "rating": m.rating} for m in movies]
    return jsonify(data), 200

@movie_api.route("/movie", methods=["POST"])
def create_movie():
    data = request.json
    if not data or "title" not in data or "duration" not in data:
        return jsonify({"error": "Thiếu title hoặc duration"}), 400
    movie = movie_business.create_movie(
        title=data["title"],
        duration=data["duration"],
        genre=data.get("genre"),
        release_date=data.get("release_date"),
        rating=data.get("rating")
    )
    return jsonify({
        "movie_id": movie.movie_id,
        "title": movie.title,
        "duration": movie.duration,
        "genre": movie.genre,
        "release_date": movie.release_date,
        "rating": movie.rating,
        "message": "Tạo movie thành công"
    }), 200

@movie_api.route("/movies/search", methods=["GET"])
def search_movies():
        keyword = request.args.get("q", "")
        movies = movie_business.search_movies(keyword)
        data = [{"movie_id": m.movie_id, "title": m.title, "duration": m.duration, "genre": m.genre,
                 "release_date": m.release_date, "rating": m.rating} for m in movies]
        return jsonify(data), 200

#if __name__ == "__main__":
#    app.run(debug=True, host="127.0.0.1", port=5000)
