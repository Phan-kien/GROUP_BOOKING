from backend.DAO.Hall.HallDAO_Interface import HallDAOInterface
from backend.DAO.Hall.Hall_entity import Hall
from backend.config import get_connection
import uuid

class HallDAO(HallDAOInterface):

    def create_hall(self, hall):
        conn = get_connection()
        cursor = conn.cursor()
        hall_id = str(uuid.uuid4())  # sinh hall_id kiểu VARCHAR
        cursor.execute(
            "INSERT INTO tbl_hall (hall_id, cinema_id, hall_name) VALUES (%s, %s, %s)",
            (hall_id, hall.cinema_id, hall.hall_name)
        )
        conn.commit()
        cursor.close()
        conn.close()
        hall.hall_id = hall_id
        return hall

    def get_all_halls(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT hall_id, cinema_id, hall_name FROM tbl_hall")
        rows = cursor.fetchall()
        halls = [Hall(hall_id=r[0], cinema_id=r[1], hall_name=r[2]) for r in rows]
        cursor.close()
        conn.close()
        return halls

    def get_hall_by_id(self, hall_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT hall_id, cinema_id, hall_name FROM tbl_hall WHERE hall_id=%s", (hall_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Hall(hall_id=row[0], cinema_id=row[1], hall_name=row[2])
        return None
