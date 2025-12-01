from backend.DAO.Customer.CustomerDAO_Interface import CustomerDAOInterface
from backend.DAO.Customer.Customer_entity import Customer
from backend.config import get_connection
import mysql.connector

class CustomerDAO(CustomerDAOInterface):
    def create_customer(self, customer):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO tbl_customer (name, email, number_phone, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (customer.name, customer.email, customer.number_phone, customer.password))
            conn.commit()
            customer.cus_id = cursor.lastrowid
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
