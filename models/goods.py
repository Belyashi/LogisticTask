from models.db.db import Db


class Goods(Db):
    def get_all_goods(self):
        sql = 'SELECT id, name, price, producer_id, weight, residue FROM Goods where residue>0;'
        cursor = self.execute(sql)
        data = self.get_dict_list(['id', 'name', 'price', 'producer_id', 'weight', 'residue'], cursor)
        cursor.close()
        return data

    def reduce(self, good_id, count):
        sql = 'select residue from Goods where id=%s;'
        data = self.execute(sql, (good_id,))
        residue = [dict(zip(['residue'], item)) for item in data][0]['residue']
        if residue < count:
            raise ValueError('Reduced count must be not less than existing.')
        else:
            sql = 'update Goods set residue=%s where id=%s'
            self.execute(sql, (residue - count, good_id,))
