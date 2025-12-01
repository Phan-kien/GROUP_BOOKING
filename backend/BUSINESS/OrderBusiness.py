from backend.DAO.Order.OrderDAO_dao import OrderDAO

class OrderBusiness:
    def __init__(self):
        self.order_dao = OrderDAO()

    def get_all_orders(self):
        return self.order_dao.get_all_orders()

    def get_order_by_id(self, order_id):
        return self.order_dao.get_order_by_id(order_id)

    def create_order(self, cus_id, combo_id=None, payment_id=None, date=None):
        return self.order_dao.create_order(cus_id, combo_id, payment_id, date)

    def update_order(self, order_id, combo_id=None, payment_id=None):
        self.order_dao.update_order(order_id, combo_id, payment_id)

    def delete_order(self, order_id):
        self.order_dao.delete_order(order_id)
