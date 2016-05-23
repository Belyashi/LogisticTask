from models.db.db import Db


class Drivers(Db):
    def get_driver_info(self, driver_id):
        cursor = self.callfunc('get_driver_info', (driver_id,))
        data = cursor.fetchall()
        cursor.close()
        data[0]['on_way'] = (data[0]['on_way'] == 'Y')
        return data[0]

    def get_driver_id(self, user_id):
        cur = self.callfunc('get_driver_id', (user_id,))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            ValueError('Driver with user_id = %d does not exist' % user_id)
        return data[0][0]

    def get_available_drivers(self, city_id):
        cur = self.callfunc('get_available_drivers', (city_id,))
        data = self.get_dict_list(['id', 'capacity'], cur)
        cur.close()
        return data

    def get_orders(self, driver_id):
        cur = self.callfunc('get_orders', (driver_id,))
        data = self.get_dict_list(['order_id', 'delivered', 'count', 'customer', 'good'], cur)
        cur.close()
        return data

    def get_next_point(self, driver_id):
        cur = self.callfunc('get_next_point', (driver_id,))
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
        self.callproc('start_move', (driver_id,))

    def arrive_to_point(self, driver_id):
        self.callproc('arrive_to_point', (driver_id,))
