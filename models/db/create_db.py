import MySQLdb
import models.config


def create_db():
    db = MySQLdb.connect(host=models.config.HOST,
                         user=models.config.USER,
                         passwd=models.config.PASSWD)
    db.autocommit(True)
    db.query("DROP DATABASE " + models.config.NAME)
    db.query("CREATE DATABASE " + models.config.NAME)
    # db.commit()
    db.close()


def create_tables():
    db = MySQLdb.connect(host=models.config.HOST,
                         user=models.config.USER,
                         passwd=models.config.PASSWD,
                         db=models.config.NAME)
    with open("./sql_scripts/create_tables.sql", "r") as f:
        sql = f.read()
    cur = db.cursor()
    cur.execute(sql)
    cur.close()
    db.close()

def make_test_data():
    db = MySQLdb.connect(host=models.config.HOST,
                         user=models.config.USER,
                         passwd=models.config.PASSWD,
                         db=models.config.NAME)
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
