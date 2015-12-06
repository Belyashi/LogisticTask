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
        self.execute(sql, name, price, self.id, weight, residue).close()

    def get_orders(self):
        sql = 'SELECT * FROM Orders WHERE customer_id = %s'
        cursor = self.execute(sql, self.id)
        cursor.fetchall()
        cursor.close()

    def add_order(self, good_id, count):
        self.__check_overflow_count(good_id, count)
        self.execute_script('add_orders', self.id, good_id, count).close()
        # TODO: Manager assigns Driver, Route and so on to Order
        pass

    def __check_overflow_count(self, good_id, count):
        sql = 'SELECT residue FROM Goods WHERE id = %s'
        cursor = self.execute(sql, good_id)
        residue = cursor[0]
        cursor.close()
        if residue < count:
            raise OverflowError('residue must be larger, than count')
