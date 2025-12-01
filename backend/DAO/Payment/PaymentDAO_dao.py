from backend.DAO.Payment.PaymentDAO_Interface import PaymentDAOInterface
from backend.DAO.Payment.Payment_entity import Payment
from backend.DAO.Payment.Payment_class import PaymentHelper
from backend.config import get_connection

class PaymentDAO(PaymentDAOInterface):

    def get_all_payments(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_payment")
        rows = cursor.fetchall()
        conn.close()
        return [PaymentHelper.from_row(r) for r in rows]

    def get_payment_by_id(self, payment_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_payment WHERE payment_id=%s", (payment_id,))
        row = cursor.fetchone()
        conn.close()
        return PaymentHelper.from_row(row) if row else None

    def create_payment(self, cus_id, amount, payment_date, payment_paid=False, status=None, method=None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_payment (cus_id, amount, payment_date, payment_paid, status, method) VALUES (%s,%s,%s,%s,%s,%s)",
            (cus_id, amount, payment_date, payment_paid, status, method)
        )
        conn.commit()
        payment_id = cursor.lastrowid
        conn.close()
        return Payment(payment_id, cus_id, amount, payment_date, payment_paid, status, method)

    def update_payment(self, payment_id, amount, payment_paid, status, method):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tbl_payment SET amount=%s, payment_paid=%s, status=%s, method=%s WHERE payment_id=%s",
            (amount, payment_paid, status, method, payment_id)
        )
        conn.commit()
        conn.close()

    def delete_payment(self, payment_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_payment WHERE payment_id=%s", (payment_id,))
        conn.commit()
        conn.close()
