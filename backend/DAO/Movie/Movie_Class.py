from backend.DAO.Movie.MovieDAO_dao import MovieDAO
from backend.DAO.Movie.Movie_entity import Movie
import uuid

class MovieHelper:
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

    @staticmethod
    def create_movie_instance(title, duration, genre=None, release_date=None, rating=None):
        movie_id = MovieHelper.generate_id()
        return Movie(movie_id, title, duration, genre, release_date, rating)
