class Order:
    def __init__(self, order_id=None, cus_id=None, combo_id=None, payment_id=None, date=None):
        self.order_id = order_id
        self.cus_id = cus_id
        self.combo_id = combo_id
        self.payment_id = payment_id
        self.date = date
