from models.db.db import Db

import utils


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
            'SELECT id, delivered, count, '
            '(select name from Goods '
            'where id=Orders.goods_id limit 1) '
            'FROM Orders '
            'WHERE customer_id = %s'
        )
        cursor = self.execute(sql, (organization_id,))
        data = self.get_dict_list(['order_id', 'delivered', 'count', 'good'], cursor)
        cursor.close()
        return data

    def add_order(self, organization_id, good_id, count):
        self.__check_overflow_count(good_id, count)
        query = (
            'INSERT INTO Orders'
            '(customer_id, delivered, goods_id, count)'
            'VALUES (%s, FALSE, %s, %s)'
        )
        self.execute(query, (organization_id, good_id, count)).close()

        query = 'SELECT MAX(id) FROM Orders '
        cursor = self.execute(query)
        order_id = cursor.fetchall()[0][0]
        cursor.close()

        producer_city_id = self.__get_producer_city_id(good_id)

        query = 'SELECT city_id FROM Organizations WHERE id = %s '
        cursor = self.execute(query, (organization_id,))
        finish_city_id = cursor.fetchall()[0][0]
        cursor.close()

        driver_id = self.__get_driver(producer_city_id)

        self.__assign_order(driver_id, order_id)
        self.__assign_way(driver_id, producer_city_id, finish_city_id)

    def __check_overflow_count(self, good_id, count):
        sql = 'SELECT residue FROM Goods WHERE id = %s'
        cursor = self.execute(sql, (good_id,))
        residue = cursor.fetchall()[0][0]
        cursor.close()
        if residue < count:
            raise OverflowError('residue must be larger, than count')

    def __get_driver(self, city_id):
        query = (
            'SELECT id '
            'FROM Drivers '
            'WHERE last_city_id = %s '
            'AND on_way = FALSE '
            'limit 1'
        )
        cursor = self.execute(query, city_id)
        data = cursor.fetchall()
        cursor.close()
        if len(data) > 0:
            return data[0][0]
        query = 'SELECT id FROM Drivers WHERE on_way = FALSE limit 1'
        cursor = self.execute(query)
        data = cursor.fetchall()
        cursor.close()
        if len(data) == 0:
            raise Exception('no free drivers')
        return data[0][0]

    def __get_producer_city_id(self, good_id):
        query = (
            'SELECT city_id '
            'FROM Organizations '
            'WHERE id = '
                '(SELECT producer_id '
                'FROM Goods '
                'WHERE id = %s) '
        )
        cur = self.execute(query, good_id)
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            raise Exception('no such producer id')
        return data[0][0]

    def __assign_order(self, driver_id, order_id):
        query = ('INSERT INTO DriversOrders '
                 '(driver_id, order_id) '
                 'VALUES (%s, %s)')
        cur = self.execute(query, (driver_id, order_id))
        cur.close()

    def __assign_way(self, driver_id, start_ciy_id, finish_city_id):
        path = utils.dijsktra(utils.g, start_ciy_id, finish_city_id)
        for finish_city_id in path[1:]:
            query = (
                'INSERT INTO ROUTES '
                '(driver_id, way_id, performed) '
                '(%s, %s, %s) '
            )
            cur = self.execute(
                query,
                (driver_id, self.__get_way_id(start_ciy_id, finish_city_id), False)
            )
            cur.close()
            start_ciy_id = finish_city_id

    def __get_way_id(self, start_city_id, finish_city_id):
        query = (
            'SELECT id FROM WAYS '
            'WHERE start_city_id = %s AND finish_city_id = %s '
            'limit 1 '
        )
        cur = self.execute(query, (start_city_id, finish_city_id))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            raise Exception('no such way id')
        return data[0][0]
