from db import Db


class Organizations(Db):
    def get_goods(self):
        sql = 'SELECT * FROM Goods WHERE customer_id = %s'
        cursor = self.execute(sql, self.id)
        # doing smth
        cursor.close()

    def add_goods(self):
        pass

    def get_orders(self):
        sql = 'SELECT * FROM Orders WHERE customer_id = %s'
        cursor = self.execute(sql, self.id)
        # doing smth
        cursor.close()

    def add_order(self):
        pass
