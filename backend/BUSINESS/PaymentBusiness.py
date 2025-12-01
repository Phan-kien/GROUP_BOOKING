from backend.DAO.Payment.PaymentDAO_dao import PaymentDAO

class PaymentBusiness:
    def __init__(self):
        self.payment_dao = PaymentDAO()

    def get_all_payments(self):
        return self.payment_dao.get_all_payments()

    def get_payment_by_id(self, payment_id):
        return self.payment_dao.get_payment_by_id(payment_id)

    def create_payment(self, cus_id, amount, payment_date, payment_paid=False, status=None, method=None):
        return self.payment_dao.create_payment(cus_id, amount, payment_date, payment_paid, status, method)

    def update_payment(self, payment_id, amount, payment_paid, status, method):
        self.payment_dao.update_payment(payment_id, amount, payment_paid, status, method)

    def delete_payment(self, payment_id):
        self.payment_dao.delete_payment(payment_id)
