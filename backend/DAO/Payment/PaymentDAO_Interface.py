from abc import ABC, abstractmethod

class PaymentDAOInterface(ABC):

    @abstractmethod
    def get_all_payments(self):
        pass

    @abstractmethod
    def get_payment_by_id(self, payment_id):
        pass

    @abstractmethod
    def create_payment(self, cus_id, amount, payment_date, payment_paid, status, method):
        pass

    @abstractmethod
    def update_payment(self, payment_id, amount, payment_paid, status, method):
        pass

    @abstractmethod
    def delete_payment(self, payment_id):
        pass
