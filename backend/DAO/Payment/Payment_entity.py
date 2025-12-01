class Payment:
    def __init__(self, payment_id=None, cus_id=None, amount=None, payment_date=None, payment_paid=False, status=None, method=None):
        self.payment_id = payment_id
        self.cus_id = cus_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_paid = payment_paid
        self.status = status
        self.method = method
