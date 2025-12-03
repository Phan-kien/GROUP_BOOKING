from backend.DAO.Showtime.Showtime_Class import ShowtimeHelper
from backend.DAO.Showtime.ShowtimeDAO_dao import ShowtimeDAO
from backend.DAO.Showtime.Showtime_entity import Showtime
from datetime import datetime

class ShowtimeBusiness:
    def __init__(self):
        self.dao = ShowtimeDAO()

    def get_all_showtimes(self):
        return self.dao.get_all_showtimes()

    def get_showtime_by_id(self, showtime_id):
        return self.dao.get_showtime_by_id(showtime_id)

    def create_showtime(self, hall_id, movie_id, date, start_time, end_time):
        """
                Chuẩn hoá date/time trước khi gửi xuống DAO
                """
        if isinstance(date, str):
            # Chuyển sang YYYY-MM-DD
            date = datetime.strptime(date, "%Y-%m-%d").date()

        start_time = ShowtimeHelper.normalize_time(start_time)
        end_time = ShowtimeHelper.normalize_time(end_time)

        return self.dao.create_showtime(hall_id, movie_id, date, start_time, end_time)
