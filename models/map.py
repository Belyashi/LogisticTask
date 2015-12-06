from db import Db


class Map(Db):
    def get_route(self):
        pass

    def get_all_cities(self):
        cur = self.execute('SELECT id, name FROM Cities')
        data = self.get_dict_list(['id', 'name'], cur)
        cur.close()
        return data