import os
import cx_Oracle as oracle_tool

import models.db.config

_path_to_scripts = '/'.join(
    os.path.abspath(__file__).split('/')[:-2]
    + ['sql_scripts']
) + '/'


def create_db():
    db = oracle_tool.connect('system/oracle@127.0.0.1:1521/XE')
    db.autocommit(True)
    db.query("DROP DATABASE " + models.db.config.NAME)
    db.query("CREATE DATABASE " + models.db.config.NAME)
    db.close()


def create_tables():
    db = oracle_tool.connect('system/oracle@127.0.0.1:1521/XE')
    with open(_path_to_scripts + "create_tables.sql", "r") as f:
        sql = f.read()
    cur = db.cursor()
    cur.execute(sql)
    cur.close()
    db.close()


def make_test_data():
    db = oracle_tool.connect('system/oracle@127.0.0.1:1521/XE')
    db.autocommit(True)
    with open(_path_to_scripts + "test_data.sql", "r") as f:
        sql = f.read()
    cur = db.cursor()
    cur.execute(sql)
    cur.close()
    db.close()


if __name__ == '__main__':
    create_db()
    create_tables()
    make_test_data()
