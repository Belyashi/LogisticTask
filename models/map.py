from db import Db


class Map(Db):
    def get_route(self):
        pass

    def get_all_cities(self):
        cur = self.execute('SELECT id, name FROM Cities')
        data = [{
                    'id': id,
                    'name': name
                } for id, name in cur]
        cur.close()
        return data