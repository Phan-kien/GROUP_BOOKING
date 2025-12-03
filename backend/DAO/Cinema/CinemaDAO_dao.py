from backend.DAO.Cinema.CinemaDAO_Interface import CinemaDAOInterface
from backend.DAO.Cinema.Cinema_entity import Cinema
from backend.config import get_connection

class CinemaDAO(CinemaDAOInterface):
    def create(self, cinema):
        conn = get_connection()
        cursor = conn.cursor()
        # Chỉ insert name + address, MySQL trigger sẽ tự sinh cinema_id
        cursor.execute(
            "INSERT INTO tbl_cinema (cinema_name, address) VALUES (%s, %s)",
            (cinema.cinema_name, cinema.address)
        )
        conn.commit()

        # Lấy ID vừa insert
        cursor.execute("SELECT cinema_id FROM tbl_cinema ORDER BY cinema_id DESC LIMIT 1")
        cinema_id = cursor.fetchone()[0]
        cinema.cinema_id = cinema_id

        cursor.close()
        conn.close()
        return cinema

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT cinema_id, cinema_name, address FROM tbl_cinema")
        rows = cursor.fetchall()
        cinemas = [Cinema(cinema_id=r[0], cinema_name=r[1], address=r[2]) for r in rows]
        cursor.close()
        conn.close()
        return cinemas

    def get_by_id(self, cinema_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT cinema_id, cinema_name, address FROM tbl_cinema WHERE cinema_id=%s", (cinema_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Cinema(cinema_id=row[0], cinema_name=row[1], address=row[2])
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
