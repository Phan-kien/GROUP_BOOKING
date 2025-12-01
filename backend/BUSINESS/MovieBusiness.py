from backend.DAO.Movie.Movie_Class import MovieHelper
from backend.DAO.Movie.MovieDAO_dao import MovieDAO

class MovieBusiness:
    def __init__(self):
        self.dao = MovieDAO()

    def get_all_movies(self):
        return self.dao.get_all_movies()

    def get_movie_by_id(self, movie_id):
        return self.dao.get_movie_by_id(movie_id)

    def create_movie(self, title, duration, genre=None, release_date=None, rating=None):
        movie = MovieHelper.create_movie_instance(title, duration, genre, release_date, rating)
        return self.dao.create_movie(movie)
