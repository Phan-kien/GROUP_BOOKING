from backend.DAO.Customer.CustomerDAO_dao import CustomerDAO
from backend.DAO.Customer.Customer_entity import Customer
from backend.DAO.Customer.Customer_class import CustomerHelper
import bcrypt

class CustomerBusiness:
    def __init__(self):
        self.dao = CustomerDAO()

    def register(self, cus_id, name=None, email=None, phone=None):
        customer = Customer(cus_id=cus_id, name=name, email=email, number_phone=phone)
        return self.dao.create_customer(customer)

    def get_customer_by_id(self, cus_id):
        return self.dao.get_customer_by_id(cus_id)