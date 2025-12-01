from backend.DAO.Book.BookDAO_dao import BookDAO

class BookBusiness:
    def __init__(self):
        self.book_dao = BookDAO()

    def get_all_books(self):
        return self.book_dao.get_all_books()

    def get_book_by_id(self, book_id):
        return self.book_dao.get_book_by_id(book_id)

    def create_book(self, cus_id, ticket_id, payment_id=None, date=None):
        return self.book_dao.create_book(cus_id, ticket_id, payment_id, date)

    def update_book(self, book_id, cus_id=None, ticket_id=None, payment_id=None, date=None):
        self.book_dao.update_book(book_id, cus_id, ticket_id, payment_id, date)

    def delete_book(self, book_id):
        self.book_dao.delete_book(book_id)
