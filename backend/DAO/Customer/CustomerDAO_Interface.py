from abc import ABC, abstractmethod

class CustomerDAOInterface(ABC):
    @abstractmethod
    def create_customer(self, customer):
        pass

    @abstractmethod
    def get_customer_by_email(self, email):
        pass

    @abstractmethod
    def get_customer_by_id(self, cus_id):
        pass
