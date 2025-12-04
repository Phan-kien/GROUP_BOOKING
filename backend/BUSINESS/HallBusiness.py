from backend.DAO.Hall.HallDAO_dao import HallDAO
from backend.DAO.Hall.Hall_class import HallHelper
from backend.DAO.Hall.Hall_entity import Hall

class HallBusiness:
    def __init__(self):
        self.hall_dao = HallDAO()

    def create_hall(self, cinema_id, hall_name):
        hall_name = HallHelper.format_name(hall_name)
        hall = Hall(hall_id=None, cinema_id=cinema_id, hall_name=hall_name)
        return self.hall_dao.create_hall(hall)

    def get_all_halls(self):
        return self.hall_dao.get_all_halls()

    def get_hall_by_id(self, hall_id):
        return self.hall_dao.get_hall_by_id(hall_id)

    def get_halls_by_cinema_and_movie(self, cinema_id, movie_id):
        return self.hall_dao.get_halls_by_cinema_and_movie(cinema_id, movie_id)

    def get_halls_by_cinema(self, cinema_id):
        return self.hall_dao.get_halls_by_cinema(cinema_id)
