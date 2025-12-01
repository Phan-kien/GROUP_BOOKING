from backend.DAO.Book.Book_entity import Book

class BookHelper:
    @staticmethod
    def from_row(row):
        return Book(
            book_id=row['book_id'],
            cus_id=row['cus_id'],
            ticket_id=row['ticket_id'],
            payment_id=row['payment_id'],
            date=row['date']
        )
