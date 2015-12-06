from db import Db


class Users(Db):
    def login(self, login, password):
        """:returns user id"""
        query = (
            'SELECT id, pass '
            'FROM Users '
            'WHERE login = %s'
        )
        cur = self.execute(query, login)
        rows = cur.fetchall()
        cur.close()

        if len(rows) == 0:
            raise ValueError('User does not exist')
        elif rows[0][1] != password:
            raise ValueError('Password is incorrect')
        else:
            return rows[0][0]

    def register_driver(self, login, password, capacity, location_city_id):
        user_id = self.__register_user(login, password)

        cur = self.get_cursor()
        query = (
            'INSERT INTO Drivers '
            '(user_id, capacity, location_city_id) '
            'VALUES (%s, %s, %s)'
        )
        cur.execute(query, (user_id, capacity, location_city_id))
        self.commit()
        cur.close()

        return user_id

    def register_organization(self, login, password, name, city_id):
        user_id = self.__register_user(login, password)

        cur = self.get_cursor()
        query = (
            'INSERT INTO Organizations '
            '(user_id, name, city_id) '
            'VALUES (%s, %s, %s)'
        )
        cur.execute(query, (user_id, name, city_id))
        self.commit()
        cur.close()

        return user_id

    def __register_user(self, login, password):
        if self.__check_registered(login):
            raise ValueError('User is already registered')

        cur = self.get_cursor()

        query = (
            'INSERT INTO Users '
            '(login, pass) '
            'VALUES (%s, %s)'
        )
        cur.execute(query, (login, password))
        self.commit()

        cur.execute('SELECT id FROM Users WHERE login = %s', (login,))
        user_id = cur.fetchall()[0][0]

        cur.close()

        return user_id

    def __check_registered(self, login):
        query = (
            'SELECT login '
            'FROM Users '
            'WHERE login = %s'
        )
        cur = self.execute(query, (login,))
        exist = cur.rowcount > 0
        cur.close()
        return exist

    def get_all(self):
        query = 'SELECT id, login FROM Users'
        cur = self.execute(query)
        data = [{
                    'id': id,
                    'login': login
                }
                for id, login in cur]
        cur.close()
        return data
