from backend.DAO.Payment.Payment_entity import Payment

class PaymentHelper:
    @staticmethod
    def from_row(row):
        return Payment(
            payment_id=row['payment_id'],
            cus_id=row['cus_id'],
            amount=row['amount'],
            payment_date=row['payment_date'],
            payment_paid=row['payment_paid'],
            status=row['status'],
            method=row['method']
        )
