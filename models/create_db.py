import MySQLdb
import config


def create_db():
    db = MySQLdb.connect(host=config.HOST,
                         user=config.USER,
                         passwd=config.PASSWD)
    db.query("DROP DATABASE " + config.NAME)
    db.query("CREATE DATABASE " + config.NAME)
    db.commit()
    db.close()


def create_tables():
    db = MySQLdb.connect(host=config.HOST,
                         user=config.USER,
                         passwd=config.PASSWD,
                         db=config.NAME)
    with open("./sql_scripts/create_tables.sql", "r") as f:
        sql = f.read()
    cur = db.cursor()
    cur.execute(sql)
    cur.close()
    db.close()

def make_test_data():
    db = MySQLdb.connect(host=config.HOST,
                         user=config.USER,
                         passwd=config.PASSWD,
                         db=config.NAME)
    db.autocommit(True)
    with open("./sql_scripts/test_data.sql", "r") as f:
        sql = f.read()
    cur = db.cursor()
    cur.execute(sql)
    cur.close()
    db.close()

import sys

if len(sys.argv) > 1 and sys.argv[1] == 'create':
    create_db()
    create_tables()
    make_test_data()
