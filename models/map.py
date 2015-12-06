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