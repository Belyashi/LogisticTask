from models.db.db import Db


class Goods(Db):
    def get_all_goods(self):
        cursor = self.callfunc('get_all_goods')
        data = self.get_dict_list(['id', 'name', 'price', 'producer_id', 'weight', 'residue'], cursor)
        cursor.close()
        return data

    def reduce(self, good_id, count):
        try:
            self.callproc('reduce', (good_id, count,))
        except:
            raise ValueError('Reduced count must be not less than existing.')
