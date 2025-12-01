from backend.DAO.Cinema.CinemaDAO_Interface import CinemaDAOInterface
from backend.DAO.Cinema.Cinema_entity import Cinema
from backend.config import get_connection

class CinemaDAO(CinemaDAOInterface):
    def create(self, cinema):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_cinema(cinema_id, cinema_name, address) VALUES (%s, %s, %s)",
            (cinema.cinema_id, cinema.cinema_name, cinema.address)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return cinema

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_cinema")
        rows = cursor.fetchall()
        cinemas = [Cinema(**row) for row in rows]
        cursor.close()
        conn.close()
        return cinemas

    def get_by_id(self, cinema_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_cinema WHERE cinema_id=%s", (cinema_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Cinema(**row) if row else None

    def update(self, cinema):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tbl_cinema SET cinema_name=%s, address=%s WHERE cinema_id=%s",
            (cinema.cinema_name, cinema.address, cinema.cinema_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return cinema

    def delete(self, cinema_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_cinema WHERE cinema_id=%s", (cinema_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
