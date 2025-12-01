import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",  # đổi mật khẩu của bạn
        database="booking"            # đổi tên database bạn có
    )

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Kết nối MySQL thành công!")
        conn.close()
    except Exception as e:
        print("Lỗi kết nối:", e)
