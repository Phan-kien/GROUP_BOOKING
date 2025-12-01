from backend.DAO.Order.OrderDAO_Interface import OrderDAOInterface
from backend.DAO.Order.Order_entity import Order
from backend.DAO.Order.Order_class import OrderHelper
from backend.config import get_connection

class OrderDAO(OrderDAOInterface):

    def get_all_orders(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_order")
        rows = cursor.fetchall()
        conn.close()
        return [OrderHelper.from_row(r) for r in rows]

    def get_order_by_id(self, order_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_order WHERE order_id=%s", (order_id,))
        row = cursor.fetchone()
        conn.close()
        return OrderHelper.from_row(row) if row else None

    def create_order(self, cus_id, combo_id=None, payment_id=None, date=None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_order (cus_id, combo_id, payment_id, date) VALUES (%s,%s,%s,%s)",
            (cus_id, combo_id, payment_id, date)
        )
        conn.commit()
        order_id = cursor.lastrowid
        conn.close()
        return Order(order_id, cus_id, combo_id, payment_id, date)

    def update_order(self, order_id, combo_id=None, payment_id=None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tbl_order SET combo_id=%s, payment_id=%s WHERE order_id=%s",
            (combo_id, payment_id, order_id)
        )
        conn.commit()
        conn.close()

    def delete_order(self, order_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_order WHERE order_id=%s", (order_id,))
        conn.commit()
        conn.close()
