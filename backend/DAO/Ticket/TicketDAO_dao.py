from backend.DAO.Ticket.TicketDAO_Interface import TicketDAOInterface
from backend.DAO.Ticket.Ticket_class import TicketHelper
from backend.DAO.Ticket.Ticket_entity import Ticket
from backend.config import get_connection

class TicketDAO(TicketDAOInterface):

    def get_all_tickets(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_ticket")
        rows = cursor.fetchall()
        conn.close()
        return [TicketHelper.from_row(r) for r in rows]

    def get_ticket_by_id(self, ticket_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_ticket WHERE ticket_id=%s", (ticket_id,))
        row = cursor.fetchone()
        conn.close()
        return TicketHelper.from_row(row) if row else None

    def create_ticket(self, price, seat, cus_id, showtime_id, payment_id=None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_ticket (price, seat, cus_id, showtime_id, payment_id) VALUES (%s,%s,%s,%s,%s)",
            (price, seat, cus_id, showtime_id, payment_id)
        )
        conn.commit()
        ticket_id = cursor.lastrowid
        conn.close()
        return Ticket(ticket_id, price, seat, cus_id, showtime_id, payment_id)

    def update_ticket(self, ticket_id, price=None, seat=None, cus_id=None, showtime_id=None, payment_id=None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tbl_ticket SET price=%s, seat=%s, cus_id=%s, showtime_id=%s, payment_id=%s WHERE ticket_id=%s",
            (price, seat, cus_id, showtime_id, payment_id, ticket_id)
        )
        conn.commit()
        conn.close()

    def delete_ticket(self, ticket_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_ticket WHERE ticket_id=%s", (ticket_id,))
        conn.commit()
        conn.close()
