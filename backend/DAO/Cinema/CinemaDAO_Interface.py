from abc import ABC, abstractmethod

class CinemaDAOInterface(ABC):

    @abstractmethod
    def create(self, cinema):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, cinema_id):
        pass

    @abstractmethod
    def update(self, cinema):
        pass

    @abstractmethod
    def delete(self, cinema_id):
        pass
