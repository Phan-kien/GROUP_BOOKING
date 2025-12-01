from backend.DAO.Showtime.Showtime_Class import ShowtimeHelper
from backend.DAO.Showtime.ShowtimeDAO_dao import ShowtimeDAO

class ShowtimeBusiness:
    def __init__(self):
        self.dao = ShowtimeDAO()

    def get_all_showtimes(self):
        return self.dao.get_all_showtimes()

    def get_showtime_by_id(self, showtime_id):
        return self.dao.get_showtime_by_id(showtime_id)

    def create_showtime(self, hall_id, movie_id, date, start_time, end_time):
        showtime = ShowtimeHelper.create_showtime_instance(hall_id, movie_id, date, start_time, end_time)
        return self.dao.create_showtime(showtime)
