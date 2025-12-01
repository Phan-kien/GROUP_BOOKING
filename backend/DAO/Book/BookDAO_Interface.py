from abc import ABC, abstractmethod

class BookDAOInterface(ABC):

    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def get_book_by_id(self, book_id):
        pass

    @abstractmethod
    def create_book(self, cus_id, ticket_id, payment_id=None, date=None):
        pass

    @abstractmethod
    def update_book(self, book_id, cus_id=None, ticket_id=None, payment_id=None, date=None):
        pass

    @abstractmethod
    def delete_book(self, book_id):
        pass
