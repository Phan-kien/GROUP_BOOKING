import mysql.connector
from backend.config import get_connection
from backend.DAO.Showtime.ShowtimeDAO_Interface import ShowtimeDAOInterface
from backend.DAO.Showtime.Showtime_entity import Showtime

class ShowtimeDAO(ShowtimeDAOInterface):

    def get_all_showtimes(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_showtime")
        rows = cursor.fetchall()
        showtimes = [Showtime(**row) for row in rows]
        cursor.close()
        conn.close()
        return showtimes

    def get_showtime_by_id(self, showtime_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_showtime WHERE showtime_id = %s", (showtime_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Showtime(**row) if row else None

    def create_showtime(self, showtime):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_showtime (showtime_id, hall_id, movie_id, date, start_time, end_time) "
            "VALUES (%s,%s,%s,%s,%s,%s)",
            (showtime.showtime_id, showtime.hall_id, showtime.movie_id, showtime.date, showtime.start_time, showtime.end_time)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return showtime
