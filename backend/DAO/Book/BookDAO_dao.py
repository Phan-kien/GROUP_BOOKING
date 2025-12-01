from backend.DAO.Book.BookDAO_Interface import BookDAOInterface
from backend.DAO.Book.Book_class import BookHelper
from backend.DAO.Book.Book_entity import Book
from backend.config import get_connection

class BookDAO(BookDAOInterface):

    def get_all_books(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_book")
        rows = cursor.fetchall()
        conn.close()
        return [BookHelper.from_row(r) for r in rows]

    def get_book_by_id(self, book_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tbl_book WHERE book_id=%s", (book_id,))
        row = cursor.fetchone()
        conn.close()
        return BookHelper.from_row(row) if row else None

    def create_book(self, cus_id, ticket_id, payment_id=None, date=None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tbl_book (cus_id, ticket_id, payment_id, date) VALUES (%s, %s, %s, %s)",
            (cus_id, ticket_id, payment_id, date)
        )
        conn.commit()
        book_id = cursor.lastrowid
        conn.close()
        return Book(book_id, cus_id, ticket_id, payment_id, date)

    def update_book(self, book_id, cus_id=None, ticket_id=None, payment_id=None, date=None):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tbl_book SET cus_id=%s, ticket_id=%s, payment_id=%s, date=%s WHERE book_id=%s",
            (cus_id, ticket_id, payment_id, date, book_id)
        )
        conn.commit()
        conn.close()

    def delete_book(self, book_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_book WHERE book_id=%s", (book_id,))
        conn.commit()
        conn.close()
