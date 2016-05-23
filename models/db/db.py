import os

from PyQt4.QtCore import QString

import cx_Oracle as oracle_tool

_path_to_scripts = '/'.join(
    os.path.abspath(__file__).split('/')[:-2]
    + ['sql_scripts']
) + '/'


class Db(object):
    def __init__(self):
         self.con = oracle_tool.connect('system/oracle@127.0.0.1:1521')

    def __del__(self):
        self.con.close()

    def get_cursor(self):
        return self.con.cursor()

    def get_dict_list(self, columns, cursor):
        return [self.get_dict(columns, item) for item in cursor]

    def get_dict(self, columns, item):
        return dict(zip(columns, item))

    def execute(self, query, params=None):
        if params is None:
            params = []
        cur = self.con.cursor()
        params = [str(p) if type(p) == QString else p for p in params]
        params = [('Y' if p else 'N') if type(p) == bool else p for p in params]
        params = ["'{}'".format(p) if type(p) == str else p for p in params]
        params = tuple(params)
        query = query % params
        if len(query) > 0 and query[-1] == ';':
            query = query[:-1]
        print 'query {}'.format(repr(query))
        cur.execute(query)
        return cur

    def callfunc(self, name, params):
        cursor = self.con.cursor()
        cursor.callfunc(name, oracle_tool.CURSOR, params)
        return cursor


db = Db()
cur = db.execute('select * from Users')
print cur.fetchall()