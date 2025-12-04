import mysql.connector
from backend.config import get_connection
from backend.DAO.Showtime.ShowtimeDAO_Interface import ShowtimeDAOInterface
from backend.DAO.Showtime.Showtime_entity import Showtime
from backend.DAO.Showtime.Showtime_Class import ShowtimeHelper

class ShowtimeDAO(ShowtimeDAOInterface):

    def get_all_showtimes(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT showtime_id, hall_id, movie_id, date, start_time, end_time
                       FROM tbl_showtime
                       """)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        showtimes = []
        for r in rows:
            st = Showtime(r[0], r[1], r[2], r[3], r[4], r[5])
            showtimes.append(st)
        return showtimes

    def get_showtime_by_id(self, showtime_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT showtime_id, hall_id, movie_id, date, start_time, end_time
                       FROM tbl_showtime
                       WHERE showtime_id = %s
                       """, (showtime_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Showtime(*row)
        return None

    def create_showtime(self, hall_id, movie_id, date, start_time, end_time):
        """
                Chú ý: KHÔNG truyền showtime_id → MySQL trigger tự sinh
                """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO tbl_showtime (hall_id, movie_id, date, start_time, end_time)
                       VALUES (%s, %s, %s, %s, %s)
                       """, (hall_id, movie_id, date, start_time, end_time))
        conn.commit()

        # Lấy showtime_id vừa insert (trigger tạo)
        cursor.execute("""
                       SELECT showtime_id
                       FROM tbl_showtime
                       WHERE hall_id = %s
                         AND movie_id = %s
                         AND date =%s
                         AND start_time=%s
                         AND end_time=%s
                       ORDER BY showtime_id DESC LIMIT 1
                       """, (hall_id, movie_id, date, start_time, end_time))
        showtime_id = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        # Trả về entity hoàn chỉnh
        return Showtime(showtime_id, hall_id, movie_id, date, start_time, end_time)

    def get_showtimes_by_hall(self, hall_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT showtime_id, hall_id, movie_id, date, start_time, end_time
                       FROM tbl_showtime
                       WHERE hall_id = %s
                       """, (hall_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [Showtime(*r) for r in rows]
