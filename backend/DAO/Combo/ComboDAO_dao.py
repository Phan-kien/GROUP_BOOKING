from backend.DAO.Combo.ComboDAO_Interface import ComboDAOInterface
from backend.DAO.Combo.Combo_entity import Combo
from backend.DAO.Combo.Combo_class import ComboHelper
from backend.config import get_connection

class ComboDAO(ComboDAOInterface):

    def get_all_combos(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_combo")
        rows = cursor.fetchall()
        conn.close()
        return [ComboHelper.from_row(r) for r in rows]

    def get_combo_by_id(self, combo_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_combo WHERE combo_id=%s", (combo_id,))
        row = cursor.fetchone()
        conn.close()
        return ComboHelper.from_row(row) if row else None

    def create_combo(self, combo_name, description, price):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_combo (combo_name, description, price) VALUES (%s, %s, %s)",
            (combo_name, description, price)
        )
        conn.commit()
        combo_id = cursor.lastrowid
        conn.close()
        return Combo(combo_id, combo_name, description, price)

    def update_combo(self, combo_id, combo_name, description, price):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tbl_combo SET combo_name=%s, description=%s, price=%s WHERE combo_id=%s",
            (combo_name, description, price, combo_id)
        )
        conn.commit()
        conn.close()

    def delete_combo(self, combo_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_combo WHERE combo_id=%s", (combo_id,))
        conn.commit()
        conn.close()
