from abc import ABC, abstractmethod

class ComboDAOInterface(ABC):

    @abstractmethod
    def get_all_combos(self):
        pass

    @abstractmethod
    def get_combo_by_id(self, combo_id):
        pass

    @abstractmethod
    def create_combo(self, combo_name, description, price):
        pass

    @abstractmethod
    def update_combo(self, combo_id, combo_name, description, price):
        pass

    @abstractmethod
    def delete_combo(self, combo_id):
        pass
