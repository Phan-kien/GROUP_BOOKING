from backend.DAO.Combo.ComboDAO_dao import ComboDAO

class ComboBusiness:
    def __init__(self):
        self.combo_dao = ComboDAO()

    def get_all_combos(self):
        return self.combo_dao.get_all_combos()

    def get_combo_by_id(self, combo_id):
        return self.combo_dao.get_combo_by_id(combo_id)

    def create_combo(self, combo_name, description, price):
        return self.combo_dao.create_combo(combo_name, description, price)

    def update_combo(self, combo_id, combo_name, description, price):
        self.combo_dao.update_combo(combo_id, combo_name, description, price)

    def delete_combo(self, combo_id):
        self.combo_dao.delete_combo(combo_id)
