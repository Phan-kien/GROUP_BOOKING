import mysql.connector
from backend.config import get_connection
from backend.DAO.Movie.MovieDAO_Interface import MovieDAOInterface
from backend.DAO.Movie.Movie_entity import Movie

class MovieDAO(MovieDAOInterface):

    def get_all_movies(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_movie")
        rows = cursor.fetchall()
        movies = [Movie(**row) for row in rows]
        cursor.close()
        conn.close()
        return movies

    def get_movie_by_id(self, movie_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_movie WHERE movie_id = %s", (movie_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Movie(**row) if row else None

    def create_movie(self, movie):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_movie (movie_id, title, duration, genre, release_date, rating) VALUES (%s,%s,%s,%s,%s,%s)",
            (movie.movie_id, movie.title, movie.duration, movie.genre, movie.release_date, movie.rating)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return movie
