from backend.DAO.Ticket.TicketDAO_dao import TicketDAO

class TicketBusiness:
    def __init__(self):
        self.ticket_dao = TicketDAO()

    def get_all_tickets(self):
        return self.ticket_dao.get_all_tickets()

    def get_ticket_by_id(self, ticket_id):
        return self.ticket_dao.get_ticket_by_id(ticket_id)

    def create_ticket(self, price, seat, cus_id, showtime_id, payment_id=None):
        return self.ticket_dao.create_ticket(price, seat, cus_id, showtime_id, payment_id)

    def update_ticket(self, ticket_id, price=None, seat=None, cus_id=None, showtime_id=None, payment_id=None):
        self.ticket_dao.update_ticket(ticket_id, price, seat, cus_id, showtime_id, payment_id)

    def delete_ticket(self, ticket_id):
        self.ticket_dao.delete_ticket(ticket_id)
