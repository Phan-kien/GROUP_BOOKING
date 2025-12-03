from backend.DAO.Showtime.Showtime_entity import Showtime
import uuid

class ShowtimeHelper:
    @staticmethod
    def normalize_time(time_str):
        parts = time_str.split(":")
        if len(parts) == 2:
            parts.append("00")
        elif len(parts) != 3:
            raise ValueError("Invalid time format. Must be HH:MM or HH:MM:SS")
        h, m, s = map(int, parts)
        return f"{h:02d}:{m:02d}:{s:02d}"