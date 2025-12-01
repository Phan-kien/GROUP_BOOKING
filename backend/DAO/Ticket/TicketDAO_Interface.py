from abc import ABC, abstractmethod

class TicketDAOInterface(ABC):

    @abstractmethod
    def get_all_tickets(self):
        pass

    @abstractmethod
    def get_ticket_by_id(self, ticket_id):
        pass

    @abstractmethod
    def create_ticket(self, price, seat, cus_id, showtime_id, payment_id=None):
        pass

    @abstractmethod
    def update_ticket(self, ticket_id, price=None, seat=None, cus_id=None, showtime_id=None, payment_id=None):
        pass

    @abstractmethod
    def delete_ticket(self, ticket_id):
        pass
