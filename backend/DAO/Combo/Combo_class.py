from backend.DAO.Combo.Combo_entity import Combo

class ComboHelper:
    @staticmethod
    def from_row(row):
        return Combo(
            combo_id=row['combo_id'],
            combo_name=row['combo_name'],
            description=row['description'],
            price=row['price']
        )
