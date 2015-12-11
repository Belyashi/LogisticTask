from models.db.db import Db


class Organizations(Db):
    def get_organization_id(self, user_id):
        cur = self.execute('SELECT id FROM Organizations WHERE user_id = %s', (user_id, ))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            ValueError('Organization with user_id = %d does not exist' % user_id)
        return data[0][0]

    def get_goods(self, organization_id):
        sql = 'SELECT id FROM Goods WHERE producer_id = %s'
        cursor = self.execute(sql, (organization_id,))
        data = self.get_dict_list(['good_id'], cursor)
        cursor.close()
        return data

    def add_goods(self, name, price, organization_id, weight, residue):
        sql = (
            'INSERT INTO Goods '
            '(name, price, producer_id, weight, residue) '
            'VALUES (%s, %s, %s, %s, %s) '
        )
        cursor = self.execute(sql, (name, price, organization_id, weight, residue))
        cursor.close()

    def get_orders(self, organization_id):
        sql = (
            'SELECT order_id, delivered, count,'
            '(select name from Goods'
            'where id==Orders.goods_id limit 1)'
            'FROM Orders '
            'WHERE customer_id = %s'
        )
        cursor = self.execute(sql, (organization_id,))
        data = self.get_dict_list(['order_id', 'delivered', 'count', 'good'], cursor)
        cursor.close()
        return data

    def add_order(self, organization_id, good_id, count):
        self.__check_overflow_count(good_id, count)
        sql = (
            'INSERT INTO Orders'
            '(customer_id, delivered, goods_id, count)'
            'VALUES (%s, FALSE, %s, %s)'
        )
        cursor = self.execute(sql, (organization_id, good_id, count))
        cursor.close()
        # TODO: Manager assigns Driver, Route and so on to Order

    def __check_overflow_count(self, good_id, count):
        sql = 'SELECT residue FROM Goods WHERE id = %s'
        cursor = self.execute(sql, (good_id,))
        residue = cursor.fetchall()[0][0]
        cursor.close()
        if residue < count:
            raise OverflowError('residue must be larger, than count')
