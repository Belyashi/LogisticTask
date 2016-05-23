from models.db.db import Db

import utils


class Organizations(Db):
    def get_organization_id(self, user_id):
        cur = self.callfunc('get_organization_id', (user_id,))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            ValueError('Organization with user_id = %d does not exist' % user_id)
        return data[0][0]

    def get_goods(self, organization_id):
        cursor = self.callfunc('get_goods', (organization_id,))
        data = self.get_dict_list(['good_id'], cursor)
        cursor.close()
        return data

    def add_goods(self, name, price, organization_id, weight, residue):
        cursor = self.callfunc('add_goods', (name, price, organization_id, weight, residue,))
        cursor.close()

    def get_orders(self, organization_id):
        cursor = self.callfunc('get_orders', (organization_id,))
        data = self.get_dict_list(['order_id', 'delivered', 'count', 'good'], cursor)
        cursor.close()
        return data

    def add_order(self, organization_id, good_id, count):
        self.__check_overflow_count(good_id, count)
        query = (
            'INSERT INTO Orders'
            '(customer_id, delivered, goods_id, count)'
            "VALUES (%s, 'N', %s, %s)"
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
        cursor = self.callfunc('check_overflow_count', (good_id,))
        residue = cursor.fetchall()[0][0]
        cursor.close()
        if residue < count:
            raise OverflowError('residue must be larger, than count')

    def __get_driver(self, city_id):
        cursor = self.callfunc('get_driver_for_deliver', (city_id,))
        data = cursor.fetchall()
        cursor.close()
        if len(data) == 0:
            raise Exception('no free drivers')
        return data[0][0]

    def __get_producer_city_id(self, good_id):
        return self.callfunc('get_producer_city_id', (good_id,))

    def __assign_order(self, driver_id, order_id):
        self.callproc('assign_order', (driver_id, order_id,))

    def __assign_way(self, driver_id, start_ciy_id, finish_city_id):
        path = utils.dijsktra(start_ciy_id, finish_city_id)
        for finish_city_id in path[1:]:
            query = (
                'INSERT INTO Routes '
                '(driver_id, way_id, performed) '
                "VALUES (%s, %s, 'N') "
            )
            way_id = self.__get_way_id(start_ciy_id, finish_city_id)
            cur = self.execute(query, (driver_id, way_id))
            cur.close()
            start_ciy_id = finish_city_id

    def __get_way_id(self, start_city_id, finish_city_id):
        query = (
            'SELECT id FROM Ways '
            'WHERE start_city_id = %s AND finish_city_id = %s '
            'AND ROWNUM <= 1'
        )
        cur = self.execute(query, (start_city_id, finish_city_id))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            raise Exception('no such way id')
        return data[0][0]
