from abc import ABC, abstractmethod

class HallDAOInterface(ABC):

    @abstractmethod
    def create_hall(self, hall):
        pass

    @abstractmethod
    def get_all_halls(self):
        pass

    @abstractmethod
    def get_hall_by_id(self, hall_id):
        pass
