from models.db.db import Db


class Map(Db):
    def get_route(self):
        pass

    def get_all_cities(self):
        cur = self.execute('SELECT id, name FROM Cities')
        data = self.get_dict_list(['id', 'name'], cur)
        cur.close()
        return data

    def get_all_ways(self):
        cur = self.execute('SELECT start_city_id, finish_city_id, length FROM Ways')
        data = self.get_dict_list(['start_city_id', 'finish_city_id', 'length'], cur)
        cur.close()
        return data

    def get_city(self, city_id):
        query = 'SELECT name FROM Cities WHERE id = %s'
        cur = self.execute(query, (city_id,))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            raise Exception('no such city id')
        return data[0][0]

    def get_city_id(self, city_name):
        query = 'SELECT id FROM Cities WHERE name = %s'
        cur = self.execute(query, (city_name,))
        data = cur.fetchall()
        cur.close()
        if len(data) == 0:
            raise Exception('no such city name')
        return data[0][0]
