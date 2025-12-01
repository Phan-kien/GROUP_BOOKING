import uuid

class CinemaHelper:
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())  # tạo cinema_id duy nhất
