from backend.DAO.Customer.CustomerDAO_Interface import CustomerDAOInterface
from backend.DAO.Customer.Customer_entity import Customer
from backend.config import get_connection
import mysql.connector

class CustomerDAO(CustomerDAOInterface):
    def create_customer(self, customer):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = """
                  INSERT INTO tbl_customer (cus_id, name, email, number_phone)
                  VALUES (%s, %s, %s, %s) \
                  """
            cursor.execute(sql, (
                customer.cus_id,
                customer.name if customer.name else None,
                customer.email if customer.email else None,
                customer.number_phone if customer.number_phone else None
            ))
            conn.commit()
            return customer
        finally:
            cursor.close()
            conn.close()

    def get_customer_by_email(self, email):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT * FROM tbl_customer WHERE email=%s"
            cursor.execute(sql, (email,))
            row = cursor.fetchone()
            if row:
                return Customer(**row)
            return None
        finally:
            cursor.close()
            conn.close()

    def get_customer_by_id(self, cus_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql = "SELECT * FROM tbl_customer WHERE cus_id=%s"
            cursor.execute(sql, (cus_id,))
            row = cursor.fetchone()
            if row:
                return Customer(**row)
            return None
        finally:
            cursor.close()
            conn.close()
