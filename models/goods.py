from db import Db


class Goods(Db):
    def get_all_goods(self):
        sql = 'SELECT * FROM Orders;'
        cursor = self.execute(sql, self.id)
        # doing smth
        cursor.close()
