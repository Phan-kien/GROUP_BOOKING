from backend.DAO.Showtime.Showtime_entity import Showtime
import uuid

class ShowtimeHelper:
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

    @staticmethod
    def create_showtime_instance(hall_id, movie_id, date, start_time, end_time):
        showtime_id = ShowtimeHelper.generate_id()
        return Showtime(showtime_id, hall_id, movie_id, date, start_time, end_time)
