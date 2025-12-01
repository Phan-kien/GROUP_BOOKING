from abc import ABC, abstractmethod

class ShowtimeDAOInterface(ABC):

    @abstractmethod
    def get_all_showtimes(self):
        pass

    @abstractmethod
    def get_showtime_by_id(self, showtime_id):
        pass

    @abstractmethod
    def create_showtime(self, showtime):
        pass
