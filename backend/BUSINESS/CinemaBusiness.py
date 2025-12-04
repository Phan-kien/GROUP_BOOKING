from backend.DAO.Cinema.CinemaDAO_dao import CinemaDAO
from backend.DAO.Cinema.Cinema_class import CinemaHelper
from backend.DAO.Cinema.Cinema_entity import Cinema

class CinemaBusiness:
    def __init__(self):
        self.dao = CinemaDAO()

    def create_cinema(self, name, address):
        cinema = Cinema(
            cinema_id=CinemaHelper.generate_id(),
            cinema_name=name,
            address=address
        )
        return self.dao.create(cinema)

    def get_all_cinemas(self):
        return self.dao.get_all()

    def get_cinema(self, cinema_id):
        return self.dao.get_by_id(cinema_id)

    def update_cinema(self, cinema_id, name, address):
        cinema = Cinema(cinema_id=cinema_id, cinema_name=name, address=address)
        return self.dao.update(cinema)

    def delete_cinema(self, cinema_id):
        return self.dao.delete(cinema_id)

    def get_cinemas_by_movie(self, movie_id):
        return self.dao.get_cinemas_by_movie(movie_id)