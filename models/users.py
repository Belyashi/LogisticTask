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
        cur = self.execute(query, login)
        exist = cur.rowcount > 0
        cur.close()
        return exist

    def get_users(self):
        pass