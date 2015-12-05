from db import Db


class Organizations(Db):
    def get_goods(self):
        sql = 'SELECT * FROM Orders WHERE id = %s;'
        cursor = self.execute(sql, self.id)
        # doing smth
        cursor.close()

    def add_goods(self):
        pass

    def get_orders(self):
        pass

    def add_order(self):
        pass
