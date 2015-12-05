from db import Db


class Organizations(Db):
    def get_goods(self):
        sql = 'SELECT * FROM Goods WHERE customer_id = %s'
        cursor = self.execute(sql, self.id)
        rows = cursor.fetchall()
        cursor.close()

    def add_goods(self, name, price, weight, residue):
        sql = (
            'INSERT INTO Goods'
            '(name, price, producer_id, weight, residue)'
            'VALUES (%s, %s, %s, %s, %s)'
        )
        cursor = self.execute(sql, name, price, self.id, weight, residue)
        rows = cursor.fetchall()
        cursor.close()

    def get_orders(self):
        sql = 'SELECT * FROM Orders WHERE customer_id = %s'
        cursor = self.execute(sql, self.id)
        cursor.fetchall()
        cursor.close()

    def add_order(self):
        cursor = self.execute_script('add_orders')
        rows = cursor.fetchall()
        cursor.close()
        # TODO: Manager assigns Driver, Route and so on to Order
        pass
