from abc import ABC, abstractmethod

class OrderDAOInterface(ABC):

    @abstractmethod
    def get_all_orders(self):
        pass

    @abstractmethod
    def get_order_by_id(self, order_id):
        pass

    @abstractmethod
    def create_order(self, cus_id, combo_id, payment_id, date):
        pass

    @abstractmethod
    def update_order(self, order_id, combo_id, payment_id):
        pass

    @abstractmethod
    def delete_order(self, order_id):
        pass
