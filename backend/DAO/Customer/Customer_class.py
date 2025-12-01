# Customer_class.py
import re
from backend.DAO.Customer.Customer_entity import Customer

class CustomerHelper:
    @staticmethod
    def validate_email(email):
        """Kiểm tra email hợp lệ"""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def format_phone(number_phone):
        if not number_phone:  # Nếu None hoặc rỗng
            return None
        return re.sub(r'\D', '', number_phone)

    @staticmethod
    def get_customer_summary(customer: Customer):
        """Trả về dict tóm tắt thông tin customer (không bao gồm password)"""
        return {
            "cus_id": customer.cus_id,
            "name": customer.name,
            "email": customer.email,
            "number_phone": customer.number_phone
        }
