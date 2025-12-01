from backend.DAO.Order.Order_entity import Order

class OrderHelper:
    @staticmethod
    def from_row(row):
        return Order(
            order_id=row['order_id'],
            cus_id=row['cus_id'],
            combo_id=row['combo_id'],
            payment_id=row['payment_id'],
            date=row['date']
        )