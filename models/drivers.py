from models.db.db import Db

import utils


class Drivers(Db):
    def get_driver_info(self, driver_id):
        query = (
            'SELECT user_id, capacity, last_city_id, on_way '
            'FROM Drivers '
            'WHERE id = %s '
        )
        cur = self.execute(query, (driver_id,))
        data = self.get_dict_list(['user_id', 'capacity', 'last_city_id', 'on_way'], cur)
        data[0]['on_way'] = bool(data[0]['on_way'])
        return data

    def get_driver_id(self, user_id):
        cur = self.execute('SELECT id FROM Drivers WHERE user_id = %s', (user_id, ))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            ValueError('Driver with user_id = %d does not exist' % user_id)
        return data[0][0]

    def get_available_drivers(self, city_id):
        # TODO: add order_id parameter
        query = ('SELECT id, capacity '
                 'FROM Drivers '
                 'WHERE on_way = FALSE AND (last_city_id = %s OR last_city_id = NULL)')
        cur = self.execute(query, (city_id,))
        data = self.get_dict_list(['id', 'capacity'], cur)
        cur.close()
        return data

    def get_orders(self, driver_id):
        query = (
            'select id, delivered, count, '
                '(select name from Organizations '
                'where id=Orders.customer_id limit 1), '
                '(select name from Goods where id=Orders.goods_id limit 1) '
            'from Orders where id in '
            '(select order_id from DriversOrders '
            'where driver_id=%s) '
        )
        cur = self.execute(query, (driver_id,))
        data = self.get_dict_list(['order_id', 'delivered', 'count', 'customer', 'good'], cur)
        cur.close()
        return data

    def get_next_point(self, driver_id):
        query = ('SELECT t1.id, t2.start_city_id, t2.finish_city_id, '
                 '(select name from Cities where id=t2.start_city_id) '
                 'as start_city, '
                 '(select name from Cities where id=t2.finish_city_id) '
                 'as finish_city '
                 'FROM Routes as t1'
                 '  INNER JOIN Ways as t2'
                 '     ON t1.way_id = t2.id '
                 'WHERE t1.driver_id = %s and t1.performed = false '
                 'ORDER BY t1.id '
                 'LIMIT 1')
        cur = self.execute(query, (driver_id,))
        data = cur.fetchall()
        cur.close()

        if len(data) == 0:
            return None
        return self.get_dict(
            [
                'id', 'start_city_id', 'finish_city_id',
                'start_city', 'finish_city'
            ],
            data[0]
        )

    def start_move(self, driver_id):
        self.__get_next_point_or_raise(driver_id)
        self.__set_on_way(driver_id, True)

    def arrive_to_point(self, driver_id):
        next_point = self.__get_next_point_or_raise(driver_id)
        self.__make_performed_next_point(driver_id)
        self.__set_last_city_id(driver_id, next_point['finish_city_id'])
        self.__set_on_way(driver_id, False)
        self.__unload_orders(driver_id, next_point['finish_city_id'])

    def __get_next_point_or_raise(self, driver_id):
        next_point = self.get_next_point(driver_id)
        if next_point is None:
            raise ValueError('Driver does not have next point')
        return next_point

    def __set_on_way(self, driver_id, on_way):
        query = ('UPDATE Drivers '
                 'SET on_way = %s '
                 'WHERE id = %s')
        cur = self.execute(query, (on_way, driver_id))
        cur.close()

    def __unload_orders(self, driver_id, city_id):
        query = ('UPDATE DriversOrders as t1 '
                 '  INNER JOIN Orders as t2 '
                 '     ON t1.order_id = t2.id '
                 '  INNER JOIN Organizations as t3 '
                 '     ON t2.customer_id = t3.id '
                 'SET t2.delivered = TRUE '
                 'WHERE t1.driver_id = %s AND t3.city_id = %s')
        cur = self.execute(query, (driver_id, city_id))
        cur.close()

    def __set_last_city_id(self, driver_id, last_city_id):
        query = ('UPDATE Drivers '
                 'SET last_city_id = %s '
                 'WHERE id = %s')
        cur = self.execute(query, (last_city_id, driver_id))
        cur.close()

    def __make_performed_next_point(self, driver_id):
        query = ('UPDATE Routes '
                 'SET performed = TRUE '
                 'WHERE driver_id = %s AND performed = FALSE '
                 'ORDER BY id '
                 'LIMIT 1')
        cur = self.execute(query, (driver_id,))
        cur.close()

    def assign_order(self, driver_id, order_id):
        # TODO: check if possible
        query = ('INSERT INTO DriversOrders '
                 '(driver_id, order_id) '
                 'VALUES (%s, %s)')
        cur = self.execute(query, (driver_id, order_id))
        cur.close()

    def assign_way(self, driver_id, start_ciy_id, finish_city_id):
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
            'SELECT MIN(id) FROM WAYS '
            'FROM WAYS '
            'WHERE start_city_id = %s AND finish_city_id = %s '
        )
        cur = self.execute(query, (start_city_id, finish_city_id))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            raise Exception('no such way id')
        return data[0][0]
