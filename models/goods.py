from db import Db


class Goods(Db):
    def get_all_goods(self):
        sql = 'SELECT id, name, price, weight, residue FROM Goods'
        cursor = self.execute(sql)
        data = self.get_dict_list(['id', 'name', 'price', 'weight', 'residue'], cursor)
        cursor.close()
        return data
