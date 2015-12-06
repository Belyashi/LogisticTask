from db import Db


class Organizations(Db):
    def get_goods(self):
        sql = 'SELECT id FROM Goods WHERE producer_id = %s'
        cursor = self.execute(sql, (self.id,))
        data = [{'good_id': id} for id in cursor]
        cursor.close()
        return data

    def add_goods(self, name, price, weight, residue):
        sql = (
            'INSERT INTO Goods '
            '(name, price, producer_id, weight, residue) '
            'VALUES (%s, %s, %s, %s, %s) '
        )
        cursor = self.execute(sql, (name, price, self.id, weight, residue))
        # self.commit()
        cursor.close()

    def get_orders(self):
        sql = 'SELECT id FROM Orders WHERE customer_id = %s'
        cursor = self.execute(sql, (self.id,))
        data = [{'order_id': id} for id in cursor]
        cursor.close()
        return data

    def add_order(self, good_id, count):
        self.__check_overflow_count(good_id, count)
        cursor = self.execute_script('add_order', (self.id, good_id, count))
        # self.commit()
        cursor.close()
        # TODO: Manager assigns Driver, Route and so on to Order

    def __check_overflow_count(self, good_id, count):
        sql = 'SELECT residue FROM Goods WHERE id = %s'
        cursor = self.execute(sql, (good_id,))
        residue = cursor.fetchall()[0][0]
        cursor.close()
        if residue < count:
            raise OverflowError('residue must be larger, than count')


from users import Users


# u = Users()
# u.register_organization('pompom', 'ololo', 'orgname', 5)
org = Organizations()
org.id = 3
org.get_goods()
org.add_goods('good_name', 300, 43, 13)
org.get_orders()

