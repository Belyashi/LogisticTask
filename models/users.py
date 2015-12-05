from db import Db


class Users(Db):
    def login(self, login, password):
        pass

    def register(self, login, password):
        if self.__check_registered(login):
            raise ValueError('User is already registered')

        query = (
            'INSERT INTO Users '
            '(login, pass) '
            'VALUES (%s, %s)'
        )

        data_user = (login, password)

        cur = self.get_cursor()
        cur.execute(query, data_user)
        self.commit()
        cur.close()

    def __check_registered(self, login):
        query = (
            'SELECT login '
            'FROM Users '
            'WHERE login = %s'
        )
        cur = self.execute(query, (login))
        exist = cur.rowcount > 0
        cur.close()
        return exist

    def get_users(self):
        pass