class Ticket:
    def __init__(self, ticket_id=None, price=None, seat=None, cus_id=None, showtime_id=None, payment_id=None):
        self.ticket_id = ticket_id
        self.price = price
        self.seat = seat
        self.cus_id = cus_id
        self.showtime_id = showtime_id
        self.payment_id = payment_id
