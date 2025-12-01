from backend.DAO.Customer.CustomerDAO_dao import CustomerDAO
from backend.DAO.Customer.Customer_entity import Customer
from backend.DAO.Customer.Customer_class import CustomerHelper
import bcrypt

class CustomerBusiness:
    def __init__(self):
        self.dao = CustomerDAO()

    def register(self, name, email, phone, password):
        # Kiểm tra email hợp lệ
        if not CustomerHelper.validate_email(email):
            return None, "Email không hợp lệ"

        # Chuẩn hóa số điện thoại
        phone = CustomerHelper.format_phone(phone)

        # Kiểm tra email đã tồn tại chưa
        if self.dao.get_customer_by_email(email):
            return None, "Email đã tồn tại"

        # Hash password
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        customer = Customer(name=name, email=email, number_phone=phone, password=hashed.decode('utf-8'))

        # Tạo customer
        return self.dao.create_customer(customer), None

    def login(self, email, password):
        customer = self.dao.get_customer_by_email(email)
        if not customer:
            return None, "Email không tồn tại"
        if bcrypt.checkpw(password.encode('utf-8'), customer.password.encode('utf-8')):
            return customer, None
        return None, "Sai mật khẩu"

    def get_customer_summary(self, customer):
        """Trả về thông tin an toàn, không bao gồm password"""
        return CustomerHelper.get_customer_summary(customer)
