import MySQLdb
import config


class Db(object):
    def __init__(self):
        self.db = MySQLdb.connect(host=config.HOST,
                                  user=config.USER,
                                  passwd=config.PASSWD,
                                  db=config.NAME)

    def __del__(self):
        self.db.close()

    def get_cursor(self):
        return self.db.cursor()

    def commit(self):
        return self.db.commit()

    def execute(self, query, *args):
        cursor = self.db.cursor()
        cursor.execute(query, args)
        return cursor

    def execute_script(self, sql_script, *args):
        with open('./sql_scripts/{0}.sql'.format(sql_script), 'r') as f:
            query = f.read()
        return self.execute(query, *args)