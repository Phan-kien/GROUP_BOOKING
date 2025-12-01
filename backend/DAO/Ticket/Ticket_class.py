from backend.DAO.Ticket.Ticket_entity import Ticket

class TicketHelper:
    @staticmethod
    def from_row(row):
        return Ticket(
            ticket_id=row['ticket_id'],
            price=row['price'],
            seat=row['seat'],
            cus_id=row['cus_id'],
            showtime_id=row['showtime_id'],
            payment_id=row['payment_id']
        )
