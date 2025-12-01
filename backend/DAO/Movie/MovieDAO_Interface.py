from abc import ABC, abstractmethod

class MovieDAOInterface(ABC):

    @abstractmethod
    def get_all_movies(self):
        pass

    @abstractmethod
    def get_movie_by_id(self, movie_id):
        pass

    @abstractmethod
    def create_movie(self, movie):
        pass
