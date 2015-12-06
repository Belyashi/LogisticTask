from models.db.db import Db


class Goods(Db):
    def get_all_goods(self):
        sql = 'SELECT id, name, price, producer_id, weight, residue FROM Goods'
        cursor = self.execute(sql)
        data = self.get_dict_list(['id', 'name', 'price', 'producer_id', 'weight', 'residue'], cursor)
        cursor.close()
        return data
