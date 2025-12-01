import re

class HallHelper:
    @staticmethod
    def format_name(name):
        """Chuẩn hóa hall_name: loại bỏ khoảng trắng đầu/cuối và ký tự đặc biệt"""
        if not name:
            return None
        name = name.strip()
        name = re.sub(r'[^\w\s]', '', name)
        return name
